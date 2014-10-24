def problem2(x):
	finalSum = 2
	currNumber = 1
	nextNumber = 2
	while True:
		if nextNumber > x:
			break
		temp = nextNumber
		nextNumber += currNumber
		currNumber = temp
		if nextNumber % 2 == 0:
			finalSum += nextNumber
	return finalSum

print problem2(4000000)