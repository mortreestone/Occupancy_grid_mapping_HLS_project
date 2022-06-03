import pathlib
import argparse
import numpy as np
import subprocess
import sys
import os
import csv


TEST_PATH = pathlib.Path(__file__).resolve().parent.parent
HLS_PATH = TEST_PATH / "HLS_OGM"
REPORT_PATH = HLS_PATH / "report"
DATATYPE_PATH = HLS_PATH / "datatype"
FLOAT_PATH = DATATYPE_PATH / "float"
FIXED_PATH = DATATYPE_PATH / "fixed"
FIXD1_PATH = FIXED_PATH / "design1"
FIXD2_PATH = FIXED_PATH / "design2"
FIXD3_PATH = FIXED_PATH / "design3"
RESLU_PATH = HLS_PATH / "resolution_A"
ALPHA_PATH = HLS_PATH / "alpha"




# type: 1-float 2-fixed1 3-fixed2 4-fixed3 5-reslu 
class design:
    def __init__(self,typee,argu1,argu2,res,acc,p_acc,late,lut,ff,dsp,bram):
        self.typee =typee
        self.argu1 =argu1
        self.argu2 = argu2
        self.res = res
        self.acc = acc
        self.p_acc=p_acc
        self.late = late
        self.lut=lut
        self.ff=ff
        self.dsp=dsp
        self.bram=bram



def run_hls(cmd):
     subprocess.run(
                cmd,
                universal_newlines=True,
        )


def run_hls2():
    cmd= [str(HLS_PATH /'source.sh')]
    os.system(r'chmod u+x ../HLS_src/source.sh')
    os.system(r'./source.sh')

    cmdh='vitis_hls -f ../HLS_src/datatype/float/runfloat.tcl'
    os.system(cmdh)
    #subprocess.run('source /tools/Xilinx/Vivado/2020.2/settings64.sh' , universal_newlines= True)
    #subprocess.run('vitis_hls -f ../HLS_src/datatype/float/runfloat.tcl' , universal_newlines= True)
    

def selection(data):
    return 1 , 0


def main(resolution,lut_max, ff_max, dsp_max, bram_max,lantency_max,power_max,accuracy_min):


    print("resoulution: ", resolution)
    print("Max LUT: ", lut_max)
    print("Max FF", ff_max)
    print("Max DSP", dsp_max)
    print("Max BRAM", bram_max)
    print("Max Latency", lantency_max, "ns")
    print("Max Power", power_max, "W")
    print("Min Accuracy", accuracy_min, "%")

    report2= str(REPORT_PATH / 'report2s.csv')
    reports= str(REPORT_PATH / 'reports.csv')


    file =open(report2)
    csvreader=csv.reader(file)
    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)
    data={}
    count =0
    for i in range(len(rows)):
        typee= int(rows[i][0])
        argu1= float(rows[i][1])
        argu2= float(rows[i][2])
        acc= float(rows[i][4])
        late= int(rows[i][6])
        lut= int(rows[i][10])
        ff= int(rows[i][9])
        dsp= int(rows[i][12])
        bram= int(rows[i][11])
        p_acc=acc - 5
        #if late == 0:
            #continue
        d=design(typee,argu1,argu2,0.5,acc,p_acc,late,lut,ff,dsp,bram) 
        data[i]=d
        count = i
    
    file2 =open(reports)
    csvreader2=csv.reader(file2)
    header = next(csvreader2)
    rows2 = []
    for row2 in csvreader2:
        rows2.append(row2)


    for i in range(len(rows2)):
        typee= int(rows2[i][0])
        argu1= float(rows2[i][1])
        argu2= float(rows2[i][2])
        p_acc= float(rows2[i][3])
        late= int(rows2[i][5])
        lut= int(rows2[i][9])
        ff= int(rows2[i][8])
        dsp= int(rows2[i][11])
        bram= int(rows2[i][10])
        acc = p_acc
        res = argu1
        #if late == 0:
            #continue
        d=design(typee,argu1,argu2,res,acc,p_acc,late,lut,ff,dsp,bram) 
        j = count+i
        data[j]=d

    for i in range(len(data)):
        print(i,data[i].typee,data[i].res)




    flaot_typ=False
    fixed1_typ=False
    fixed2_typ=False
    fixed3_typ=False    
    resolution_type=False
    alpha_type=False


    design_type, design_num=selection(data)

    if design_type==1:
        flaot_typ =True
    elif design_type==2:
        fixed1_typ =True
    elif design_type==3:
        fixed2_typ =True
    elif design_type==4:
        fixed3_typ =True
    elif design_type==5:
        resolution_type =True




    if flaot_typ:
        cmd= [str(FLOAT_PATH /'run.sh')]
        #run_hls2()
        #run_hls(cmd)
    elif fixed1_typ:
        cmd= [str(FIXD1_PATH /'run.sh')]
        run_hls(cmd)
    elif fixed2_typ:
        cmd= [str(FIXD2_PATH /'run.sh')]
        run_hls(cmd)
    elif fixed3_typ:
        cmd= [str(FIXD3_PATH /'run.sh')]
        run_hls(cmd)
    elif resolution_type:
        cmd= [str(RESLU_PATH /'run.sh')]
        run_hls(cmd)
    elif alpha_type:
        cmd= [str(ALPHA_PATH /'run.sh')]
        run_hls(cmd)
    else:    
        print("Found no solution")


    print("Selected Design Result:")
    print("accuracy:", data[design_num].acc)
    print("latency:",data[design_num].late)
    print("LUT:",data[design_num].lut)
    print("FF:",data[design_num].ff)
    print("DSP:",data[design_num].dsp)
    print("BRAM:",data[design_num].bram)

    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Occupancy Grid Map Hardware Builder")
    # parser.add_argument("-p", "--plot_live", action="store_true", help="Whether we should plot as we go")
    # parser.add_argument("-d", "--datafile", type=str, default="data/rooms-dataset.npz", help="Location of data. Defaults to data/rooms-dataset.npz")
    parser.add_argument("-r", "--resolution", type=float, default=0.5, help="Grid resolution. Range: default=0.5")
    parser.add_argument("-lut", "--lut_max", type=int, default=53200, help="Setting the maximuin utilization of LUT. Minimuim value:16000. default: 53200")
    parser.add_argument("-ff", "--ff_max", type=int, default=10000, help="Setting the maximuin utilization of FF. Minimuim value:10000. default: 10000")
    parser.add_argument("-dsp", "--dsp_max", type=int, default=60, help="Setting the maximuin utilization of DSP. Minimuim value:12. default: 60")
    parser.add_argument("-bram", "--bram_max", type=int, default=6, help="Setting the maximuin utilization of BRAM. Minimuim value:0. default: 6")
    parser.add_argument("-l", "--lantency_max", type= int, default=10000, help="Setting the maximuin latency in nano second. Minimuin value: 10000 ns. default:10000")
    parser.add_argument("-power", "--power_max", type= float, default =0.5, help="Setting the maximuin power in Watt. Minimuin value: 0.2 W. default:0.5")
    parser.add_argument("-acc", "--accuracy_min", type=float, default=95, help="Setting the minimuin accuracy in percent. Minimuin value: 20%%. default:95%%")
    args = vars(parser.parse_args())

    main(**args)