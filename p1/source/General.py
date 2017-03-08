#!/usr/bin/python3

import sys
from math import sqrt


#####################################################################

# convert text file to 2d list of points (floats)
def convert(inputfilestring):

	# convert input text file to floats
	fin = open(inputfilestring, 'rt')
	strpnts = fin.readlines(); 
	fin.close()
	
	# 2d list of points
	points=[]
	[points.append(x.split()) for x in strpnts]
	convertedList = [[float(string) for string in inner] for inner in points]
	
	#return list of points
	return(convertedList)

def calcDist(a,b):
	from math import sqrt
	# calculate distance
	dx = float(a[0] - b[0])
	dy = float(a[1] - b[1])
	distance = sqrt(pow(dx,2)+pow(dy,2))   
	return distance
	
#####################################################################

def sortList(convertedList):
	return(sorted(convertedList, key=lambda x: x[0]))

#####################################################################

# print a list of points
def printPoints(list):
	for x in list: print(x[0],x[1])	

# print a list of point pairs
def printPairs(pairs):
	for x in pairs: print(x[0][0],x[0][1],x[1][0],x[1][1])

# write results to file	
def writePairs(dist, pairs, outputfilestring):
	fout = open(outputfilestring,'wt')
	print(dist, file=fout)
	for x in pairs:
		print(x[0][0],x[0][1],x[1][0],x[1][1],file=fout)
	fout.close()
		
#####################################################################

# input number of points, output a list
def genFloats(numoflines):
	from random import random as rand
	floatPoints = []
	for a in range(0,numoflines): floatPoints.append([rand()*100,rand()*100])
	return floatPoints

#####################################################################
	
# split list by xrange
def splitList(points):
	xm = int(len(points)/2)
	a = points[:xm]
	b = points[xm:]
	return (a,b)
		
def getDelta(ad,ap,bd,bp):
		if ad < bd: return (ad,ap)
		elif ad == bd: return(ad,ap+bp)
		else: return(bd,bp)
		
def getPntsInDelta(delta,pointList):
	
	pntsInDelta=[]
	xm = int(len(pointList)/2)
	for x in range(xm,0,-1):
		if (pointList[xm][0]-pointList[x][0]) <= delta:
			pntsInDelta.append(pointList[x])
		else: break
	
	for x in range(xm+1,len(pointList)):
		if (pointList[x][0]-pointList[xm][0]) <= delta:
			pntsInDelta.append(pointList[x])
		else: break
		
	return pntsInDelta
	
	
def sortY(pntsInDelta):
	return(sorted(pntsInDelta, key=lambda y: y[1]))

	


def GetShortestInSortedStrip(pointsInStrip):
	minDistance = float('inf')
	minPointPairs = [[[],[]]]
	for i in range(0, len(pointsInStrip)):
		for j in range(i+1, len(pointsInStrip)):
			if abs(pointsInStrip[i][1] - pointsInStrip[j][1]) > minDistance:
				break
			
			else: 
				#get distance between points
				distance = calcDist(pointsInStrip[i],pointsInStrip[j])

				# decide whether shortest and react
				if distance < minDistance and distance > 0:
					minDistance = distance
					del(minPointPairs[:])
					minPointPairs.append([pointsInStrip[i],pointsInStrip[j]])
				elif distance == minDistance:
					minPointPairs.append([pointsInStrip[i],pointsInStrip[j]])
					
		
	return (minDistance, minPointPairs)	
