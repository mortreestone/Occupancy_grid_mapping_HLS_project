############################################################
## author: Szu-Wei Lin
## date: Jul/29/2021
## This is the tcl file for resolution parameters design 
############################################################

# get the values of parameters from bash script
set R [lindex $argv 2]
puts "R : $R"
set A [lindex $argv 3]
puts "A : $A"
set X [lindex $argv 4]
puts "X : $X"
set Y [lindex $argv 5]
puts "Y : $Y"
set E [lindex $argv 6]
puts "E : $E"
set P [lindex $argv 7]
puts "P : $P"

set currDir [pwd]
puts "pwd : $currDir"

set CFLAGS "-DPRESOLUTION=${R} -DPA=${A} -DPYDIM=${Y} -DPXDIM=${X} -DPALFA=${E}" 


# Project name
set hls_prj al_${P}.prj


# Open/reset the project
open_project ${hls_prj}

# add source files 
add_files alpha/header.h -cflags $CFLAGS
add_files alpha/ogm.cpp -cflags $CFLAGS

# add testbench files
add_files -tb alpha/data.h -cflags $CFLAGS
add_files -tb alpha/grid_1.h -cflags $CFLAGS
add_files -tb alpha/main.cpp -cflags $CFLAGS

#set top module
set_top ogm


# synthesis setup 
open_solution "solution1" -flow_target vivado
set_part {xc7z020clg400-1}
create_clock -period 10 -name default

# HLS directives
#source "./ogm4/solution1/directives.tcl"
set_directive_interface -mode s_axilite "ogm" xi
set_directive_interface -mode s_axilite "ogm" yi
set_directive_interface -mode s_axilite "ogm" thetai
set_directive_interface -mode s_axilite "ogm" angle
set_directive_interface -mode s_axilite "ogm" z_t
set_directive_interface -mode m_axi -offset slave "ogm" grid

csim_design
csynth_design

export_design -flow syn -rtl verilog -format ip_catalog -output $currDir/output/${hls_prj}_1.zip


exit