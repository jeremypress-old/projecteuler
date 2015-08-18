import math
import EulerTools
def problem21():
	amicableSum = 0
	for i in range(10000):
		divs = EulerTools.sumDivisors(i)
		if (i == EulerTools.sumDivisors(divs) and i != divs):
			amicableSum += i
	return amicableSum

