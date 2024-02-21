# ####################################################################

#  Created by Encounter(R) RTL Compiler v10.10-s209_1 on Wed May 16 20:02:57 -0700 2012

# ####################################################################

set sdc_version 1.7

set_units -capacitance 1000.0fF
set_units -time 1000.0ps

# Set the current design
current_design s1494_bench

create_clock -name "blif_clk_net" -add -period 1.5 -waveform {0.0 0.75} [get_ports blif_clk_net]
set_clock_transition 0.1 [get_clocks blif_clk_net]
set_clock_gating_check -setup 0.0 
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v0]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v1]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v2]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v3]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v4]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v5]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v6]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports CLR]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports blif_reset_net]
set_input_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports blif_clk_net]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_6]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_7]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_8]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_9]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_10]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_11]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_12]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_13]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_14]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_15]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_16]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_17]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_18]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_19]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_20]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_21]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_22]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_23]
set_output_delay -clock [get_clocks blif_clk_net] -add_delay 0.0 [get_ports v13_D_24]
set_wire_load_mode "enclosed"
set_dont_use [get_lib_cells NangateOpenCellLibrary/ANTENNA_X1]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X1]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X16]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X2]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X32]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X4]
set_dont_use [get_lib_cells NangateOpenCellLibrary/FILLCELL_X8]
set_dont_use [get_lib_cells NangateOpenCellLibrary/LOGIC0_X1]
set_dont_use [get_lib_cells NangateOpenCellLibrary/LOGIC1_X1]
