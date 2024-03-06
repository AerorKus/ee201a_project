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

def metal_layer(select):
    #organized to run more aggressive route blk first
    if(select == 7):
      return 0, 0, 0, 0
    if(select == 4):
      return 0, 0, 0, 1
    if(select == 5):
      return 0, 0, 1, 0
    if(select == 1):
      return 0, 0, 1, 1
    if(select == 6):
      return 0, 1, 0, 0
    if(select == 2):
      return 0, 1, 0, 1
    if(select == 3):
      return 0, 1, 1, 0
    if(select == 0):
      return 0, 1, 1, 1
    # if(select == 8):
    #   return 1, 0, 0, 0
    # if(select == 9):
    #   return 1, 0, 0, 1
    # if(select == 10):
    #   return 1, 0, 1, 0
    # if(select == 11):
    #   return 1, 0, 1, 1
    # if(select == 12):
    #   return 1, 1, 0, 0
    # if(select == 13):
    #   return 1, 1, 0, 1
    # if(select == 14):
    #   return 1, 1, 1, 0
    # if(select == 15):
    #   return 1, 1, 1, 1
 
def block_test(metal1, metal2, metal3, metal4):
  position = 40
  max_score = 0
  while position <= 60:
    f_data = open("data", "w")
    f_data.write(str(position) + '\n')
    f_data.write(str(metal1) + '\n')
    f_data.write(str(metal2) + '\n')
    f_data.write(str(metal3) + '\n')
    f_data.write(str(metal4) + '\n')
    f_data.close()
    position += 1 #detail of blk
    subprocess.run([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)

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

    #FOM
    #weight
    alpha = 1
    beta = 1
    gamma = 1
    sigma = 1
    epsilon = 1
    #figures
    layer_num = metal1 + metal2 + metal3 + metal4
    setup_slack = float(setup_data[0])
    twl = float(twl_data[0])
    drc_violation = status_drc
    success_place = 1

    score = alpha*layer_num + beta*setup_slack - gamma*drc_violation - sigma*twl + epsilon*success_place
    end = time.time()
    time_elapsed = end - start
    
    f_score = open("score", "a")
    f_score.write(str(time_elapsed) + ": " + "Score = " + str(score) + '\n')
    f_score.close
    
    if(time_elapsed > 5400):
      print("time_elapsed = " + str(end-start) + "s")
      break
    if(score > max_score):
      max_score = score
      max_score_position = position
      max_score_metal1 = metal1
      max_score_metal2 = metal2
      max_score_metal3 = metal3
      max_score_metal4 = metal4
      
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
    subprocess.run([f"./clean.sh"], shell=True)
    subprocess.run([f"./clean_checkers.sh"], shell=True)
  return max_score, max_score_position, max_score_metal1, max_score_metal2, max_score_metal3, max_score_metal4

#main
i = 0
max_score = 0
while i <= 7:
  metal1, metal2, metal3, metal4 = metal_layer(i)
  score = block_test(metal1, metal2, metal3, metal4)
  if(score > max_score):
    max_score = score
  i+=1
  print("min score = " + str(max_score))


