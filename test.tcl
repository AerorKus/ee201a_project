# UCLA EE 201A -- VLSI Design Automation
# Winter 2021
# Lab 4 Skeleton Tcl Script
# ----------------------------------------
# Use the following command to run:
# 	$ innovus -win -init lab4_skeleton.tcl
# ----------------------------------------

# Setup design config
set netlist s1494_synth.v
set top_cell s1494_bench
set sdc s1494.sdc
set lef NangateOpenCellLibrary.lef
set DNAME s1494
set OUTPUTDIR output

set lefDefOutVersion 5.7

# Check if the directory exists
if {![file isdirectory $OUTPUTDIR]} {
    # If it doesn't exist, create it
    if {[catch {file mkdir $OUTPUTDIR} result]} {
        puts "Error creating directory: $OUTPUTDIR"
    } else {
        puts "Directory created: $OUTPUTDIR"
    }
} else {
    puts "Directory already exists: $OUTPUTDIR"
}


# Initialize design
suppressMessage TECHLIB-436
suppressMessage IMPVL-159
set init_verilog $netlist
set init_design_netlisttype "Verilog"
set init_design_settop 1
set init_top_cell $top_cell
set init_lef_file $lef
set init_pwr_net VDD
set init_gnd_net VSS
source ./rc.mmode.tcl
init_design -setup _default_view_ -hold _default_view_
setAnalysisMode -analysisType onChipVariation -cppr both
setDesignMode -process 45

# Report initial setup and hold time, post-synthesis but before physical design
report_timing -check_type setup -nworst  10 -net > ${OUTPUTDIR}/${DNAME}_init_setup.tarpt
report_timing -early -nworst  10 -net > ${OUTPUTDIR}/${DNAME}_init_hold.tarpt

# DON'T CHANGE: Limit number of metal/routing layers
setMaxRouteLayer 4

# Specify floorplan dimensions and placement utilization
set UTIL 0.88
floorplan -r 1.0 $UTIL 6 6 6 6



set design_bbox_llx [dbGet top.fPlan.box_llx]
set design_bbox_lly [dbGet top.fPlan.box_lly]
set design_bbox_urx [dbGet top.fPlan.box_urx]
set design_bbox_ury [dbGet top.fPlan.box_ury]
set core_bbox_llx [dbGet top.fPlan.coreBox_llx]
set core_bbox_lly [dbGet top.fPlan.coreBox_lly]
set core_bbox_urx [dbGet top.fPlan.coreBox_urx]
set core_bbox_ury [dbGet top.fPlan.coreBox_ury]

put $design_bbox_llx
put $design_bbox_lly
put $design_bbox_urx
put $design_bbox_ury
put $core_bbox_llx
put $core_bbox_lly
put $core_bbox_urx
put $core_bbox_ury

set position 50
set width 1.0
set routeblk_pos [expr ($design_bbox_urx - $design_bbox_llx) * ($position/100.0)]
set placeblk_pos [expr ($core_bbox_urx - $core_bbox_llx) * ($position/100.0)]
put $routeblk_pos
put $placeblk_pos

set placeblk_llx [expr $placeblk_pos - $width/2]
set placeblk_lly $core_bbox_lly
set placeblk_urx [expr $placeblk_pos + $width/2]
set placeblk_ury $core_bbox_ury

put $placeblk_llx
put $placeblk_lly
put $placeblk_urx
put $placeblk_ury

set routeblk_llx [expr $routeblk_pos - $width/2]
set routeblk_lly $design_bbox_lly
set routeblk_urx [expr $routeblk_pos + $width/2]
set routeblk_ury $design_bbox_ury

put $routeblk_llx
put $routeblk_lly
put $routeblk_urx
put $routeblk_ury

createRouteBlk -box {15.555 0.0 16.555 31.64} -layer metal3 -name routeblk
createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 -name routeblk
# createPlaceBlockage -type hard -box {{$placeblk_llx} {$placeblk_lly} {$placeblk_urx} {$placeblk_ury}} -name placeblk

