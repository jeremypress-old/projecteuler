import math
def problem3(original):
	count = int(x**0.5) #start at the square root, have to check both factors of the numbers 
	while count > 0:
		otherFactor = int(original / x)
		if orig % x == 0:
			if isPrime(x):
				return x
		elif orig % otherFactor == 0: #checking the other potential factor
			if isPrime(otherFactor) == 0:
				return x
		x -= 1

def isPrime(x):
	if x % 2 == 0:
		return False
	counter = 3
	while counter <= x - 1:
		if x % counter == 0:
			return False
		counter += 2
	return True

print problem3(600851475143)