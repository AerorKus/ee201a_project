import sys
import subprocess
import os
import time

if os.path.exists("data"):
  os.remove("data")
  f = open("data", "x")
else:
  f = open("data", "x")

f = open("data", "w")

position = 50
metal1 = 0
metal2 = 1
metal3 = 1
metal4 = 0

f.write(str(position) + '\n')
f.write(str(metal1) + '\n')
f.write(str(metal2) + '\n')
f.write(str(metal3) + '\n')
f.write(str(metal4) + '\n')

subprocess.run([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)

f.truncate(0)
f.seek(0)
f.close()  
os.remove("data")
