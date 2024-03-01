
set counter 0

set fp [open "data" r]
while { [gets $fp data] >= 0 } {
    if {$counter == 0} {set position $data}
    if {$counter == 1} {set layer_metal(0) $data}
    if {$counter == 2} {set layer_metal(1) $data}
    if {$counter == 3} {set layer_metal(2) $data}
    if {$counter == 4} {set layer_metal(3) $data}
    incr counter
}

puts $position
puts $layer_metal(0)
puts $layer_metal(1)
puts $layer_metal(2)
puts $layer_metal(3)

close $fp

