############################################################
## author: Szu-Wei Lin
## date: May/22/2022
## This is the tcl file for delete_project
############################################################

# get the values of parameters from bash script
set P [lindex $argv 2]
puts "P : $P"

# Project name
set hls_prj float.prj
delete_project ${hls_prj}

exit