SHELL := /bin/bash

PERF = run_perf_checker.csh
STRIP = run_blockage_checker.csh
CHECK = run_checkers.csh
LEF = NangateOpenCellLibrary.lef
DEF = output/s1494_postrouting.def 
VERILOG = output/s1494_postrouting.v
YAML = blockages_definition.yaml 

default:
	python3 a.py
in:
	innovus -nowin < innovus_skeleton.tcl

test:
	innovus -nowin < test.tcl


info:
	@echo "./$(PERF) $(LEF) $(DEF) $(VERILOG)"
	@echo "./$(STRIP) ../../$(LEF) ../../$(DEF) ../../$(VERILOG) ../../$(YAML)"

clean:
	./clean_checkers.sh
	./clean.sh
