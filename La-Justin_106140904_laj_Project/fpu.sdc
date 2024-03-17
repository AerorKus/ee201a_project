# ####################################################################

#  Created by Genus(TM) Synthesis Solution 19.12-s121_1 on Mon Mar 04 19:30:45 PST 2024

# ####################################################################

set sdc_version 2.0

set_units -capacitance 1fF
set_units -time 1000ps

# Set the current design
current_design fpu

create_clock -name "clk_i" -period 5 -waveform {0.0 2.5} [get_ports clk_i]
set_clock_transition 0.1 [get_clocks clk_i]
set_clock_gating_check -setup 0.0 
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports clk_i]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[31]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[30]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[29]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[28]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[27]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[26]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[25]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[24]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[23]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[22]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[21]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[20]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[19]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[18]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[17]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[16]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[15]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[14]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[13]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[12]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[11]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[10]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[9]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[8]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[7]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[6]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[5]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[4]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[3]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[2]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[1]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opa_i[0]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[31]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[30]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[29]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[28]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[27]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[26]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[25]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[24]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[23]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[22]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[21]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[20]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[19]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[18]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[17]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[16]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[15]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[14]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[13]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[12]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[11]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[10]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[9]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[8]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[7]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[6]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[5]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[4]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[3]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[2]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[1]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {opb_i[0]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {fpu_op_i[2]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {fpu_op_i[1]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {fpu_op_i[0]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {rmode_i[1]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {rmode_i[0]}]
set_input_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports start_i]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[31]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[30]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[29]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[28]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[27]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[26]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[25]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[24]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[23]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[22]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[21]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[20]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[19]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[18]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[17]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[16]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[15]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[14]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[13]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[12]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[11]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[10]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[9]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[8]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[7]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[6]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[5]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[4]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[3]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[2]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[1]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports {output_o[0]}]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports ready_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports ine_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports overflow_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports underflow_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports div_zero_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports inf_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports zero_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports qnan_o]
set_output_delay -clock [get_clocks clk_i] -add_delay 0.0 [get_ports snan_o]
set_wire_load_mode "enclosed"
