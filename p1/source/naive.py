#!/usr/bin/python3

import bruteforce as brute
import General as general

# @summary Finds the smallest distance between two points
# @args points: a sorted list of points
# @return pair: the closest pair and its distance
def naiveDivideConquer(points):
	
  if len(points) <= 3:
    return brute.bruteForce(points);

  middle = int(len(points)/2)
  (bestDistanceLeft, bestPairsLeft) = naiveDivideConquer(points[:middle])
  (bestDistanceRight, bestPairsright) = naiveDivideConquer(points[middle+1:])
   
  (minDistance, minPairs) = general.getDelta(bestDistanceLeft, bestPairsLeft, 
					     bestDistanceRight, bestPairsright)

  hotStripper = general.getPntsInDelta(minDistance, points)

  
  stripSortedByY = general.sortY(hotStripper)
  (stripMinDistance , stripMinPairs) = general.GetShortestInSortedStrip(stripSortedByY)
  return general.getDelta(minDistance, minPairs, 
			  stripMinDistance , stripMinPairs)
  



