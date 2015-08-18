import math

def isPrime(x):
	if (x == 2):
		return True
	elif (x % 2) == 0:
		return False
	counter = 3
	while counter <= math.sqrt(x):
		if x % counter == 0:
			return False
		counter += 2
	return True

def isPalindrone(x):
	number = str(x)
	if len(number) % 2 == 0: #even
		divAmount = len(number)//2
	else:
		divAmount = int(len(number)/2)
	for index in range(divAmount):
		if number[index] != number[-(index + 1)]:
			return False
	return True

def numberOfFactors(x):
	counter = 0
	for i in range(1, int(math.sqrt(x)) + 1):
		if (x % i == 0):
			counter += 2
	if (math.sqrt(x) == int(math.sqrt(x))):
		counter -= 1
	return counter

def stringToArray(strIn, rows, columns):
	strIn = strIn.split(" ")
	finalArray = []
	for y in range(rows):
		rowArray = []
		for x in range(columns):
			currentItem = int(strIn[x + y * columns])
			rowArray.append(currentItem)
		finalArray.append(rowArray)
	return finalArray

def sumOfDigits(number):
	arrayOfDigits = list(str(number))
	total = 0
	for item in arrayOfDigits:
		total += int(item)
	return total

def sumDivisors(x):
	total = 0
	for i in range(1, x):
		if x % i == 0:
			total += i
	return total

def fibGenerator():
	yield 0
	yield 1
	curr = 0
	next = 1
	while True:
		yield curr + next
		temp = next
		next += curr
		curr = temp

