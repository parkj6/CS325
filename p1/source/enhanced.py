#!/usr/bin/python3

import bruteforce as brute
import General as general

# @summary Finds the smallest distance between two points
# @args points: a sorted list of points
# @return pair: the closest pair and its distance
def EnhancedDivideConquer(points, sortedByY):
	
  if len(points) <= 3:
    return brute.bruteForce(points);
	
######################################################
  middle = int(len(points)/2)
  midVal = points[middle][0]
	
  sortedByYLeft = []
  sortedByYRight = []
  for x in  sortedByY:
    if x[0] <= midVal: sortedByYLeft.append(x)
    else: sortedByYRight.append(x)

  


######################################################
	
	
	


  (bestDistanceLeft, bestPairsLeft) = EnhancedDivideConquer(points[:middle], sortedByYLeft)
  (bestDistanceRight, bestPairsright) = EnhancedDivideConquer(points[middle+1:], sortedByYRight)
   
  (minDistance, minPairs) = general.getDelta(bestDistanceLeft, bestPairsLeft, 
					     bestDistanceRight, bestPairsright)

  #hotStripper = general.getPntsInDelta(minDistance, points)

  stripSortedByY = []
  for x in sortedByY:
    if x[0] >= (midVal-minDistance) and x[0] <= (midVal+minDistance): stripSortedByY.append(x)
	
  
  
  (stripMinDistance , stripMinPairs) = general.GetShortestInSortedStrip(stripSortedByY)
  return general.getDelta(minDistance, minPairs, 
			  stripMinDistance , stripMinPairs)
  






