def problem2():
	finalSum = 2
	currNumber = 1
	nextNumber = 2
	while True:
		if nextNumber > 4000000:
			break
		temp = nextNumber
		nextNumber += currNumber
		currNumber = temp
		if nextNumber % 2 == 0:
			finalSum += nextNumber
	return finalSum
