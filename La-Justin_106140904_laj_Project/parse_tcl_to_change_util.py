# example file on how to change the UTIL value in the tcl file
# you can use this code in your script if you want to.

skeleton_path = "innovus_skeleton_fpu.tcl"

NEW_UTIL = 0.88

def replace_line(lines,line_no,new_line):
    lines[line_no] = new_line
    return lines

with open(skeleton_path, 'r') as file:
    lines = file.readlines()
    lines = replace_line(lines, 61, f"set UTIL {NEW_UTIL}\n")

with open(skeleton_path, 'w') as file:
    file.writelines(lines)