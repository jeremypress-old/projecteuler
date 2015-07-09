def problem6():
	return squareOfSums(100) - sumOfSquares(100)

def squareOfSums(x):
	count = sum(range(x + 1))
	return count * count

def sumOfSquares(x):
	count = 0
	for number in range(x + 1):
		count += number * number
	return count