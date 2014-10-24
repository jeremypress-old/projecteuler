def problem1(x):
	finalSum = 0
	for number in range(x):
		if number % 3 == 0 or number % 5 == 0:
			finalSum += number
	return finalSum

print problem1(1000)