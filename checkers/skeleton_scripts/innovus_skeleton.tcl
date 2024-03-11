# UCLA EE 201A -- VLSI Design Automation
# Winter 2021
# Lab 4 Skeleton Tcl Script
# ----------------------------------------
# Use the following command to run:
# 	$ innovus -win -init lab4_skeleton.tcl
# ----------------------------------------

# Setup design config
set netlist output/fpu_postrouting.v
set top_cell fpu
set sdc fpu.sdc
set lef NangateOpenCellLibrary.lef
set DNAME design
set OUTPUTDIR checker_output

set x1_r 67.3015
set y1_r 0.0
set x2_r 68.3015
set y2_r 149.24
set x1_p 67.3015
set y1_p 6.02
set x2_p 68.3015
set y2_p 143.22

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

create_library_set -name default_library_set -timing ./NangateOpenCellLibrary_typical_conditional_nldm.lib
create_rc_corner -name _default_rc_corner_ -T 25.0
create_delay_corner -name _default_delay_corner_ -library_set default_library_set -opcond typical  -opcond_library NangateOpenCellLibrary -rc_corner _default_rc_corner_
create_constraint_mode -name _default_constraint_mode_ -sdc_files $sdc
 
create_analysis_view -name _default_view_  -constraint_mode _default_constraint_mode_ -delay_corner _default_delay_corner_
 
init_design -setup _default_view_ -hold _default_view_
setAnalysisMode -analysisType onChipVariation -cppr both
setDesignMode -process 45

restoreDesign design_file.dat $top_cell

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
