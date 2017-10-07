import sys
import os
import re

try:
	sys.argv[1]
except IndexError:
	print "Usage: python "+sys.argv[0]+" <filename>"
else:
#Retrieve info from twitter
	with open(sys.argv[1], 'r') as f:
		for line in f:
			os.system('wget -O - '+line.rstrip()+' | grep "      <title>" >> tempFile')

#Create output file
	output = open(sys.argv[1]+"_Results", 'w+')

#Clean it up
	with open('tempFile', 'r') as f:
		for line in f:
			tempLine = line.strip()
			tempLine=tempLine[7:]
			tempLine=tempLine[:-14]
			tempLine = re.sub(" on Twitter","",tempLine)
			tempLine = re.sub("&quot;","", tempLine)
			output.write(tempLine+"\n")
	output.close()
	os.system('rm tempFile')
