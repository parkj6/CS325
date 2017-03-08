import General as general
import bruteforce as brute
import naive as naiveDivideConquer
import enhanced as enhancedDivideConquer
import time as timer

# summary: produces lists of size numInputs and run each algorithm
# @param numInputs: number of inputs
def measureRunTime(numInputs):
  
  bruteForceTimes = []
  naiveTimes = []
  enhancedTimes = []
    
  for i in range (10):
    testList = general.genFloats(numInputs)

    #start measuring brute force
    start = timer.clock()
    brute.bruteForce(testList)
    end = timer.clock()
    time = end - start
    bruteForceTimes.append(time)

    #start measuring naive
    start = timer.clock()
    testListNaive = general.sortList(testList)
    naiveDivideConquer.naiveDivideConquer(testListNaive)
    end = timer.clock()
    time = end - start
    naiveTimes.append(time)

    #start measuring enhanced
    start = timer.clock()
    ySorted = general.sortY(testList)
    testListEnhanced = general.sortList(testList)
    enhancedDivideConquer.EnhancedDivideConquer(testListEnhanced, ySorted)
    end = timer.clock()
    time = end - start
    enhancedTimes.append(time)

  averageBrute = sum(bruteForceTimes)/len(bruteForceTimes)
  averageNaive = sum(naiveTimes)/len(naiveTimes)
  averageEnhanced = sum(enhancedTimes)/len(enhancedTimes)

  return averageBrute, averageNaive, averageEnhanced

# summary: Test time without running brute force
# @param numInputs: number of inputs
def measureNoBruteForce(numInputs):
  
  naiveTimes = []
  enhancedTimes = []  

  for i in range (10):
    testList = general.genFloats(numInputs)

    #start measuring brute force
    #start = timer.clock()
    #brute.bruteForce(testList)
    #end = timer.clock()
    #time = end - start
    #bruteForceTimes.append(time)

    #start measuring naive
    start = timer.clock()
    testListNaive = general.sortList(testList)
    naiveDivideConquer.naiveDivideConquer(testListNaive)
    end = timer.clock()
    time = end - start
    naiveTimes.append(time)

    #start measuring enhanced
    start = timer.clock()
    ySorted = general.sortY(testList)
    testListEnhanced = general.sortList(testList)
    enhancedDivideConquer.EnhancedDivideConquer(testListEnhanced, ySorted)
    end = timer.clock()
    time = end - start
    enhancedTimes.append(time)

  averageNaive = sum(naiveTimes)/len(naiveTimes)
  averageEnhanced = sum(enhancedTimes)/len(enhancedTimes)

  return averageNaive, averageEnhanced

##############Measuring Average Running Times####################

brute100, naive100, enhanced100 = measureRunTime(100)
brute500, naive500, enhanced500 = measureRunTime(500)
brute1000, naive1000, enhanced1000 = measureRunTime(1000)
brute5000, naive5000, enhanced5000 = measureRunTime(5000)
#brute10000, naive10000, enhanced10000 = measureRunTime(10000)

# don't plot times for brute force for n > 100000 because
# that takes too much time
naive10000, enhanced10000 = measureNoBruteForce(10000)
naive50000, enhanced50000 = measureNoBruteForce(50000)
naive100000, enhanced100000 = measureNoBruteForce(100000)

bruteTimes = [brute100, brute500, brute1000, brute5000]
naiveTimes = [naive100, naive500, naive1000, naive5000, naive10000, naive50000, naive100000]
enhancedTimes = [enhanced100, enhanced500, enhanced1000, enhanced5000, enhanced10000, enhanced50000, enhanced100000]

#write to external file and plot in matlab
bruteFile = open('brutetimes.txt', 'w+')
numInput = [100, 500, 1000, 5000]
arrayElement = 0
for item in bruteTimes:
  bruteFile.write("%s %f\n" % (numInput[arrayElement], item))
  arrayElement = arrayElement + 1
bruteFile.close()

naiveFile = open('naivetimes.txt', 'w+')
numInput = [100, 500, 1000, 5000, 10000, 50000, 100000]
arrayElement = 0
for item in naiveTimes:
  naiveFile.write("%s %f\n" % (numInput[arrayElement], item))
  arrayElement = arrayElement + 1
naiveFile.close()

enhancedFile = open('enhancedtimes.txt', 'w+')
numInput = [100, 500, 1000, 5000, 10000, 50000, 100000]
arrayElement = 0
for item in enhancedTimes:
  enhancedFile.write("%s %f\n" % (numInput[arrayElement], item))
  arrayElement = arrayElement + 1
enhancedFile.close()

print("Done")








