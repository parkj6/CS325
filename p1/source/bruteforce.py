#!/usr/bin/python3

import General as general

#####################################################################

# takes a 2d array of points and finds the minimum distance
# returns the minimum distance (bd) and the list of points (bp)
def bruteForce(convertedList):
	from math import sqrt
	
	# variables for keeping track (best distance, best points)
	bestDistance = float('inf') # first entry will be distance
	bestPositions = []

	# loops for every combination
	for a in range(0,len(convertedList)):
		for b in range(a,len(convertedList)):
			
			#get distance between points
			distance = general.calcDist(convertedList[a],convertedList[b])

			# decide whether shortest and react
			if distance < bestDistance and distance > 0:
				bestDistance = distance
				del(bestPositions[:])
				bestPositions.append([convertedList[a],convertedList[b]])
			elif distance == bestDistance:
				bestPositions.append([convertedList[a],convertedList[b]])

	return(bestDistance, bestPositions) #best distance and best points list
