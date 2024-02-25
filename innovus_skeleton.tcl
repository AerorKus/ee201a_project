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

#blockages
set position 40
set width 1.0
set layer_blk 1

set design_bbox_llx [dbGet top.fPlan.box_llx]
set design_bbox_lly [dbGet top.fPlan.box_lly]
set design_bbox_urx [dbGet top.fPlan.box_urx]
set design_bbox_ury [dbGet top.fPlan.box_ury]
set core_bbox_llx [dbGet top.fPlan.coreBox_llx]
set core_bbox_lly [dbGet top.fPlan.coreBox_lly]
set core_bbox_urx [dbGet top.fPlan.coreBox_urx]
set core_bbox_ury [dbGet top.fPlan.coreBox_ury]

set routeblk_pos [expr ($design_bbox_urx - $design_bbox_llx) * ($position/100.0)]
set placeblk_pos [expr (($core_bbox_urx - $core_bbox_llx) * ($position/100.0) + $core_bbox_llx)]

set placeblk_llx [expr ($placeblk_pos - $width/2)]
set placeblk_lly $core_bbox_lly
set placeblk_urx [expr $placeblk_pos + $width/2]
set placeblk_ury $core_bbox_ury

set routeblk_llx [expr $routeblk_pos - $width/2]
set routeblk_lly $design_bbox_lly
set routeblk_urx [expr $routeblk_pos + $width/2]
set routeblk_ury $design_bbox_ury

# createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal$layer_blk -name routeblk
createPlaceBlockage -type hard -box $routeblk_llx $placeblk_lly $routeblk_urx $placeblk_ury -name placeblk

createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal1 -name routeblk
createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal2 -name routeblk
createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 -name routeblk
createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal4 -name routeblk

# switch layer_blk {
#    1 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal1 -name routeblk
#    }
#    2 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal2 -name routeblk
#    }
#    3 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 -name routeblk
#    }
#    4 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal4 -name routeblk
#    }
#    5 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal1 metal2 -name routeblk
#    }
#    6 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal1 metal3 -name routeblk
#    }
#    7 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal1 metal4 -name routeblk
#    }
#    8 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal2 metal3 -name routeblk
#    }
#    9 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal2 metal4 -name routeblk
#    }
#    10 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 metal4 -name routeblk
#    }
#    10 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 metal4 -name routeblk
#    }
#    10 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 metal4 -name routeblk
#    }
#    10 {
#         createRouteBlk -box $routeblk_llx $routeblk_lly $routeblk_urx $routeblk_ury -layer metal3 metal4 -name routeblk
#    }
# }

# Define global power nets 
globalNetConnect VDD -type pgpin -pin VDD -inst * -module {}
globalNetConnect VSS -type pgpin -pin VSS -inst * -module {}

# Create power structures. DON'T CHANGE addRing statement.
addRing -layer {top metal1 bottom metal1 left metal2 right metal2} -spacing {top 1 bottom 1 left 1 right 1} -width {top 1 bottom 1 left 1 right 1} -center 1 -nets { VDD VSS }

# Place standard cells - timing-driven by default
# Enable placement of IO pins as well
setPlaceMode -place_global_place_io_pins true -reorderScan false
placeDesign
#place_opt_design

# Legalize placement if necessary 
refinePlace

# Save Verilog netlist post-placement
saveNetlist -excludeLeafCell ${OUTPUTDIR}/${DNAME}_placed.v

# Optimize for setup time before clock tree synthesis (CTS)
optDesign -preCTS

# Special Route power nets
sroute -connect { corePin } -corePinTarget { firstAfterRowEnd } -nets { VDD VSS }

# Perform trial route and get initial timing results
trialroute

# Build static timing model for the design
buildTimingGraph

# Run clock tree synthesis (CTS)
set_ccopt_property buffer_cells {BUF_X1 BUF_X2} 
set_ccopt_property inverter_cells {INV_X1 INV_X2 INV_X4 INV_X8 INV_X16}
create_ccopt_clock_tree_spec
ccopt_design -cts

# Refine placement again
refinePlace 

# More trial routing post-CTS to get better estimates
setTrialRouteMode -highEffort true
trialRoute

# Extract RC delay estimates
setExtractRCMode -layerIndependent 1
extractRC

# Report clock tree synthesis results
report_ccopt_clock_trees -file ${OUTPUTDIR}/postcts.ctsrpt
report_ccopt_skew_groups -local_skew -file ${OUTPUTDIR}/postcts_localskew.ctsrpt

# Run post-CTS timing analysis
setAnalysisMode -checkType hold -asyncChecks async -skew true
buildTimingGraph
report_timing -nworst 10 -net > ${OUTPUTDIR}/${DNAME}_postcts_hold.tarpt

# Optimize for hold time after CTS
optDesign -postCTS -hold 

# Perform post-CTS RC extraction
setExtractRCMode -engine preRoute -assumeMetFill
extractRC

# Run timing analysis again
buildTimingGraph
report_timing -nworst 10 -net > ${OUTPUTDIR}/${DNAME}_prerouting.tarpt

# Connect all new cells to VDD/GND
globalNetConnect VDD -type tiehi
globalNetConnect VDD -type pgpin -pin VDD -override

globalNetConnect VSS -type tielo
globalNetConnect VSS -type pgpin -pin VSS -override

# Run global and detailed routing
globalDetailRoute

# Optimize post routing
optDesign -hold -postRoute

# Extract RC delays
setExtractRCMode -engine postRoute
extractRC

# Report timing
buildTimingGraph
report_timing -nworst 10 -net > ${OUTPUTDIR}/${DNAME}_postrouting_hold.tarpt

# Report setup time
setAnalysisMode -checkType setup -asyncChecks async -skew true
buildTimingGraph
report_timing -nworst 10 -net > ${OUTPUTDIR}/${DNAME}_postrouting_setup.tarpt

# Add filler cells
addFiller -cell FILLCELL_X1 FILLCELL_X2 FILLCELL_X4 FILLCELL_X8 FILLCELL_X16 FILLCELL_X32

# Check for design-rule violations
verifyGeometry -allowRoutingBlkgPinOverlap -allowRoutingCellBlkgOverlap -error 20 -warning 5 -report ${OUTPUTDIR}/${DNAME}.drc.rpt

# Write the final results
streamOut ${OUTPUTDIR}/${DNAME}.gds -libName DesignLib -structureName $DNAME -merge { ./NangateOpenCellLibrary.gds } -stripes 1 -units 10000 -mode ALL

defOut -floorplan -netlist -routing ${OUTPUTDIR}/${DNAME}_postrouting.def
rcOut -spef ${OUTPUTDIR}/${DNAME}_postrouting.spef

saveNetlist -excludeLeafCell ${OUTPUTDIR}/${DNAME}_postrouting.v
summaryReport -noHtml -outfile ${OUTPUTDIR}/summary.rpt
reportGateCount -level 10 -outfile ${OUTPUTDIR}/gate_count.rpt
checkDesign -io -netlist -physicalLibrary -powerGround -tieHilo -timingLibrary -floorplan -place -noHtml -outfile ${OUTPUTDIR}/design.rpt

puts "*************************************************************"
puts "* Innovus script finished"
puts "*"
puts "* Results:"
puts "* --------"
puts "* Layout:  ${OUTPUTDIR}/${DNAME}.gds"
puts "* Netlist: ${OUTPUTDIR}/${DNAME}_postrouting.v"
puts "* Timing:  ${OUTPUTDIR}/${DNAME}_postrouting_setup.tarpt"
puts "* DRC:     ${OUTPUTDIR}/${DNAME}.drc.rpt"
puts "*"
puts "* Type 'exit' to quit"
puts "*"
puts "*************************************************************"

