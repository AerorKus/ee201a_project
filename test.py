import sys
import subprocess
import os
import time

with open("output/s1494_postrouting_setup.tarpt") as fp_setup:
    data_setup = fp_setup.readlines()

for setup_str in data_setup:
  if (setup_str.startswith("= Slack Time                    ")):
    setup_data_temp= setup_str.split("                    ")
    setup_data = setup_data_temp[1].split("\n")
    if(setup_data[0] == '0.481'):  
      print(setup_data[0])
