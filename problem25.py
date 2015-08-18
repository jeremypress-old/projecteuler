import EulerTools

def problem25():
	currFibNumber = EulerTools.fibGenerator()
	nextFib = next(currFibNumber)
	count = 0
	while len(str(nextFib)) < 1000:
		print(nextFib)
		count += 1
		nextFib = next(currFibNumber)
	return count