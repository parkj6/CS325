#!/usr/bin/env python

from pulp import *

# @summary Calculates values a and b for line of best fit
# @params coordinateX x coordinates for the points
# @params coordinateY y coordinates for the points
# @params minOrMax 0 for minimize problem, 1 for maximize problem
# @return values a and b for the regression line
def calculateBestFit(coordinateX, coordinateY, minOrMax):

	#define the problem, minimize or maximize
	if minOrMax == 0:
		calculate = LpProblem("calculate", LpMinimize)
	elif minOrMax == 1:
		calculate = LpProblem("calculate", LpMaximize)
	else:
		return -1
	
	#variables to solve for: a and b
	a = LpVariable("a", 0, None, LpContinuous) 
	b = LpVariable("b", 0, None, LpContinuous)

	#Define the problem and the constraints
	for i in range(len(coordinateX)):
		calculate += a*coordinateX[i]+b-coordinateY[i]
		calculate += a*coordinateX[i]+b-coordinateY[i] <= coordinateY[i]-(a*coordinateX[i]+b) #a*coordinateX[i]+b-coordinateY[i], been trying out different bounds
		calculate += -a*coordinateX[i]-b+coordinateY[i] <= coordinateY[i]-(a*coordinateX[i]+b)

	calculate.writeLP("WarmUp.lp")
	calculate.solve()
	print ("status:", LpStatus[calculate.status])

	for v in calculate.variables():
		print (v.name, "=", v.varValue)
	print("maximum =", value(calculate.objective))
	print(calculate.constraints)
	
coordinateX = [1,2,3,5,7,8,10]
coordinateY = [3,5,7,11,14,15,19]
calculateBestFit(coordinateX, coordinateY, 1)