def problem4():
	palindroneList = []
	number1 = 999
	while number1 > 0:
		print(number1)
		number2 = 999
		while number2 > 0:
			if isPalindrone(number1 * number2):
				palindroneList.append(number1 * number2)
			number2 -= 1
		number1 -= 1
	return max(palindroneList)

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