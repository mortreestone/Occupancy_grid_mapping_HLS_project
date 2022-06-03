puts [llength $argv]
foreach i $argv {puts $i}
puts "The second arg is [lindex $argv 0]"

set P [lindex $argv 0]
puts "P : $P"

set currDir [pwd]
puts "pwd : $currDir"

open_project $currDir/res_${P}.prj/solution1/impl/verilog/project.xpr

reset_run synth_1

launch_runs impl_1 

wait_on_run impl_1

open_run impl_1

report_power -format xml -file $currDir/res_${P}.prj/power_report.xml

close_design
close_project
exit