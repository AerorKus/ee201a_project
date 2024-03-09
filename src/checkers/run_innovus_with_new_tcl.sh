#/bin/bash

# first CD to the folder where this script is located
cd "$(dirname "$0")"
cd ../

innovus < checkers/skeleton_scripts/innovus_skeleton.tcl
