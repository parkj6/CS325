import csv

# @summary Parse csv and get average temperature per day
# @return AvgTemp average temperature per day
# @return day  
def dataParse():
	list = []
	with open('Corvallis.csv', 'r') as file:
		line = csv.reader(file, delimiter = ';')
	
		for row in line:
			list.append(row)
	
	avgTemp = []
	day = []
	
	for i in range(1, len(list)):
		avgTemp.append((float)(list[i][7]))
		day.append((int)(list[i][8]))
		
	list = list[1:]
	day = day[1:]
	return avgTemp, day

	#######################################################
	
def OCdataParse():
	list = []
	with open('sandiego.csv', 'r') as file:
		line = csv.reader(file, delimiter = ',')
	
		for row in line:
			list.append(row)
	
	avgTemp = []
	day = []
	
	for i in range(1, len(list)):
		avgTemp.append((((float)(list[i][3]))-32)*(5/9))
		day.append((int)(list[i][4]))
		
	list = list[1:]
	day = day[1:]
	return avgTemp, day











	
#parsing example
#[avgTemp, day] = dataParse()
#print(avgTemp)
#print(day)

		