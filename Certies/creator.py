#!/bin/python
import os
try:
	os.mkdir("DONE")
	os.mkdir("SVGS")
except :
	pass

with open("names.txt") as f :
	for postName in f.readlines() :
		post, name = postName.strip('\n').split(' - ')
		filename = post + name
		with open("finalcerti.svg") as cert :
			certi = cert.read()
			certi = certi.replace("Abhay", name).replace("PRESIDENT", post)
		with open( "SVGS/" + post + name + ".svg","w") as expo :
			expo.write(certi)
		os.system("inkscape -z \"SVGS/{}.svg\" -d 300 -e DONE/\"{}.png\"".format(post + name, post + name))
