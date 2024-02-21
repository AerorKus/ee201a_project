
# # accept 3 arguments: lef, def, verilog
import sys
import subprocess
import os
import time

skeleton_path = "./checkers/skeleton_scripts/innovus_skeleton.pre"
new_fpath = "./checkers/skeleton_scripts/innovus_skeleton.tcl"

# get first 3 arguments
lef_fpath = ""
def_fpath = ""
verilog_fpath = ""
if len(sys.argv) > 3:
    lef_fpath = sys.argv[1]
    def_fpath = sys.argv[2]
    verilog_fpath = sys.argv[3]

# check if environmental variable PRJ_SRC is set. If not, quit
if not os.environ.get('PRJ_SRC'):
    print("Error: Please source the project setup file.")
    exit(1)


# if arguments not provided, print error
if not lef_fpath or not def_fpath or not verilog_fpath:
    print("Error: not enough arguments provided. We need 3: lef,def,verilog")
    exit(1)

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
    lines = replace_line(lines, 12, f"set lef {lef_fpath}\n")
    lines = replace_line(lines, 15, f"set def {def_fpath}\n")
    with open(new_fpath, 'w') as file:
        file.writelines(lines)

# first rm rf checker_output
subprocess.run(["rm -rf ./checker_output"],shell=True)

# if checker_output doesnt exist, make it
if not os.path.exists("./checker_output"):
    os.makedirs("./checker_output")



# now in subproccess, run "run_innovus_with_new_tcl.sh" with NO arguments
# needs to be in csh (not wholly defined in python) in order to be able to cd inside the script
print("Innovus setup complete with:")
print(f"    LEF: {lef_fpath}")
print(f"    DEF: {def_fpath}")
print(f"    Verilog: {verilog_fpath}")
time.sleep(1)
print("Running Innovus to extract performance information...")

subprocess.run(["bash ./checkers/run_innovus_with_new_tcl.sh > /dev/null 2>&1"], shell=True)

# now parse results
# check that checker_output exists
if not os.path.exists("./checker_output"):
    print("Error: checker_output directory not found. Innovus might not have been run. Try sourcing the setup file manually.")
    exit(1)


print("Innovus run complete. Parsing results... (you can also manually check the log file in project root.)")
time.sleep(1)
# inside checker_output we want to parse:
    # design.drc.rpt for DRC errors
    # design_postrouting_setup.tarpt to check for setup violations
    # design_postrouting_hold.tarpt to check for hold violations
    # summary.rpt for core area

# DRC errors
print("Checking DRC errors...")
with open("./checker_output/design.drc.rpt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "  Total Violations : " in line:
            print(line[1:], end="")
            break
        elif "No DRC violations were found" in line:
            print(" No DRC violations found")
            break
 
time.sleep(1)
print("Checking setup/hold timing violations...")
# setup/hold timing violations
with open("./checker_output/design_postrouting_setup.tarpt", 'r') as file:
    lines = file.readlines()
    # find first instance of "= Slack Time                    "
    # actual line "= Slack Time                    0.534"
    slack = ""
    float_slack = -1
    for line in lines:
        if "= Slack Time                    " in line:
            slack = line.split(" ")[-1]
            float_slack = float(slack)
            if float_slack < 0:
                print(" Setup timing violation found. Setup Slack:",float_slack)
            else:
                print(" No setup timing violations found. Setup Slack:",float_slack)
            break
    if float_slack == -1:
        print(" Error: no setup slack time found")

with open("./checker_output/design_postrouting_hold.tarpt", 'r') as file:
    lines = file.readlines()
    # find first instance of "= Slack Time                    "
    # actual line "= Slack Time                    0.534"
    slack = ""
    float_slack = -1
    for line in lines:
        if "  Slack Time                    " in line:
            slack = line.split(" ")[-1]
            float_slack = float(slack)
            if float_slack < 0:
                print(" Hold timing violation found. Hold Slack:",float_slack)
            else:
                print(" No hold timing violations found. Hold Slack:",float_slack)
            break
    if float_slack == -1:
        print(" Error: no hold slack time found")

# core area
time.sleep(1)
print("Checking core area...")
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
                print(" Error: no core area found")
            else:
                print(f" Core area: {area} um^2")
            time.sleep(0.5)
        if "Total area of Standard cells: " in line:
            area = line.split()[-2].strip()
            float_area = float(area)
            if float_area == -1:
                print(" Error: no standard cell area found")
            else:
                print(f" Standard cell area: {area} um^2")
        if "Total metal1 wire length:" in line:
            m1 = line.split()[-2].strip()
            print(f" M1 wire length: {m1} um")
        if "Total metal2 wire length:" in line:
            m2 = line.split()[-2].strip()
            print(f" M2 wire length: {m2} um")
        if "Total metal3 wire length:" in line:
            m3 = line.split()[-2].strip()
            print(f" M3 wire length: {m3} um")
        if "Total metal4 wire length:" in line:
            m4 = line.split()[-2].strip()
            print(f" M4 wire length: {m4} um")
        if "Total wire length:" in line:
            total = line.split()[-2].strip()
            print(f" Total wire length: {total} um")
            break
        
print("Done checking")
time.sleep(0.5)
exit(0)