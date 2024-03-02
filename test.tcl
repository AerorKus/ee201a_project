
set counter 0

# set fp [open "data" r]
# while { [gets $fp data] >= 0 } {
#     if {$counter == 0} {set position $data}
#     if {$counter == 1} {set layer_metal(0) $data}
#     if {$counter == 2} {set layer_metal(1) $data}
#     if {$counter == 3} {set layer_metal(2) $data}
#     if {$counter == 4} {set layer_metal(3) $data}
#     incr counter
# }

set routeblk_llx 50
set routeblk_lly 20
set routeblk_urx 20
set routeblk_ury 20
set placeblk_lly 10
set placeblk_ury 10

set fp_routeblk [open "routeblk" w+]
puts $fp_routeblk " $routeblk_llx\n$routeblk_lly\n$routeblk_urx\n$routeblk_ury"
close $fp_routeblk

set fp_placeblk [open "placeblk" w+]
puts $fp_placeblk " $routeblk_llx\n$placeblk_lly\n$routeblk_urx\n$placeblk_ury"
close $fp_placeblk


