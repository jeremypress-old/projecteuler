def collatzCounter(n):
	if n == 0:
		return 0
	counter = 1 #the original number counts in the length
	while n != 1:
		if (n % 2 == 0):
			n /= 2
		else:
			n = 3 * n + 1
		counter += 1
	counter += 1 #they count reaching 1 as part of the length
	return counter + 1

def problem14():
	maxLength = 0
	maxNumber = 0
	for i in range(1000000):
		print(i)
		currentLength = collatzCounter(i)
		if (currentLength > maxLength):
			maxLength = collatzCounter(i)
			maxNumber = i
	return maxNumber