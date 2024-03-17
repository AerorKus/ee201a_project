SHELL := /bin/bash

PERF = run_combined_checker.csh
LEF = NangateOpenCellLibrary.lef
DEF = output/s1494_postrouting.def 
VERILOG = output/s1494_postrouting.v
YAML = blockages_definition.yaml 

default:
	@python3 src/project.py 0.88

info:
	@echo "./$(PERF) $(VERILOG) $(YAML)" 

clean:
	./clean_checkers.sh
	./clean.sh
	
