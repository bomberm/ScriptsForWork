import sys
import os
import re

def process(imageLinks):
	with open('tempFile', 'r') as f:
		imageCount = 1
		for line in f:
			image = ""
			if re.search('<title>', line):
				tweet = line.split(':', 1)[0]
				tweet = tweet[13:-11]
			elif re.search('og:image"', line):
				image = line.split("content=")[1]
				image = image[1:-3]
			elif re.search('og:description', line):
				line = line.strip()
				line=line[42:-2]
				tweet += ": "+line.replace('&quot;','')+'\n'
				return tweet
			if image != "":
				imageLinks.write(image+'\n')
				imageCount += 1
			
try:
	sys.argv[1]
except IndexError:
	print "Usage: python "+sys.argv[0]+" <filename>"
else:

	results = []
	images = open('images', 'w+')
#Retrieve info from twitter
	with open(sys.argv[1], 'r') as f:
		for line in f:
			os.system('wget -q -O - '+line.rstrip()+' > tempFile')
			results.append(process(images))

	images.close()
#Scrape images
	with open('images', 'r') as f:
		for line in f:
			line = line.split(":large")[0]
			if not re.search('profile_images', line):
				os.system('wget '+line.rstrip())

#Create output file
	output = open(sys.argv[1]+"_Results", 'w+')

#Write output file
	output.writelines(results)
	output.close()
	os.system('rm tempFile')
	os.system('rm images')
