#!/usr/bin/env python3

from pulp import *
from math import *
import csvparser as pars

# @summary Calculates values a and b for line of best fit
# @params coordinateX x coordinates for the points
# @params coordinateY y coordinates for the points
# @params minOrMax 0 for minimize problem, 1 for maximize problem
# @return values a and b for the regression line
def calculateBestFit(day, T, minOrMax):

	#define the problem, minimize or maximize
	if minOrMax == 0:
		calculate = LpProblem("calculate", LpMinimize)
	elif minOrMax == 1:
		calculate = LpProblem("calculate", LpMaximize)
	else:
		return -1
	
	#variables to solve for: a and b
	x0 = LpVariable("x0", None, None, LpContinuous)
	x1 = LpVariable("x1", None, None, LpContinuous)
	x2 = LpVariable("x2", None, None, LpContinuous)
	x3 = LpVariable("x3", None, None, LpContinuous)
	x4 = LpVariable("x4", None, None, LpContinuous)
	x5 = LpVariable("x5", None, None, LpContinuous)
	z = LpVariable("z", 0, None, LpContinuous)
	
	# Objective
	calculate += z
	
	###########################################################################################################################################################################
	#    x0 + x1*day[i] + x2*cos((2*pi*day[i])/365.25) + x3*sin((2*pi*day[i])/365.25) + x4*cos((2*pi*day[i])/(365.25*10.7)) + x5*sin((2*pi*day[i])/(365.25*10.7)) - T[i]
	###########################################################################################################################################################################
	#Define the problem and the constraints
	for i in range(len(day)):
		calculate += x0 + x1*day[i] + x2*cos((2*pi*day[i])/365.25) + x3*sin((2*pi*day[i])/365.25) + x4*cos((2*pi*day[i])/(365.25*10.7)) + x5*sin((2*pi*day[i])/(365.25*10.7)) - T[i] <= z
		calculate += x0 + x1*day[i] + x2*cos((2*pi*day[i])/365.25) + x3*sin((2*pi*day[i])/365.25) + x4*cos((2*pi*day[i])/(365.25*10.7)) + x5*sin((2*pi*day[i])/(365.25*10.7)) - T[i] >= -z


	calculate.writeLP("Warm.lp")
	calculate.solve()
	print ("status:", LpStatus[calculate.status])

	for v in calculate.variables():
		print (v.name, "=", v.varValue)

coordinateX = [0,1]
coordinateY = [0,100]

print ("Solution for Corvallis\n")
[T, day] = pars.dataParse()
calculateBestFit(day,T, 0)

print ("Solution for San Diego\n")
[T, day] = pars.OCdataParse()
calculateBestFit(day,T, 0)
