import pathlib
import argparse
import numpy as np
import subprocess
import os
from multiprocessing import Pool


HLS_PATH = pathlib.Path(__file__).resolve().parent
DATATYPE_PATH = HLS_PATH / "datatype"
FLOAT_PATH = DATATYPE_PATH / "float"
FIXED_PATH = DATATYPE_PATH / "fixed"
FIXD1_PATH = FIXED_PATH / "design1"
FIXD2_PATH = FIXED_PATH / "design2"
FIXD3_PATH = FIXED_PATH / "design3"
RESLU_PATH = HLS_PATH / "resolution_A"
ALPHA_PATH = HLS_PATH / "alpha"


def run_hls1(q):
    os.system(q[0])
    subprocess.call(q[1], shell=True)
    os.system(q[2])
    subprocess.call(q[3], shell=True)
    os.system(q[4])

def main(resolution,floating,design1,design2,design3,alpha):

    q=[]
    if(floating):
        pathls=str(FLOAT_PATH /'runfloat.tcl')
        pathcsv=str(FLOAT_PATH /'hls_csv.py')
        pathpower= str(FLOAT_PATH /'power.tcl')
        pathfpower = str(FLOAT_PATH /'findpower.py')
        pathdelete = str(FLOAT_PATH /'del.tcl')
        
        cmdhls='vitis_hls -f ' + pathls +' 27 18 float'
        cmdcsv = 'python3 ' + pathcsv +' float.prj/solution1/syn/report/csynth.xml float.prj/solution1/csim/report/ogm_csim.log 0'
        cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs float"
        cmdfpwr= 'python3 ' + pathfpower +' float.prj/power_report.xml 0'
        cmddele= 'vitis_hls -f ' + pathdelete +' float'
        print(cmdhls)
        q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])
        # run_hls1([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])   


 
    if(design1):
          for l in [36,34,32,30,28,26,24,22,20,18,16,14]:
              for k in [8,7,6,5,4,3,2]:
                i=int(l*k/10)
                p = 10000+100*l+i
                pathls=str(FIXD1_PATH /'runfixed.tcl')
                pathcsv=str(FIXD1_PATH /'hls_csv.py')
                pathpower= str(FIXD1_PATH /'power.tcl')
                pathfpower = str(FIXD1_PATH /'findpower.py')
                pathdelete = str(FIXD1_PATH /'del.tcl')             
        
                cmdhls='vitis_hls -f ' + pathls +' ' + str(i) +' '+ str(l) +' ' + str(p)
                cmdcsv = 'python3 ' + pathcsv +' fixed_' +str(p) + '.prj/solution1/syn/report/csynth.xml fixed_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
                cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
                cmdfpwr= 'python3 ' + pathfpower +' fixed_' +str(p) +'.prj/power_report.xml ' +str(p)
                cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       
                print(cmdhls)
                q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])
                #run_hls1([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])

    if(design2):
          for l in [36,34,32,30,28,26,24,22,20,18,16,14]:
              for k in [8,7,6,5,4,3,2]:
                i=int(l*k/10)
                p = int(20000+100*l+i)
                pathls=str(FIXD2_PATH /'runfixed.tcl')
                pathcsv=str(FIXD2_PATH /'hls_csv.py')
                pathpower= str(FIXD2_PATH /'power.tcl')
                pathfpower = str(FIXD2_PATH /'findpower.py')
                pathdelete = str(FIXD2_PATH /'del.tcl')                    
        
                cmdhls='vitis_hls -f ' + pathls +' ' + str(i) +' '+ str(l) +' ' + str(p)
                cmdcsv = 'python3 ' + pathcsv +' fixed_' +str(p) + '.prj/solution1/syn/report/csynth.xml fixed_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
                cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
                cmdfpwr= 'python3 ' + pathfpower +' fixed_' +str(p) +'.prj/power_report.xml ' +str(p)
                cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       

                print(cmdhls)
                q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])

    if(design3):
          for l in [36,34,32,30,28,26,24,22,20,18,16,14]:
              for k in [8,7,6,5,4,3,2]:       
                i=int(l*k/10)
                p = 30000+100*l+i
                pathls=str(FIXD3_PATH /'runfixed.tcl')
                pathcsv=str(FIXD3_PATH /'hls_csv.py')
                pathpower= str(FIXD3_PATH /'power.tcl')
                pathfpower = str(FIXD3_PATH /'findpower.py')
                pathdelete = str(FIXD3_PATH /'del.tcl')    

                cmdhls='vitis_hls -f ' + pathls +' ' + str(i) +' '+ str(l) +' ' + str(p)
                cmdcsv = 'python3 ' + pathcsv +' fixed_' +str(p) + '.prj/solution1/syn/report/csynth.xml fixed_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
                cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
                cmdfpwr= 'python3 ' + pathfpower +' fixed_' +str(p) +'.prj/power_report.xml ' +str(p)
                cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       

                print(cmdhls)
                q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])
                #run_hls1(cmdhls,cmdcsv,cmdviv,cmdfpwr)          


    if(resolution):
        for r in [2,1,0.5,0.25,0.125]:
            for b in [0.5,1,1.5,2]:                    
                a= r*b
                x=int(70/r)
                y=int(60/r)
                p=int(40000+r*80+b*2)
                pathls=str(RESLU_PATH /'resrun.tcl')
                pathcsv=str(RESLU_PATH /'hls_csv.py')
                pathpower= str(RESLU_PATH /'power.tcl')
                pathfpower = str(RESLU_PATH /'findpower.py')
                pathdelete = str(RESLU_PATH /'del.tcl')  
        
                cmdhls='vitis_hls -f ' + pathls +' ' + str(r) +' '+ str(a) +' ' + str(x)+' ' + str(y)+' ' + str(p)
                cmdcsv = 'python3 ' + pathcsv +' res_' +str(p) + '.prj/solution1/syn/report/csynth.xml res_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
                cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
                cmdfpwr= 'python3 ' + pathfpower +' res_' +str(p) +'.prj/power_report.xml ' +str(p)
                cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       
                print(cmdhls)
                q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])
                #run_hls1(cmdhls,cmdcsv,cmdviv,cmdfpwr)          


    if(alpha):
        for c in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
            r=0.5
            a=r
            x=int(70/r)
            y=int(60/r)
            p=int(50000+r*800+c*10)
            pathls=str(ALPHA_PATH /'alrun.tcl')
            pathcsv=str(ALPHA_PATH /'hls_csv.py')
            pathpower= str(ALPHA_PATH /'power.tcl')
            pathfpower = str(ALPHA_PATH /'findpower.py')
            pathdelete = str(ALPHA_PATH /'del.tcl')  
            cmdhls='vitis_hls -f ' + pathls +' ' + str(r) +' '+ str(a) +' ' + str(x)+' ' + str(y)+' ' + str(c)+' ' + str(p)
            cmdcsv = 'python3 ' + pathcsv +' al_' +str(p) + '.prj/solution1/syn/report/csynth.xml al_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
            cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
            cmdfpwr= 'python3 ' + pathfpower +' al_' +str(p) +'.prj/power_report.xml ' +str(p)
            cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       
            print(cmdhls)
            q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])
        for c in [0.1,0.2,0.3,0.4,0.5]:
            r=0.25
            a=r
            x=int(70/r)
            y=int(60/r)
            p=int(50000+r*800+c*10)
            pathls=str(ALPHA_PATH /'alrun.tcl')
            pathcsv=str(ALPHA_PATH /'hls_csv.py')
            pathpower= str(ALPHA_PATH /'power.tcl')
            pathfpower = str(ALPHA_PATH /'findpower.py')
            pathdelete = str(ALPHA_PATH /'del.tcl')  
            cmdhls='vitis_hls -f ' + pathls +' ' + str(r) +' '+ str(a) +' ' + str(x)+' ' + str(y)+' ' + str(c)+' ' + str(p)
            cmdcsv = 'python3 ' + pathcsv +' al_' +str(p) + '.prj/solution1/syn/report/csynth.xml al_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
            cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
            cmdfpwr= 'python3 ' + pathfpower +' al_' +str(p) +'.prj/power_report.xml ' +str(p)
            cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       
            print(cmdhls)
            q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])   
        for c in [0.1,0.2,0.3]:
            r=0.125
            a=r
            x=int(70/r)
            y=int(60/r)
            p=int(50000+r*800+c*10)
            pathls=str(ALPHA_PATH /'alrun.tcl')
            pathcsv=str(ALPHA_PATH /'hls_csv.py')
            pathpower= str(ALPHA_PATH /'power.tcl')
            pathfpower = str(ALPHA_PATH /'findpower.py')
            pathdelete = str(ALPHA_PATH /'del.tcl')  
            cmdhls='vitis_hls -f ' + pathls +' ' + str(r) +' '+ str(a) +' ' + str(x)+' ' + str(y)+' ' + str(c)+' ' + str(p)
            cmdcsv = 'python3 ' + pathcsv +' al_' +str(p) + '.prj/solution1/syn/report/csynth.xml al_' +str(p) +'.prj/solution1/csim/report/ogm_csim.log '+ str(p)
            cmdviv='vivado -mode batch -source ' +pathpower + " -tclargs " + str(p)
            cmdfpwr= 'python3 ' + pathfpower +' al_' +str(p) +'.prj/power_report.xml ' +str(p)
            cmddele= 'vitis_hls -f ' + pathdelete +' '+ str(p)       
            print(cmdhls)
            q.append([cmdhls,cmdcsv,cmdviv,cmdfpwr,cmddele])   






    print(os.cpu_count())
    pool = Pool(3)
    pool.map(run_hls1,q)
    pool.close()
    pool.join()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Occupancy Grid Map Hardware Builder")
    parser.add_argument("-r", "--resolution", action="store_true", help="different resoluation and A")
    parser.add_argument("-f", "--floating", action="store_true", help="where datatype is floating point")
    parser.add_argument("-d1", "--design1", action="store_true", help="here datatype is fixed design1")
    parser.add_argument("-d2", "--design2", action="store_true", help="here datatype is fixed design2")
    parser.add_argument("-d3", "--design3", action="store_true", help="here datatype is fixed design3")
    parser.add_argument("-a", "--alpha", action="store_true", help="different alpha")
    args = vars(parser.parse_args())

    main(**args)