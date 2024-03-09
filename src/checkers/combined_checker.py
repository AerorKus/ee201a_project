import sys
import subprocess
import os
import time

log_output_file = "combined_checker_output.txt"

# delete log output file if it exists
if os.path.exists(log_output_file):
    os.remove(log_output_file)

# then make a new empty one
with open(log_output_file, 'w') as file:
    file.write("")

# I want to overload print() so that it my_prints a message and also writes to the output file
def my_print(*args, **kwargs):
    print(*args, **kwargs)
    with open(log_output_file, 'a') as file:
        print(*args, **kwargs, file=file)

skeleton_path = "./checkers/skeleton_scripts/innovus_skeleton.pre"
new_fpath = "./checkers/skeleton_scripts/innovus_skeleton.tcl"

# get first 2 arguments
verilog_fpath = ""
blockage_fpath = ""
if len(sys.argv) > 2:
    verilog_fpath = sys.argv[1]
    blockage_fpath = sys.argv[2]
elif len(sys.argv) > 1:
    verilog_fpath = sys.argv[1]

# check if environmental variable PRJ_SRC is set. If not, quit
if not os.environ.get('PRJ_SRC'):
    my_print("Error: Please source the project setup file.")
    exit(1)

# if arguments not provided, my_print error
if not verilog_fpath:
    my_print("Error: not enough arguments provided. We need at least the verilog path.")
    exit(1)

blockage_check = False
if blockage_fpath != "":
    my_print("Blockage file provided, will also run strip checker.")
    blockage_check = True

# first, parse blockage file (yaml) to get blockage coordinates
x1_route = 0
y1_route = 0
x2_route = 0
y2_route = 0

x1_place = 0
y1_place = 0
x2_place = 0
y2_place = 0

blkg_type = ""
if blockage_check:
    with open(blockage_fpath, 'r') as file:
        for line in file:
            if line.startswith("#"):
                continue
            if "place_blockage" in line:
                blkg_type = "place"
                continue
            if "route_blockage" in line:
                blkg_type = "route"
                continue        
            if "x1" in line:
                if blkg_type == "place":
                    x1_place = float(line.split(":")[1][:-1].strip())
                if blkg_type == "route":
                    x1_route = float(line.split(":")[1][:-1].strip())
            if "y1" in line:
                if blkg_type == "place":
                    y1_place = float(line.split(":")[1][:-1].strip())
                if blkg_type == "route":
                    y1_route = float(line.split(":")[1][:-1].strip())
            if "x2" in line:
                if blkg_type == "place":
                    x2_place = float(line.split(":")[1][:-1].strip())
                if blkg_type == "route":
                    x2_route = float(line.split(":")[1][:-1].strip())
            if "y2" in line:
                if blkg_type == "place":
                    y2_place = float(line.split(":")[1][:-1])
                if blkg_type == "route":
                    y2_route = float(line.split(":")[1][:-1])


# determine top module from verilog file
top_module = ""
with open(verilog_fpath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "module" in line:
            top_module = line.split(" ")[1]
            if "(" in top_module:
                top_module = top_module.split("(")[0]
            break

def replace_line(lines,line_no,new_line):
    lines[line_no] = new_line
    return lines

with open(skeleton_path, 'r') as file:
    lines = file.readlines()
    lines = replace_line(lines, 9, f"set netlist {verilog_fpath}\n")
    lines = replace_line(lines, 10, f"set top_cell {top_module}\n")
    lines = replace_line(lines, 11, f"set sdc {top_module}.sdc\n")
    lines = replace_line(lines, 16, f"set x1_r {x1_route}\n")
    lines = replace_line(lines, 17, f"set y1_r {y1_route}\n")
    lines = replace_line(lines, 18, f"set x2_r {x2_route}\n")
    lines = replace_line(lines, 19, f"set y2_r {y2_route}\n")
    lines = replace_line(lines, 20, f"set x1_p {x1_place}\n")
    lines = replace_line(lines, 21, f"set y1_p {y1_place}\n")
    lines = replace_line(lines, 22, f"set x2_p {x2_place}\n")
    lines = replace_line(lines, 23, f"set y2_p {y2_place}\n")

    with open(new_fpath, 'w') as file:
        file.writelines(lines)

# first rm rf checker_output
subprocess.run(["rm -rf ./checker_output"],shell=True)

# if checker_output doesnt exist, make it
if not os.path.exists("./checker_output"):
    os.makedirs("./checker_output")

# now in subproccess, run "run_innovus_with_new_tcl.sh" with NO arguments
# needs to be in csh (not wholly defined in python) in order to be able to cd inside the script
my_print("Innovus setup complete with:")
my_print(f"    Verilog: {verilog_fpath}")
if blockage_check:
    my_print(f"    Blockage file: {blockage_fpath}")
    my_print("Place blockage setup:")
    my_print("    x1:",x1_place,"y1:",y1_place,"x2:",x2_place,"y2:",y2_place)
    my_print("Route blockage setup:")
    my_print("    x1:",x1_route,"y1:",y1_route,"x2:",x2_route,"y2:",y2_route)

time.sleep(1)
if blockage_check:
    my_print("Running Innovus to extract performance and strip information...")
else:
    my_print("Running Innovus to extract performance information...")

subprocess.run(["bash ./checkers/run_innovus_with_new_tcl.sh > /dev/null 2>&1"], shell=True)

# now parse results
# check that checker_output exists
if not os.path.exists("./checker_output"):
    my_print("Error: checker_output directory not found. Innovus might not have been run. Try sourcing the setup file manually.")
    exit(1)

my_print("Innovus run complete. Parsing results... (you can also manually check the log file in project root.)")
time.sleep(1)
# DRC errors
my_print("Checking DRC errors...")
with open("./checker_output/design.drc.rpt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "  Total Violations : " in line:
            my_print(line[1:], end="")
            break
        elif "No DRC violations were found" in line:
            my_print(" No DRC violations found")
            break
 
time.sleep(1)
my_print("Checking setup/hold timing violations...")
# setup/hold timing violations
with open("./checker_output/design_postrouting_setup.tarpt", 'r') as file:
    lines = file.readlines()
    # find first instance of "= Slack Time                    "
    # actual line "= Slack Time                    0.534"
    slack = ""
    float_slack = -1
    for line in lines:
        if "= Slack Time                   " in line:
            slack = line.split(" ")[-1]
            float_slack = float(slack)
            if float_slack < 0:
                my_print(" Setup timing violation found. Setup Slack:",float_slack)
            else:
                my_print(" No setup timing violations found. Setup Slack:",float_slack)
            break
    if float_slack == -1:
        my_print(" Error: no setup slack time found")

with open("./checker_output/design_postrouting_hold.tarpt", 'r') as file:
    lines = file.readlines()
    # find first instance of "= Slack Time                    "
    # actual line "= Slack Time                    0.534"
    slack = ""
    float_slack = -1
    for line in lines:
        if "  Slack Time                   " in line:
            slack = line.split(" ")[-1]
            float_slack = float(slack)
            if float_slack < 0:
                my_print(" Hold timing violation found. Hold Slack:",float_slack)
            else:
                my_print(" No hold timing violations found. Hold Slack:",float_slack)
            break
    if float_slack == -1:
        my_print(" Error: no hold slack time found")

# core area
time.sleep(1)
my_print("Checking core area...")
with open("./checker_output/summary.rpt", 'r') as file:
    lines = file.readlines()
    # example line:
    # Total area of Core: 349.258 um^2  
    area = ""
    float_area = -1
    for line in lines:
        if "Total area of Core:" in line:
            area = line.split()[-2].strip()
            float_area = float(area)
            if float_area == -1:
                my_print(" Error: no core area found")
            else:
                my_print(f" Core area: {area} um^2")
            time.sleep(0.5)
        if "Total area of Standard cells: " in line:
            area = line.split()[-2].strip()
            float_area = float(area)
            if float_area == -1:
                my_print(" Error: no standard cell area found")
            else:
                my_print(f" Standard cell area: {area} um^2")
        if "Total metal1 wire length:" in line:
            m1 = line.split()[-2].strip()
            my_print(f" M1 wire length: {m1} um")
        if "Total metal2 wire length:" in line:
            m2 = line.split()[-2].strip()
            my_print(f" M2 wire length: {m2} um")
        if "Total metal3 wire length:" in line:
            m3 = line.split()[-2].strip()
            my_print(f" M3 wire length: {m3} um")
        if "Total metal4 wire length:" in line:
            m4 = line.split()[-2].strip()
            my_print(f" M4 wire length: {m4} um")
        if "Total metal5 wire length:" in line:
            m5 = line.split()[-2].strip()
            my_print(f" M5 wire length: {m5} um")
        if "Total metal6 wire length:" in line:
            m6 = line.split()[-2].strip()
            my_print(f" M6 wire length: {m6} um")
        if "Total wire length:" in line:
            total = line.split()[-2].strip()
            my_print(f" Total wire length: {total} um")
            break
        
time.sleep(1)
# example blockage out file:
    #layer:metal3
    # layer:metal2
    # layer:metal1
    # layer:metal1
    # layer:metal3
    # layer:metal4
    # layer:metal4
    # layer:metal4
    # layer:metal3
    # layer:metal2
    # layer:metal3
    # layer:metal4
if blockage_check:
    my_print("Checking place & route violations...")
    with open("./checker_output/blockage_return.txt",'r') as f:
        # we read all the lines. If the word "FILLER" exists in the line, skip it. Otherwise, increment and my_print line
        lines = f.readlines()
        count = 0
        for line in lines:
            if "FILLER" in line:
                continue
            count += 1
            if count > 5:
                continue
            my_print(" PLACE VIOLATION:",line.strip())
        if count > 5:
            my_print(f" Skipping printing remaining {count-5} placement violations...")
        if count == 0:
            my_print(" No place violations found.")
    time.sleep(1)
    layer_arr = [0] * 8 # up to 8 layers
    with open("./checker_output/layer_return.txt",'r') as f:
        # we read all the lines, and increase the layer_arr index by 1 according to layer number
        lines = f.readlines()
        for line in lines:
            layer = int(line.split(":")[1].strip()[-1])
            layer_arr[layer-1] += 1
    my_print("Route violations:")
    for i in range(len(layer_arr)):
        if layer_arr[i] > 0:
            my_print(f" Metal Layer {i+1} has {layer_arr[i]} violations")
    
    # if every element in layer_arr is 0, then no route violations
    if all(x == 0 for x in layer_arr):
        my_print(" No route violations found. This indicates that absolutely NO nets are crossing your blockage area on any layer.")
        my_print(" This should not happen - we only expect blockage up to a point. Something is wrong.")
    # check if any layers have 0 violations, and my_print the first layer that has 0 violations
    # we want the largest layer from 0 to 8 with no violations to be my_printed
    # for i in range(len(layer_arr)):
    #     if layer_arr[i] == 0:
    #         continue
    #     else:
    #         my_print(" This means your stitching (and route blockage) has worked up until layer:", i)
    #         break
    my_print("Done checking route violations")
my_print("Done checking")

time.sleep(0.5)
exit(0)
