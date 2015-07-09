import EulerTools
import math
def problem3():
	counter = int(math.sqrt(600851475143))
	while counter > 0:
		print(counter)
		if 600851475143 % counter == 0:
			if EulerTools.isPrime(counter):
				return counter
		counter -= 1
