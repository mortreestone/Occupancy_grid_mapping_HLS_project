#!/usr/bin/python

import sys
import csv
import xml.etree.ElementTree as ET
from os import path




def main(argv):
    print(argv)
    if len(argv) != 4:
        print("error")
        return 1

    report = {}
    print(argv[1])
    if argv[1] == "-d":
        argv[1] = "solution1/syn/report/csynth.xml"

    file = open(argv[2], 'r')
    keep_phrases = ["INFO:",
              "Compiling",
              "Generating","L="]
    lines = file.read().splitlines()
    k="0"

    for line in lines:
        i=0
        for phrase in keep_phrases:
            if phrase in line:
                i = i+1
                break
        if(i==0):
            k=line

    try:
        ki=float(k)
        #print(ki)
        if ki ==0 :
            print("process incomplete in")
            print(argv[3])
            ki =-1
    except:
        print(" ")
        print("process error in")
        print( argv[3])
        ki=-2


    length = int((int(argv[3])%10000)/100)
    integer =int(int(argv[3])%100)
    percent= int(integer/length * 100)
    report['design num'] = argv[3]
    report['length'] = length
    report['integer'] = integer
    report['d-point percentage'] = percent
    report['accurcy'] =ki

    try:
        root = ET.parse(argv[1]).getroot()
        print(root)  
        perf_estim = root.find('PerformanceEstimates')
        area_estim = root.find('AreaEstimates/Resources')   
        report['estim_clock'] = perf_estim.find('SummaryOfTimingAnalysis/EstimatedClockPeriod').text
        report['lat_worst'] = perf_estim.find('SummaryOfOverallLatency/Worst-caseLatency').text
        report['lat_avg'] = perf_estim.find('SummaryOfOverallLatency/Average-caseLatency').text
        report['lat_best'] = perf_estim.find('SummaryOfOverallLatency/Best-caseLatency').text
        report['FF'] = area_estim.find('FF').text
        report['LUT'] = area_estim.find('LUT').text
        report['BRAM'] = area_estim.find('BRAM_18K').text
        report['DSP'] = area_estim.find('DSP').text




        
    except OSError:
        print("no result")
        report['estim_clock'] = 0
        report['lat_worst'] = 0
        report['lat_avg'] = 0
        report['lat_best'] = 0
        report['FF'] = 0
        report['LUT'] = 0
        report['BRAM'] = 0
        report['DSP'] = 0
        
    





    #user_assign = root.find('UserAssignments')




    # report['estim_clock'] = perf_estim.find('SummaryOfTimingAnalysis/EstimatedClockPeriod').text
    # report['lat_worst'] = perf_estim.find('SummaryOfOverallLatency/Worst-caseLatency').text
    # report['lat_avg'] = perf_estim.find('SummaryOfOverallLatency/Average-caseLatency').text
    # report['lat_best'] = perf_estim.find('SummaryOfOverallLatency/Best-caseLatency').text

    # report['FF'] = area_estim.find('FF').text
    # report['LUT'] = area_estim.find('LUT').text
    # report['BRAM'] = area_estim.find('BRAM_18K').text
    # report['DSP'] = area_estim.find('DSP').text


    fieldnames= report.keys()
    if path.exists('report2s.csv'):
        print("write in mama")
        with open('report2s.csv', 'a') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writerow(report)     
    else:
        with open('report2s.csv','w') as output:
            print("write in baby")
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(report)
    print("yeah yeah")

if __name__ == "__main__":
    main(sys.argv)