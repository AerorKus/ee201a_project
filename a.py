import sys
import subprocess
import os
import time

if os.path.exists("data"):
  os.remove("data")
  f_data = open("data", "x")
else:
  f_data = open("data", "x")
f_data = open("data", "w")

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

position = 50
metal1 = 0
metal2 = 1
metal3 = 1
metal4 = 0

f_data.write(str(position) + '\n')
f_data.write(str(metal1) + '\n')
f_data.write(str(metal2) + '\n')
f_data.write(str(metal3) + '\n')
f_data.write(str(metal4) + '\n')
f_data.close()

subprocess.run([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)



with open('output/s1494.drc.rpt') as fp_drc:
  if 'No DRC violations were found' in fp_drc.read():
          print("No DRC Violations")
          status_drc = 1
  
with open("output/summary.rpt") as fp_summ:
    data = fp_summ.readlines()

#Total Wire Length
for twl_str in data:
  if (twl_str.startswith("Total wire length:")):
    twl_data_tmp = twl_str.split(": ")
    twl_data = twl_data_tmp[1].split(" um")
    if(twl_data[0] == '3583.6600'):  
      print(twl_data[0])

# Core Density    
for area_str in data:
  if (area_str.startswith("% Core Density #2(Subtracting Physical Cells): ")):
    area_data_tmp = area_str.split(": ")
    area_data = area_data_tmp[1].split("%")
    if(area_data[0] == '87.687'):  
      print(area_data[0])


f_data = open("data", "w")
f_data.truncate(0)
f_data.seek(0)
f_data.close()

fp_drc.close()
fp_summ.close()
os.remove("data")

