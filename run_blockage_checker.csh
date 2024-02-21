#/bin/csh

# this runs the strip checker on your files
# this ensures your blockages have been honored by innovus

# correct usage:
# from project root:
# ./run_strip_checker.csh $LEF_FILE $DEF_FILE $VERILOG_FILE $BLOCKAGE_DEFINITION_YAML
# the file paths need to be ABSOLUTE PATHS, not RELATIVE paths.
# So, /w/class.1/ee/ee201o/ee201ot2/2024_labs/project/NangateOpenCellLibrary.lef, not ./NangateOpenCellLibrary.lef!
# this is extremely important!
# use the latest files produced by Innovus, so your initial lef, the generated def, the *LATEST* post-routing verilog, and the blockage definition yaml file!

python3 ./checkers/strip_checker.py $argv
