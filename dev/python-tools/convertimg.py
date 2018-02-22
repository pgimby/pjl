#!/usr/bin/python3

#import packages
import os

rootDir="/usr/local/master/labs/rawphotos"
output=rootDir + "/output"

imgageList = []
def listOfImg(rootDir):
	imageList = []
	print(rootDir)
	for root, dirs, files in os.walk(rootDir):
		for i in files:
			if "img.jpg" in i:
				imageList.append(i)

	return imageList

imageList = listOfImg(rootDir)
for i in imageList:
	inputPath = rootDir + "/" + i
	os.system("convert " + inputPath + " -gravity center -resize 200x200^ -crop 200x200+0+0 " + output + "/"+ i)