# ******************************************************************************
# ******************************************************************************
#
#	 Makefile for building OpenAccess Example Applications
#
# ******************************************************************************
# Except as specified in the OpenAccess terms of use of Cadence or Silicon
# Integration Initiative, this material may not be copied, modified,
# re-published, uploaded, executed, or distributed in any way, in any medium,
# in whole or in part, without prior written permission from Cadence.
#
#                Copyright 2002-2005 Cadence Design Systems, Inc.
#                           All Rights Reserved.
#
#  $Author: icftcm $
#  $Revision: #1 $
#  $Date: 2010/08/09 $
# ******************************************************************************
# ******************************************************************************


include /w/class.1/ee/ee201o/ee201ota/oa_macro.defs

PROG = bound_checker

DEFAULT: $(PROG)

cvs:
	@$(MAKE) TOOLSDIR=../../../../$(PLATFORM)/tools.$(PLATFORM) $(PROG) 


# Compile the application code
$(PROG).o: $(PROG).cpp 
	$(CCPATH) $(CXXOPTS) $(DEBUG) -o $(PROG).o -I$(TOOLSDIR)/include/oa \
	 -I$(TOOLSDIR)/include \
	 -c $(PROG).cpp 

# Link the executable

$(PROG): $(PROG).o  $(OA_LIB_LIST)
	$(CCPATH) $(CXXOPTS) -o $(PROG)  $(PROG).o \
         $(COMMON_CODE) \
	 -L$(OA_LIB_DIR) \
	 -loaCommon \
	 -loaBase \
	 -loaPlugIn\
	 -loaDM\
	 -loaTech\
         -loaDesign\
	 $(SYSLIBS)

clean: 
	@/bin/rm  -rf $(PROG).o 
	@/bin/rm  -rf $(PROG) 
