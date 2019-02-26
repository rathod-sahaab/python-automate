#!/bin/python
import os

try :
    os.mkdir("STAGE")
    print("Created directory STAGE")
except :
    pass

os.chdir("NAMED")
files = os.listdir()
for file in files :
	if file[-4:] == ".svg" :
		os.system("inkscape -z {} -e ../STAGE/{}.png".format(file,file[:-4]))
print("DONE!")
