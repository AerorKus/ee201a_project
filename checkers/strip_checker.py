# accept 4 arguments: lef, def, verilog, blockage file
import sys
import subprocess
import os
import time


oa_checker_path = "./checkers/oa_bound_checker"
os.chdir(oa_checker_path)
blockage_parsed_fpath = "./blockage_parsed.txt"

# get first 4 arguments
lef_fpath = ""
def_fpath = ""
verilog_fpath = ""
blockage_fpath = ""
if len(sys.argv) > 4:
    lef_fpath = sys.argv[1]
    def_fpath = sys.argv[2]
    verilog_fpath = sys.argv[3]
    blockage_fpath = sys.argv[4]

# if arguments not provided, print error
if not lef_fpath or not def_fpath or not verilog_fpath or not blockage_fpath:
    print("Error: not enough arguments provided. We need 4: lef,def,verilog,blockage file")
    exit(1)

# first, parse blockage file (yaml) to get blockage coordinates
x1 = 0
y1 = 0
x2 = 0
y2 = 0
with open(blockage_fpath, 'r') as file:
    for line in file:
        if line.startswith("#"):
            continue
        if "x1" in line:
            x1 = float(line.split(":")[1][:-2].strip())
        if "x2" in line:
            x2 = float(line.split(":")[1][:-2].strip())
        if "y1" in line:
            y1 = float(line.split(":")[1][:-2].strip())
        if "y2" in line:
            y2 = float(line.split(":")[1][:-1])

# in oa_checker_path, generate blockage_parsed.txt
# it's just a txt file with x1 y1 x2 y2 in it and nothing else
            
# first run oa_checker_path/clean.sh
subprocess.run(["./clean.sh > /dev/null 2>&1"], shell=True)
# then write to it
with open(blockage_parsed_fpath, 'w') as file:
    file.write(f"{x1} {y1} {x2} {y2}")

print("Now checking for blockage violations...")

# then run checker_oa_database.sh (this also runs lab)
subprocess.run([f"./checker_oa_database_and_run.sh {lef_fpath} {def_fpath} {verilog_fpath}"], shell=True)

print("Done.")