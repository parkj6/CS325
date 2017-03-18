#!/usr/bin/python3


# import the helper functions
import helpers as edit


# declare the input and output file names
InFileName = "imp2input.txt"
OutFileName = "imp2output.txt"

# open input and output files
inFile = open(InFileName, "r" )
outFile = open(OutFileName, "w")

# declare line variable
line = "1"

# loop to pull in lines form file
while True:
	
	# pull in line
	line = inFile.readline()

	# break at end of file
	if line == '': break

	# split the line
	twoStrings = line.split(",")
	
	# set the strings
	one = twoStrings[0][:]
	two = twoStrings[1][:-1]

	###################################
	###   calculate edit distance   ###
	[O1, O2, D] = edit.comp(one, two)
	###################################
	
	# create output string
	outputLine = O1 + ',' + O2 + ':' + str(D)
	
	# write output string to file
	outFile.write(outputLine)
	outFile.write('\n')

# close i/o
inFile.close()
outFile.close()



