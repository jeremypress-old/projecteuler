def problem6(x):
	return squareOfSums(x) - sumOfSquares(x)

def squareOfSums(x):
	count = sum(range(x + 1))
	return count * count

def sumOfSquares(x):
	count = 0
	for number in range(x + 1):
		count += number * number
	return count