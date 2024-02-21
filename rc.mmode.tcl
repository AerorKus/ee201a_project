create_library_set -name default_library_set -timing ./NangateOpenCellLibrary_typical_conditional_nldm.lib
create_rc_corner -name _default_rc_corner_ -T 25.0
create_delay_corner -name _default_delay_corner_ -library_set default_library_set -opcond typical  -opcond_library NangateOpenCellLibrary -rc_corner _default_rc_corner_
create_constraint_mode -name _default_constraint_mode_ -sdc_files {s1494.sdc}
 
create_analysis_view -name _default_view_  -constraint_mode _default_constraint_mode_ -delay_corner _default_delay_corner_
 
 
## set_analysis_view -setup _default_view_  -hold _default_view_
 
