import math
def problem21():
	amicableSum = 0
	for i in range(10000):
		divs = divisors(i)
		if (i == divisors(divs) and i != divs):
			amicableSum += i
	return amicableSum

def divisors(x):
	total = 0
	for i in range(1, x):
		if x % i == 0:
			total += i
	return total
