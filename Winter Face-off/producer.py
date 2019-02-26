#!/bin/python
import os

try :
    os.mkdir("NAMED")
    print("Created directory NAMED")
except :
    pass

with open("names") as names:
    for line in names.readlines():
        aname,bname = line.split()
        filename = aname+bname+".svg"
        newfile = ""
        with open('wfot.svg') as f :
            newfile = f.read().replace("Abhay",aname).replace("Raj",bname)

        with open("NAMED/"+filename,"w") as f:
            f.write(newfile)
