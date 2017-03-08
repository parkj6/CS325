#!/usr/python
import sys
from random import random as rand

numoflines = int(sys.argv[1])
outputfilestring = str(sys.argv[2])
fout = open(outputfilestring, 'wt')
for a in range(0,numoflines):
    x = rand()*100  
    y = rand()*100
    print(x, y, file=fout)
fout.close() 
 
