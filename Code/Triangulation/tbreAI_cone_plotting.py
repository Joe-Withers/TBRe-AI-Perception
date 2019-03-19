#!/usr/bin/env python

import numpy as np

focalLength = 2
imageWidth = 1280
imageHeight = 720
depth = 260
coordinateList = []

def coordinateCalc(width, height, boxCornerX, boxCornerY)-> list:
	midPX = (boxCornerX + width)/2
	midPY = (boxCornerY + height)/2
	centerDistX = midPX - (imageWidth/2)
	centerDistY = midPY - (imageHeight/2)
	centerDistZ = (imageHeight/2 - midPY)

	return(centerDistX, centerDistY, centerDistZ)


def main():
	
	#coordinateList = coordinate.append(coordinateCalc(200, 200, 150, 160))
	#print(coordinateList)
	#this returns "none" when executed, not sure where the error is
	
	coordinate = np.array(coordinateCalc(200, 200, 150, 160))
	coordinate[0] = coordinate[0]*depth
	coordinate[1] = coordinate[1]*depth
	#i couldn't seem to slice the array to do this in one line. coordinate[0:1] didn't work



	print(coordinate)
	#not sure if this is working as intended, seems to be a tuple in a list - might not be what we want
	



if __name__ == "__main__":
	main()
