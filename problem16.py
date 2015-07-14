def problem16():
	arrayOfDigits = list(str(2**1000))
	total = 0
	for item in arrayOfDigits:
		total += int(item)
	return total