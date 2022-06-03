############################################################
## author: Szu-Wei Lin
## date: Jul/29/2021
## This is the tcl file for fixed-point 
############################################################

# get the values of parameters from bash script
#set I [lindex $argv 2]
#puts "I : $I"
#set L [lindex $argv 3]
#puts "L : $L"
#set P [lindex $argv 4]
#puts "P : $P"


#set CFLAGS "-DL_CONST=${L} -DI_CONST=${I}" 

# Project name
set hls_prj float.prj


# Open/reset the project
open_project ${hls_prj} -reset

# add source files 
#add_files ../HLS_src/datatype/float/header.h -cflags $CFLAGS
#add_files ../HLS_src/datatype/float/ogm.cpp -cflags $CFLAGS
add_files ../HLS_src/datatype/float/header.h
add_files ../HLS_src/datatype/float/ogm.cpp

# add testbench files
#add_files -tb ../HLS_src/datatype/float/data.h -cflags $CFLAGS
#add_files -tb ../HLS_src/datatype/float/grid1.h -cflags $CFLAGS
#add_files -tb ../HLS_src/datatype/float/main.cpp -cflags $CFLAGS
add_files -tb ../HLS_src/datatype/float/data.h 
add_files -tb ../HLS_src/datatype/float/grid1.h 
add_files -tb ../HLS_src/datatype/float/main.cpp

#set top module
set_top ogm


# synthesis setup 
open_solution "solution1" -flow_target vivado
set_part {xc7z020clg400-1}
create_clock -period 10 -name default

# HLS directives
#source "./ogm4/solution1/directives.tcl"
set_directive_top -name ogm "ogm"
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