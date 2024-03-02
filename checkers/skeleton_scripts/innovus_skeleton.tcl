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

set x1_r 0.0
set y1_r 0.0
set x2_r 50.0
set y2_r 5.0
set x1_p 0.0
set y1_p 0.0
set x2_p 25.0
set y2_p 2.0

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

restoreDesign [file dirname [file normalize [info script]]]/design_file.dat $top_cell

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

set qb [dbQuery -area $x1_p $y1_p $x2_p $y2_p -objType {inst}]

# foreach
set output_file "checker_output/blockage_return.txt"
set file_handle [open $output_file "w"]

set count 0
foreach instance $qb {
    set layer [get_db $instance .name]
    puts $file_handle $layer
}

close $file_handle


set qq [dbQuery -area $x1_r $y1_r $x2_r $y2_r -objType {wire}]

# foreach
set output_file "checker_output/layer_return.txt"
set file_handle [open $output_file "w"]

foreach wire $qq {
    set layer [get_db $wire .layer]
    puts $file_handle $layer
}

close $file_handle
