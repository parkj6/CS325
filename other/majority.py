def majority(data, tiebreaker =None): # complete code, with testing, in majority.py
	'''Return the majority element of sequence data, OR
	tiebreaker - if exactly half of the elements in data are tiebreaker , OR
	None otherwise.
	'''
	n = len(data)
	if n == 0:
		return tiebreaker
	pairs = [] # empty list
	if n % 2 == 1:
		tiebreaker = data[-1] # last element in Python sequence
	for i in range(0, n-1, 2): # for(i = 0; i < n-1; i+=2)
		if data[i] == data[i+1]:
			pairs.append(data[i])
			major = majority(pairs, tiebreaker )
		if major is None:
			return None
		nMajor = data.count(major) # handy method does the obvious
		if 2*nMajor > n or (2*nMajor == n and major == tiebreaker ):
			return major
	return None # candidate did not pan out
