import sys
import subprocess
import os
import time
import shutil
import yaml

start = time.time() #start timer

if os.path.exists("data"):
  os.remove("data")
  f_data = open("data", "x")
else:
  f_data = open("data", "x")
f_data.close()

if os.path.exists("score"):
  os.remove("score")
  f_score = open("score", "x")
else:
  f_score = open("score", "x")
f_score.close()


if os.path.exists("max_score"):
  os.remove("max_score")
  f_max_score = open("max_score", "x")
else:
  f_max_score = open("max_score", "x")
f_max_score.close()

if os.path.exists("routeblk"):
  os.remove("routeblk")
  f_routeblk = open("routeblk", "x")
else:
  f_routeblk = open("routeblk", "x")
f_routeblk.close()

if os.path.exists("placeblk"):
  os.remove("placeblk")
  f_placeblk = open("placeblk", "x")
else:
  f_placeblk = open("placeblk", "x")
f_placeblk.close()

def save_best():
  
  path = "best_results"
  if os.path.exists(path):
      shutil.rmtree(path)
  os.makedirs(path, exist_ok = True) 

  source_dir = r"design_file.dat"
  destination_dir = r"best_results/design_file.dat"
  shutil.copytree(source_dir, destination_dir)

  #generated def
  src_path = r"output/fpu_postrouting.def"
  dst_path = r"best_results/best_postrouting.def"
  shutil.copy(src_path, dst_path)

  #generated verilog
  src_path = r"output/fpu_postrouting.v"
  dst_path = r"best_results/best_postrouting.v"
  shutil.copy(src_path, dst_path)

  #lef
  src_path = r"NangateOpenCellLibrary.lef"
  dst_path = r"best_results/NangateOpenCellLibrary.lef"
  shutil.copy(src_path, dst_path)

  #gds
  src_path = r"NangateOpenCellLibrary.gds"
  dst_path = r"best_results/NangateOpenCellLibrary.gds"
  shutil.copy(src_path, dst_path)

  #blockage yaml
  src_path = r"blockage.yaml"
  dst_path = r"best_results/best_blockages.yaml"
  shutil.copy(src_path, dst_path)

def block_yaml():
  with open("routeblk") as fp_setup:
    data = fp_setup.readlines()
    setup_data = data[0].split("\n")
    routeblk_llx = float(setup_data[0])
    setup_data = data[1].split("\n")
    routeblk_lly = float(setup_data[0])
    setup_data = data[2].split("\n")
    routeblk_urx = float(setup_data[0])
    setup_data = data[3].split("\n")
    routeblk_ury = float(setup_data[0])


  with open("placeblk") as fp_setup:
      data = fp_setup.readlines()
      setup_data = data[0].split("\n")
      placeblk_llx = float(setup_data[0])
      setup_data = data[1].split("\n")
      placeblk_lly = float(setup_data[0])
      setup_data = data[2].split("\n")
      placeblk_urx = float(setup_data[0])
      setup_data = data[3].split("\n")
      placeblk_ury = float(setup_data[0])


  pnr_blockage = { "place_blockage" : {"x1" : placeblk_llx , "x2" : placeblk_urx, "y1" : placeblk_lly, "y2" : placeblk_ury}, \
  "route_blockage" : {"x1" : routeblk_llx , "x2" : routeblk_urx, "y1" : routeblk_lly, "y2" : routeblk_ury}}
  with open('blockage.yaml', 'w') as outfile:
    yaml.dump(pnr_blockage, outfile, sort_keys=False)

def metal_layer(data):
    metal6 = (int(data) & 1) >> 0
    metal5 = (int(data) & 2) >> 1
    metal4 = (int(data) & 4) >> 2
    metal3 = (int(data) & 8) >> 3
    metal2 = (int(data) & 16) >> 4
    metal1 = (int(data) & 32) >> 5
    return metal1, metal2, metal3, metal4, metal5, metal6


def block_test(metal1, metal2, metal3, metal4, metal5, metal6, max_score):
  position_options = [45, 50, 55]
  for position in position_options:
    f_data = open("data", "w")
    f_data.write(str(position) + '\n')
    f_data.write(str(metal1) + '\n')
    f_data.write(str(metal2) + '\n')
    f_data.write(str(metal3) + '\n')
    f_data.write(str(metal4) + '\n')
    f_data.write(str(metal5) + '\n')
    f_data.write(str(metal6) + '\n')
    f_data.close()

    done = subprocess.Popen([f"innovus -nowin < innovus_skeleton_fpu.tcl"], shell=True)
    done.wait()
    print("done subprocess")
    
    block_yaml()

    checker_command = 'python3 ./checkers/combined_checker.py output/fpu_postrouting.v blockage.yaml'
    done = subprocess.Popen([checker_command], shell=True)
    done.wait()
    print("done subprocess")

    with open("combined_checker_output.txt") as f_checker:
        if ' No place violations found' in f_checker.read():
            success_place = 1
        else:
            success_place = 0
    print(success_place)

    with open("combined_checker_output.txt") as f_checker:
        if ' No route violations found' in f_checker.read():
            success_route = 1
        else:
            success_route = 0
    print(success_route)

    with open("combined_checker_output.txt") as f_checker:
        data = f_checker.readlines()
        for setup_slack in data:
            if (setup_slack.startswith(" No setup timing violations found. Setup Slack:")):
                setup_data_temp = setup_slack.split(": ")
                setup_data = setup_data_temp[1].split("\n")
                print(setup_data[0])
        for drc_errors in data:
            if (drc_errors.startswith("Checking DRC errors...")):
                continue
            if (drc_errors.startswith(" Total Violations :")):
                drc_errors_data_temp = drc_errors.split(": ")
                drc_errors_data = drc_errors_data_temp[1].split(" Viols.")
                print(drc_errors_data[0])
        for area in data:
            if (area.startswith(" Core area:")):
                area_data_temp = area.split(": ")
                area_data = area_data_temp[1].split(" um^2")
                print(area_data[0])
        for twl in data:
            if (twl.startswith(" Total wire length:")):
                twl_data_temp = twl.split(": ")
                twl_data = twl_data_temp[1].split(" um")
                print(twl_data[0])
        

    #FOM
    #weight
    alpha = 1
    beta = 13
    gamma = 0.075
    sigma = 0.0001
    epsilon = 3
    #figures
    basetwl = 98000
    basedrc = 11
    layer_num = metal1 + metal2 + metal3 + metal4 + metal5 + metal6
    setup_slack = float(setup_data[0])
    twl = float(twl_data[0])
    drc_violation = float(drc_errors_data[0])


    score = alpha*layer_num + beta*setup_slack - gamma*(drc_violation-basedrc) - sigma*(twl-basetwl) + epsilon*success_place
    end = time.time()
    time_elapsed = end - start
    print("score FOM: " + str(score))
    f_score = open("score", "a")
    f_score.write("Time = " + str(time_elapsed) + ": " + "Score = " + str(score) + '\n'\
                  "position = " + str(position) + "; metal1 = " + str(metal1) + "; metal2 = " + str(metal2) + "; metal3 = " + str(metal3) + "; metal4 = " + str(metal4) + "; metal5 = " + str(metal5) + "; metal6 = " + str(metal6) + '\n'  + '\n')
    f_score.flush()
    f_score.close
    
    
    if(score > max_score):
      print("score " + str(score) + " > " + "max score " + str(max_score) + "\n")
      max_score = score
      save_best()
      f_max_score = open("max_score", "a")
      f_max_score.write(str(max_score) + '\n')
      f_max_score.flush()
      f_max_score.close
    
    # end of function
    f_data = open("data", "w")
    f_data.truncate(0)
    f_data.seek(0)
    f_data.close()
    f_checker.close()

    done = subprocess.Popen([f"./clean.sh"], shell=True)
    done.wait()
    done = subprocess.Popen([f"./clean_checkers.sh"], shell=True)
    done.wait()

    #out of time 1hr 30mins
    if(time_elapsed > 5400):
      print("time_elapsed = " + str(end-start) + "s")
      stop_time = 1
      return stop_time, max_score
    else:
      stop_time = 0
  return stop_time, max_score

#main

skeleton_path = "innovus_skeleton_fpu.tcl"

if len(sys.argv) > 1:
    NEW_UTIL = sys.argv[1]

def replace_line(lines,line_no,new_line):
    lines[line_no] = new_line
    return lines

with open(skeleton_path, 'r') as file:
    lines = file.readlines()
    lines = replace_line(lines, 61, f"set UTIL {NEW_UTIL}\n")

with open(skeleton_path, 'w') as file:
    file.writelines(lines)

i = 31 #6 layers but not blocking metal1
max_score = 0
while i > 0:
  metal1, metal2, metal3, metal4, metal5, metal6 = metal_layer(i)
  stop_time, score = block_test(metal1, metal2, metal3, metal4, metal5, metal6, max_score)
  if(score > max_score):
    max_score = score
  i-=1
  print("max score = " + str(max_score))
  if(stop_time == 1):
    break


