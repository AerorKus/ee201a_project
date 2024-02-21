# UCLA EE 201A -- VLSI Design Automation
# Winter 2021
# Lab 4 Skeleton Tcl Script
# ----------------------------------------
# Use the following command to run:
# 	$ innovus -win -init lab4_skeleton.tcl
# ----------------------------------------

# Setup design config
set netlist output/s1494_postrouting.v
set top_cell s1494_bench
set sdc design.sdc
set lef NangateOpenCellLibrary.lef
set DNAME design
set OUTPUTDIR checker_output
set def output/s1494_postrouting.def

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

defIn $def

# Extract RC delays
setExtractRCMode -engine postRoute
extractRC

# Report timing
setAnalysisMode -checkType hold -asyncChecks async -skew true
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

