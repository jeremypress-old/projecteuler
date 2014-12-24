def problem7(x):
	primesCount = 0
	currPrime = 0
	possibleCount = 2
	while primesCount != x - 1:
		print(primesCount)
		if isPrime(possibleCount):
			currPrime = possibleCount
			primesCount += 1
		possibleCount += 1
	return currPrime

def isPrime(x):
	if x % 2 == 0:
		return False
	counter = 3
	while counter <= x - 1:
		if x % counter == 0:
			return False
		counter += 2
	return True