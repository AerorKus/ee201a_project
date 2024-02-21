#/bin/csh

# this runs the performance checker on your output files
# this will report DRC, hold/setup slack, core/cell area, and wirelength
# use this to ensure your design has not failed p&r and extract performance metrics for plots

# correct usage:
# from project root:
# ./run_perf_checker.csh $LEF_FILE $DEF_FILE $VERILOG_FILE
# So, /w/class.1/ee/ee201o/ee201ot2/2024_labs/project/NangateOpenCellLibrary.lef, not ./NangateOpenCellLibrary.lef!
# this is extremely important!
# use the latest files produced by Innovus, so your initial lef, the generated def, and the *LATEST* post-routing verilog!

python3 ./checkers/perf_checker.py $argv
