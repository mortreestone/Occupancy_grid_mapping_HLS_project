import os
import sys
from os import path


def main(argv):
    #print(argv)
    if len(argv) != 3:
        print("error")
        return 1

    report = {}
    #print(argv[1])
    if argv[1] == "-d":
        argv[1] = "solution1/syn/report/csynth.xml"


    # file = open('fixed32031.prj/solution1/csim/report/ogm_csim.log', 'r')
    file = open(argv[1], 'r')

    keep_phrases = ["INFO:",
              "Compiling",
              "Generating","L="]


    lines = file.read().splitlines()

    k="0"
    percent=(int(argv[2])%10)*10
    length=int(int(argv[2])/1000)
    integer=int(int(argv[2])/10)-(length*100)

    print(percent)
    print(length)
    print(integer)

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
            print(argv[2])
    except:
        print(" ")
        print("process error in")
        print( argv[2])



if __name__ == "__main__":
    main(sys.argv)