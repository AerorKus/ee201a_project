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

# done = subprocess.Popen([f"innovus -nowin < innovus_skeleton.tcl"], shell=True)
# done.wait()
# print("done")


import yaml
# data_a = 1
# data = dict(
#     A = data_a,
#     B = dict(
#         C = 'c',
#         D = 'd',
#         E = 'e',
#     )
# )

# with open('data.yaml', 'w') as outfile:
#     yaml.dump(data, outfile, default_flow_style=False)

# with open("routeblk") as fp_setup:
#     data = fp_setup.readlines()
#     setup_data = data[0].split("\n")
#     print(setup_data[0])
#     routeblk_llx = setup_data[0]
#     setup_data = data[1].split("\n")
#     print(setup_data[0])
#     routeblk_lly = setup_data[0]
#     setup_data = data[2].split("\n")
#     print(setup_data[0])
#     routeblk_urx = setup_data[0]
#     setup_data = data[3].split("\n")
#     print(setup_data[0])
#     routeblk_ury = setup_data[0]


# with open("placeblk") as fp_setup:
#     data = fp_setup.readlines()
#     setup_data = data[0].split("\n")
#     print(setup_data[0])
#     placeblk_llx = setup_data[0]
#     setup_data = data[1].split("\n")
#     print(setup_data[0])
#     placeblk_lly = setup_data[0]
#     setup_data = data[2].split("\n")
#     print(setup_data[0])
#     placeblk_urx = setup_data[0]
#     setup_data = data[3].split("\n")
#     print(setup_data[0])
#     placeblk_ury = setup_data[0]


# pnr_blockage = { "place_blockage" : {"x1" : placeblk_llx , "x2" : placeblk_urx, "y1" : placeblk_lly, "y2" : placeblk_ury}, \
# "route_blockage" : {"x1" : routeblk_llx , "x2" : routeblk_urx, "y1" : routeblk_lly, "y2" : routeblk_ury}}
# with open('data.yaml', 'w') as outfile:
#     yaml.dump(pnr_blockage, outfile, sort_keys=False)


# set fp_routeblk [open "routeblk" w+]
# puts $fp_routeblk "$routeblk_llx\n$routeblk_lly\n$routeblk_urx\n$routeblk_ury"
# close $fp_routeblk

# print(open('data.yaml').read())
# path = "best_results"
# try: 
#     os.makedirs(path, exist_ok = True) 
#     print("Directory '%s' created successfully" % path) 
# except OSError as error: 
#     print("Directory '%s' can not be created" % path) 
#     os.rmdir(path)
#     os.makedirs(path, exist_ok = True) 
#     print("Directory '%s' created successfully" % path) 

# import shutil

# path = "best_results"
# shutil.rmtree(path)
# os.makedirs(path, exist_ok = True) 

# source_dir = r"design_file.dat"
# destination_dir = r"best_results/design_file.dat"
# shutil.copytree(source_dir, destination_dir)

# #generated def
# src_path = r"output/fpu_postrouting.def"
# dst_path = r"best_results/fpu_postrouting.def"
# shutil.copy(src_path, dst_path)

# #generated verilog
# src_path = r"output/fpu_postrouting.v"
# dst_path = r"best_results/fpu_postrouting.v"
# shutil.copy(src_path, dst_path)

# #lef
# src_path = r"NangateOpenCellLibrary.lef"
# dst_path = r"best_results/NangateOpenCellLibrary.lef"
# shutil.copy(src_path, dst_path)

# #gds
# src_path = r"NangateOpenCellLibrary.gds"
# dst_path = r"best_results/NangateOpenCellLibrary.gds"
# shutil.copy(src_path, dst_path)

# #blockage yaml
# src_path = r"blockages_definition.yaml"
# dst_path = r"best_results/blockages_definition.yaml"
# shutil.copy(src_path, dst_path)


# skeleton_path = "innovus_skeleton.tcl"

# if len(sys.argv) > 1:
#     NEW_UTIL = sys.argv[1]

# def replace_line(lines,line_no,new_line):
#     lines[line_no] = new_line
#     return lines

# with open(skeleton_path, 'r') as file:
#     lines = file.readlines()
#     lines = replace_line(lines, 50, f"set UTIL {NEW_UTIL}\n")

# with open(skeleton_path, 'w') as file:
#     file.writelines(lines)

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

block_yaml()