#!/bin/csh

source ./csh_ee201a_setup

/w/class.1/ee/ee201o/ee201ota/oa/bin/linux_rhel40_64/opt/lef2oa -lib DesignLib -lef "$1" -dataModel 3 > lef2oa.logx
/w/class.1/ee/ee201o/ee201ota/oa/bin/linux_rhel40_64/opt/verilog2oa -lib DesignLib -refLibs DesignLib -verilog "$3" -dataModel 3 > verilog2oa.logx
/w/class.1/ee/ee201o/ee201ota/oa/bin/linux_rhel40_64/opt/def2oa -lib DesignLib -def "$2" -dataModel 3 > def2oa.logx

./bound_checker