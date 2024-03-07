import sys
import subprocess
import os
import time

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
f_score = open("score", "w")
f_score.write("Score\n")
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
 
def metal_layer(data):
    metal6 = (int(data) & 1) >> 0
    metal5 = (int(data) & 2) >> 1
    metal4 = (int(data) & 4) >> 2
    metal3 = (int(data) & 8) >> 3
    metal2 = (int(data) & 16) >> 4
    metal1 = (int(data) & 32) >> 5
    return metal1, metal2, metal3, metal4, metal5, metal6


def block_test(metal1, metal2, metal3, metal4, metal5, metal6):
  position = 40
  max_score = -10000
  while position <= 60:
    f_data = open("data", "w")
    f_data.write(str(position) + '\n')
    f_data.write(str(metal1) + '\n')
    f_data.write(str(metal2) + '\n')
    f_data.write(str(metal3) + '\n')
    f_data.write(str(metal4) + '\n')
    f_data.write(str(metal5) + '\n')
    f_data.write(str(metal6) + '\n')
    f_data.close()
    position += 1 #detail of blk
    done = subprocess.Popen([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)
    done.wait()
    print("done subprocess")
      
    with open('output/s1494.drc.rpt') as fp_drc:
      if 'No DRC violations were found' in fp_drc.read():
        print("No DRC Violations")
        status_drc = 0
      else:
        status_drc = 1 
      
    with open("output/summary.rpt") as fp_summ:
        data = fp_summ.readlines()

    with open("output/s1494_postrouting_setup.tarpt") as fp_setup:
        data_setup = fp_setup.readlines()


    #Total Wire Length
    for twl_str in data:
      if (twl_str.startswith("Total wire length:")):
        twl_data_tmp = twl_str.split(": ")
        twl_data = twl_data_tmp[1].split(" um")
        print(twl_data[0])

    # Core Density    
    for area_str in data:
      if (area_str.startswith("% Core Density #2(Subtracting Physical Cells): ")):
        area_data_tmp = area_str.split(": ")
        area_data = area_data_tmp[1].split("%")
        print(area_data[0])
    #setup slack

    for setup_str in data_setup:
      if (setup_str.startswith("= Slack Time                    ")):
        setup_data_temp= setup_str.split("                    ")
        setup_data = setup_data_temp[1].split("\n")
        print(setup_data[0])
        break

    #FOM
    #weight
    alpha = 1
    beta = 1
    gamma = 1
    sigma = 1
    epsilon = 1
    #figures
    layer_num = metal1 + metal2 + metal3 + metal4 + metal5 + metal6
    setup_slack = float(setup_data[0])
    twl = float(twl_data[0])
    drc_violation = status_drc
    success_place = 1

    score = alpha*layer_num + beta*setup_slack - gamma*drc_violation - sigma*twl + epsilon*success_place
    end = time.time()
    time_elapsed = end - start
    print("score FOM" + str(score))
    f_score = open("score", "a")
    f_score.write(str(time_elapsed) + ": " + "Score = " + str(score) + '\n')
    f_score.close
    
    if(score > max_score):
      max_score = score
      max_score_position = position
      max_score_metal1 = metal1
      max_score_metal2 = metal2
      max_score_metal3 = metal3
      max_score_metal4 = metal4
      max_score_metal5 = metal5
      max_score_metal6 = metal6
      
      f_max_score = open("max_score", "a")
      f_max_score.write(str(max_score) + '\n')
      f_max_score.close
    
    # end of function
    f_data = open("data", "w")
    f_data.truncate(0)
    f_data.seek(0)
    f_data.close()
    fp_drc.close()
    fp_summ.close()
    done = subprocess.Popen([f"./clean.sh"], shell=True)
    done.wait()
    # done = subprocess.Popen([f"./clean_checkers.sh"], shell=True)
    # done.wait()
    #out of time 1hr 30mins
    # if(time_elapsed > 5000):
    if(time_elapsed > 60):
      print("time_elapsed = " + str(end-start) + "s")
      stop_time = 1
      return stop_time, max_score, max_score_position, max_score_metal1, max_score_metal2, max_score_metal3, max_score_metal4, max_score_metal5, max_score_metal6
    else:
      stop_time = 0
  return stop_time, max_score, max_score_position, max_score_metal1, max_score_metal2, max_score_metal3, max_score_metal4, max_score_metal5, max_score_metal6

#main
i = 31 #6 layers but not blocking metal1
max_score = -10000
while i > 0:
  metal1, metal2, metal3, metal4, metal5, metal6 = metal_layer(i)
  stop_time, score, score_position, score_metal1, score_metal2, score_metal3, score_metal4, score_metal5, score_metal6 = block_test(metal1, metal2, metal3, metal4, metal5, metal6)
  if(score > max_score):
    max_score = score
    max_score_position = score_position
    max_score_metal1 = score_metal1
    max_score_metal2 = score_metal2
    max_score_metal3 = score_metal3
    max_score_metal4 = score_metal4
    max_score_metal5 = score_metal5
    max_score_metal6 = score_metal6
    f_data = open("data", "w")
    f_data.write(str(max_score_position) + '\n')
    f_data.write(str(max_score_metal1) + '\n')
    f_data.write(str(max_score_metal2) + '\n')
    f_data.write(str(max_score_metal3) + '\n')
    f_data.write(str(max_score_metal4) + '\n')
    f_data.write(str(max_score_metal5) + '\n')
    f_data.write(str(max_score_metal6) + '\n')
    f_data.close()
  i-=1
  print("max score = " + str(max_score))
  if(stop_time == 1):
    break

done = subprocess.Popen([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)
done.wait()



