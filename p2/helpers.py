#!/usr/bin/python3



###################################################################
##	Using the comp function will calculate the edit distance of
## two strings and output the altered strings. Values are returned
## in the form of:
##
##	[str=OutputString1,str=OuptutString2,int=Editdistance] 
##
## Inputs are in the form :
##			
##	comp(str=InputString1, str=InputString2)
##
###################################################################

def comp(string1, string2):

	# turn imput strings into lists
	str1 = list(string1)
	str2 = list(string2)

	# puts fake NULL into strings and generates/initalizes utility arrays
	[str1, str2, EditArr, DirectionArr] = GenArrays(str1,str2)

	# fills utility arrays
	[EditArr, DirectionArr] = CalcArrays(str1, str2, EditArr, DirectionArr)
	
	# generate backtrace list
	TraceArr = GenBackTrace(str1, str2, DirectionArr)

	# generate the put strings
	[OutString1, OutString2] = GenOutputStrs(str1, str2, TraceArr)

	# get min edit distance
	minDist = EditArr[len(str2)-1][len(str1)-1]

	# convert list of chars to strings
	Out1 = char2str(OutString1)
	Out2 = char2str(OutString2)
	
	# return strings of altered inputs and the min edit distance
	return [Out1, Out2, minDist]

###################################################################
###################################################################




####################################################################
######################	   Helper Functions		####################
####################################################################



#######################	  Gen Arrs	  ########################
def GenArrays(str1, str2):
	
	# prepend '-' char to each string
	str1.insert(0,'-')	  
	str2.insert(0,'-')	
	
	# generateCost matrix
	costMatrix = CostMatrixGen() 

	# declare utility arrays
	EditArr = [[0 for x in range(0,len(str1))] for y in range(0,len(str2))]	 
	DirectionArr = [['x' for x in range(0,len(str1))] for y in range(0,len(str2))]

	# utility Array base cases
	EditArr[0][0] = 0
	DirectionArr[0][0] = 'U'	

	# Initialize utility arrays (first row first column)
	for j in range(1,len(str1)):
		EditArr[0][j] = EditArr[0][j-1] + penaltyLookUp(str1[j], '-', costMatrix)
	DirectionArr[0][j] = 'L'		
	for i in range(1,len(str2)):
		EditArr[i][0] = EditArr[i-1][0] + penaltyLookUp(str2[i], '-', costMatrix)
		DirectionArr[i][0] = 'U'
	# return prepended strings, EditArr, (resulting costs), DirectionArr (where it came from)	
	return [str1, str2, EditArr, DirectionArr]

	

#######################		CalcArrays	  ########################
def CalcArrays(str1, str2, EditArr, DirectionArr):
	
	# generate cost matrix from file
	costMatrix = CostMatrixGen()

	# embedded for loops fill arrays
	for i in range(1,len(str2)):
		for j in range(1,len(str1)):

					# calculations for min comparison (Up, Diagonal, Left)
			U = EditArr[i-1][j] +  penaltyLookUp(str2[i], '-', costMatrix)
			D = EditArr[i-1][j-1] + penaltyLookUp(str1[j], str2[i], costMatrix)
			L = EditArr[i][j-1] + penaltyLookUp(str1[j], '-',  costMatrix)
			
					# set value of EditArr (Up, Diagonal, Left)
			EditArr[i][j] = min(U,D,L)
			
			# set value for backtrace array (DirectionArr)
			if(EditArr[i][j] == U): DirectionArr[i][j] = 'U'
			elif(EditArr[i][j] == L): DirectionArr[i][j] = 'L'
			elif(EditArr[i][j] == D): DirectionArr[i][j] = 'D'
			else: 
				print("Failed Miserably")
				exit()

		# return filled utility arrays
	return [EditArr, DirectionArr]




#######################	   Generate Backtrace  ###################### 
def GenBackTrace(str1, str2, DirectionArr):
	
	# initalize iterators
	i = len(str2)-1
	j = len(str1)-1

	# holds a list of characters dipecting backtrace	
	TraceArr = []

	# obtain reverse trace list
	while(1):

		# if at inital index
		if((i==0) and (j==0)): break
		
		# add direction value at location
		TraceArr.append(DirectionArr[i][j])

		# alter itterator values based on result
		if(DirectionArr[i][j] == 'U'): i = i-1
		elif(DirectionArr[i][j] == 'D'): i = i-1; j = j-1
		elif(DirectionArr[i][j] == 'L'): j = j-1
		else: 
			print("Failed Miserably")
		exit()

	# reverse the list for string generation orientation
	rTraceArr = []
	for x in range(0,len(TraceArr)): rTraceArr.insert(0,TraceArr[x])
	
	#printArr(DirectionArr)
	
	# returns the trace in correct order
	return rTraceArr



######################### Generate Output Strings ##################### 
def GenOutputStrs(str1, str2, TraceArr):

	# declare output strings
	OutString1 = []
	OutString2 = []

	# declare itterators
	S1 = 1 
	S2 = 1 
	
	# loop that calculates the values of the output strings
	for x in range(0, len(TraceArr)):
		
		# the motherfuckin shit!
		if(TraceArr[x] == 'U'): # came from above (insert)
			OutString1.append('-')
			OutString2.append(str2[S2])
			S2 = S2+1
		elif(TraceArr[x] == 'D'): # came from the diagonal (align)
			OutString1.append(str1[S1])
			OutString2.append(str2[S2])
			S1 = S1+1
			S2 = S2+1
		else:
			OutString1.append(str1[S1]) # came from the left (delete)
			OutString2.append('-')
			S1 = S1+1
	
	# return the calculated output strings
	return [OutString1, OutString2]

	
# create a matrix with the cost of every action
def CostMatrixGen():
	costMatrix = [] # initalize
	with open("imp2cost.txt", "r") as cost: # hard coded input cost file
		for line in cost:
			rowList = line.split(',')
			rowList[-1] = rowList[-1].strip()
			costMatrix.append(rowList)
	return costMatrix
	

# look up cost based on pre loaded cost matrix file
def penaltyLookUp(letter1, letter2, costMatrix):
	i = 0
	j = 0
	
	for x in range(0,len(costMatrix)):
		if(letter1 == costMatrix[x][0]): i =x
	for y in range(0,len(costMatrix)):
		if(letter2 ==  costMatrix[0][y]): j = y

	# return	
	return int(costMatrix[i][j])
	
def calcResult(str1,str2):
	s1 = list(str1)
	s2 = list(str2)
	
	costMatrix = CostMatrixGen()

	score = 0
	for x in range(0, len(str1)):
		score = score + penaltyLookUp(s1[x],s2[x],costMatrix)
				
	return score

	
# convert list of chars to string
def char2str(listOchars):
	string = ''
	for x in range(0, len(listOchars)):
		string = string + listOchars[x]
	return string
	

# Helper function to print 2D arrays
def printArr(arr):
	for x in range(0, len(arr)):
		print(arr[x])
		


# Test Example 

'''
costM = CostMatrixGen()
printArr(costM)
[O1, O2, D] = comp("CCACTGACATAAGCCTCTGCGTTC","TCATGACATGTGCCGCTCACCGTGACTATAGACTCTCAGCAATGGTTAAAGAATCAGCCCGCCAATAGGGGCGGCAAATAATACCGCTGC")
print(O1, ',', O2, ':', D)
print("\n\n")
print("Calculation of score based on output:",calcResult(O1,O2))
print("\n\n")
'''
