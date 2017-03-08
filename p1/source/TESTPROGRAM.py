#!/usr/bin/python3
import General as general	# helper functions for all
from bruteforce import bruteForce 	# brute force algo
from naive import naiveDivideConquer 	# naive D&C algo
from enhanced import EnhancedDivideConquer 	# enhanced D&C algo




#####EXAMPLE PROGRAM RUNS INSTANCE OF EACH ALGO#####
print("\n\n\n")#GIMME SOME SPACE





# Declare number of points to run algo on
x = (general.genFloats(5000))


#BRUTE#FORCE#
################BRUTE#FORCE########################
print("STARTING BRUTE FORCE ALGO:")
(shortestDistance, listOfShortestPoints) = bruteForce(x)
#printing results ....
print("Shortest Distance :",shortestDistance)
print("Closest Points:")
general.printPairs(listOfShortestPoints)
print("\n\n")
####################################################

#NAIEVE#D&C#
################NAIEVE#D&C##########################
print("STARTING NAIEVE D&C:")
x = general.sortList(x)
(shortestDistance, listOfShortestPoints) = naiveDivideConquer(x)
#printing results ....
print("Shortest Distance :",shortestDistance)
print("Closest Points:")
general.printPairs(listOfShortestPoints)
print("\n\n")
####################################################

#ENHANCED#D&C#
################ENHANCED#D&C########################
print("STARTING ENHANCED D&C")
x = general.sortList(x)
y = general.sortY(x)
(shortestDistance, listOfShortestPoints) = EnhancedDivideConquer(x,y)
#printing results ....
print("Shortest Distance :",shortestDistance)
print("Closest Points:")
general.printPairs(listOfShortestPoints)
print("\n\n")
####################################################




