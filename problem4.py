import EulerTools
def problem4():
	palindroneList = []
	number1 = 999
	while number1 > 0:
		number2 = 999
		while number2 > 0:
			if EulerTools.isPalindrone(number1 * number2):
				palindroneList.append(number1 * number2)
			number2 -= 1
		number1 -= 1
	return max(palindroneList)
