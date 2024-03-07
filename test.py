import sys
import subprocess
import os
import time


# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)

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



# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')



# def test(num):
     
#     metal1 = num%2
#     print(metal1)
#     print("\r")
#     metal2 = num%4
#     print(metal2)
#     print("\r")
    
# def decimalToBinary(data):
#     metal1 = (int(data) & 1) >> 0
#     metal2 = (int(data) & 2) >> 1
#     metal3 = (int(data) & 4) >> 2
#     metal4 = (int(data) & 8) >> 3
#     metal5 = (int(data) & 16) >> 4
#     metal6 = (int(data) & 32) >> 5

#     print(metal1)
#     print(metal2)
#     print(metal3)
#     print(metal4)
#     print(metal5)
#     print(metal6)
     


# n = 42
# # DecimalToBinary(n)
# # print("\r")
# # test(n)
# # print(bin(n))
# print(bin(n).replace("0b", ""))
# print("\r")
# print((n & 32) >> 5)
# print("\r")
# decimalToBinary(n)

done = subprocess.Popen([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)
done.wait()
print("done")