#!/usr/bin/python
import glob, os, string
os.chdir(".")

print "File,        Eo,         G"

Ener=[]
for file in glob.glob("*.out"):
    ifile=open(file,"r")
    data=ifile.readlines()
    for line in data:
	if "Zero-point correction" in line: 
    	    datx=string.split(line)
            Ener.append(datx[2])
	if "Sum of electronic and zero-point Energies=" in line: 
    	    datx=string.split(line)
            Ener.append(datx[6])
	if "Sum of electronic and thermal Free Energies" in line: 
    	    datx=string.split(line)
            Ener.append(datx[7])
	    
    print file, float(Ener[1])-float(Ener[0]), Ener[2]



