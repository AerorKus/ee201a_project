#/bin/csh

# this runs the combined checker on your output files
# this will report DRC, hold/setup slack, core/cell area, and wirelength
# use this to ensure your design has not failed p&r and extract performance metrics for plots
# if you provide a boundary definitions yaml file, it will also run the placemt and routing blockage checker

# correct usage:
# from project root:
# ./run_combined_checker.csh $VERILOG_FILE [OPTIONAL]$BOUNDARY_DEFINITION_FILE 
# Use absolute paths for files. Relative paths from project root *should* work, but are not guaranteed to work.
# So, /w/class.1/ee/ee201o/ee201ot2/2024_labs/project/NangateOpenCellLibrary.lef, not ./NangateOpenCellLibrary.lef.
# use the latest files produced by Innovus, so your post routing verilog and OPTIONALLY, your boundary definition file
# if the boundary definition yaml is provided, a routing and placement blockage violation check will also be performed. Else, only performance information will be returned.

python3 ./checkers/combined_checker.py $argv

# The combined checker will now also by default write all it's prints out in a file called combined_checker_output.txt
# this is for your convenience so you can use it for your scripting needs.
