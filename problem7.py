import EulerTools

def problem7():
	primesCount = 0
	currPrime = 0
	possibleCount = 2
	while primesCount != 10001:
		if EulerTools.isPrime(possibleCount):
			currPrime = possibleCount
			primesCount += 1
		possibleCount += 1
	return currPrime
