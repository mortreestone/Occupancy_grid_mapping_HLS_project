#!/bin/bash
# Bash script for the fixed-point design, by me

source /tools/Xilinx/Vivado/2020.2/settings64.sh


# r=0.5
#     for c in {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1}
#     do
#         b=1
#         a=`echo "$r*$b" |bc -l`
#         x=`echo "70/$r" |bc -l`
#         y=`echo "60/$r" |bc -l`
#         p=`echo "10*$c" |bc -l`
#         d=`echo "$c" |bc -l`
#         #s= $p+"accuracy"
#         # echo $r
#         # echo $a
#         # echo $x
#         # echo $y
#         # echo $p
#         sem -j+0
#             #nice vitis_hls -f alrun.tcl $r $a $x $y $d $p 
#             #vivado -mode batch -source power.tcl -tclargs $p &
#             python3 hls_csv.py $p.prj/solution1/syn/report/csynth.xml $p.prj/solution1/csim/report/ogm_csim.log $p 
#             #python3 findpower.py res$p.prj/power_report.xml $p 
#             #python3 csm.py $p.prj/solution1/csim/report/ogm_csim.log $p $r
#             #python3 $s.py $r
#         #}&
#  done
# sem --wait



# r=0.25
#     for c in {0.4,0.5}
#     do
#         b=1
#         a=`echo "$r*$b" |bc -l`
#         x=`echo "70/$r" |bc -l`
#         y=`echo "60/$r" |bc -l`
#         p=`echo "10*$c+250" |bc -l`
#         d=`echo "$c" |bc -l`
#         #s= $p+"accuracy"
#         # echo $r
#         # echo $a
#         # echo $x
#         # echo $y
#         # echo $p
#         sem -j+0
#             #nice vitis_hls -f alrun.tcl $r $a $x $y $d $p 
#             #vivado -mode batch -source power.tcl -tclargs $p &
#             python3 hls_csv.py $p.prj/solution1/syn/report/csynth.xml $p.prj/solution1/csim/report/ogm_csim.log $p 
#             #python3 findpower.py res$p.prj/power_report.xml $p 
#             #python3 csm.py $p.prj/solution1/csim/report/ogm_csim.log $p $r
#             #python3 $s.py $r
#         #}&
#  done
# sem --wait



for r in {0.25,0.125}
do
    for c in {0.1,0.2,0.3}
    do
        b=1
        a=`echo "$r*$b" |bc -l`
        x=`echo "70/$r" |bc -l`
        y=`echo "60/$r" |bc -l`
        p=`echo "10*$c+100*$r" |bc -l`
        d=`echo "$c" |bc -l`
        #s= $p+"accuracy"
        # echo $r
        # echo $a
        # echo $x
        # echo $y
        # echo $p
        sem -j+0
            nice vitis_hls -f alrun.tcl $r $a $x $y $d $p 
            vivado -mode batch -source power.tcl -tclargs $p 
            python3 hls_csv.py $p.prj/solution1/syn/report/csynth.xml $p.prj/solution1/csim/report/ogm_csim.log $p 
            #python3 findpower.py res$p.prj/power_report.xml $p 
            #python3 csm.py $p.prj/solution1/csim/report/ogm_csim.log $p $r
            #python3 $s.py $r
        #}&
    done
    done



echo Hello World!
