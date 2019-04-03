#!/usr/bin/env python

#Working template of hydropathy score calculation script
#You need to put in comments for every line
import sys
import re

if len(sys.argv)<8:
    print ""
    print "Usage: hydropathy_graph.py -i <input file> -o <output file>"
    print "-i: input file"
    print "-o: output file"
    print ""


InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0

for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()

window=int(window)
Value=0
window_counter=0
InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + ".output.csv"
OutFile = open(OutFileName,"w")

for i in range(len(ProtSeq)):
    Value+=Hydropathy[ProtSeq[i]]
    if(i>(window-1) and i<=(len(ProtSeq)-window)):
        Value=Value-Hydropathy[ProtSeq[i-window]]
        OutString = "%d,%.2f" % (window_counter, Value)
        OutFile.write(OutString + "\n")

    window_counter+=1

OutFile.close()
