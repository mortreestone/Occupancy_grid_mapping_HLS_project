#!/usr/bin/python3

'''
Created on June 13, 2019 by Wesley Stirk

Finds and calculates the power after the data has been generated. 

Last updated on June 13, 2019 by Wesley Stirk
'''


import os
import sys
import csv
import xml.etree.ElementTree as et
from os import path
#import mngdata


def main(argv) :
    if len(argv) < 3 :
        print("Invalid arguments.")
        print(sys.argv)
        exit()
    
    xmlFile = sys.argv[1]
    power=ParsePowerXML(xmlFile)
    print(power)
    report = {}
    report['design num'] = argv[2]
    report['power']  = power

    fieldnames= report.keys()
    if path.exists('power_report.csv'):
        print("write in mama")
        with open('power_report.csv', 'a') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writerow(report)     
    else:
        with open('power_report.csv','w') as output:
            print("write in baby")
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(report)
    print("yeah yeah")
    


def ParsePowerXML(xmlFile) :
    tree = et.parse(xmlFile)
    root = tree.getroot()
    KEY_WORD = "Total On-Chip Power (W)" #key word that vivado ouput when doing a power report


    useNext = False

    power = None #starts as none which allows it be tested later on
    for r in root.iter() :
        if useNext : #if the next iterabl contains the information we need
            power = float(r.attrib['contents'])
            break
        else :
            if KEY_WORD in r.attrib.values() : #find the key word. The row after has the value we need.
                useNext = True

    #todo: do error checking on whether the power value was actually found?

    return power


if __name__ == '__main__' :
    main(sys.argv)
