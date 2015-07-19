ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
edge = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def problem17():
	totalLen = 0
	for i in range(1001):
		totalLen += len(intToWord(i))
	return totalLen

def intToWord(num):
	if (num <= 9):
		return ones[num]
	elif (num > 9 and num <= 19):
		return edge[num - 10]
	elif (num > 19 and num  <= 99):
		tensPlace = num // 10
		onesPlace = num % 10
		return tens[tensPlace] + ones[onesPlace]
	elif (num > 99 and num <= 999):
		hundredsPlace = num // 100
		tensPlace = num // 10 % 10
		onesPlace = num % 10
		if (tensPlace  == 0 and onesPlace == 0):
			andd = ""
		else:
			andd = "and"
		if (tensPlace == 1):
			return ones[hundredsPlace] + "hundred" + andd + edge[onesPlace]
		else:
			return ones[hundredsPlace] + "hundred" + andd + tens[tensPlace] + ones[onesPlace]
	elif (num == 1000):
		return "onethousand"