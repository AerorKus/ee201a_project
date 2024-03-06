import sys
import subprocess
import os
import time


start = time.time()
print("hello")
end = time.time()
print(end - start)

# with open("output/s1494_postrouting_setup.tarpt") as fp_setup:
#     data_setup = fp_setup.readlines()

# for setup_str in data_setup:
#   if (setup_str.startswith("= Slack Time                    ")):
#     setup_data_temp= setup_str.split("                    ")
#     setup_data = setup_data_temp[1].split("\n")
#     if(setup_data[0] == '0.481'):  
#       print(setup_data[0])

# def metal_layer(select):
#     if(select == 0):
#      return 0, 0, 0, 1
#     if(select == 1):
#       return 1, 0, 0, 0

# metal1, metal2, metal3, metal4 = metal_layer(1)
# print(metal1)
# print(metal2)
# print(metal3)
# print(metal4)

# min_score = 1
# print("min score = " + str(min_score))