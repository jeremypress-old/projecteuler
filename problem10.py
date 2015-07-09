import EulerTools
def problem10():
	total = 0
	for x in range(2, 2000000):
		if EulerTools.isPrime(x):
			total += x
	return total
