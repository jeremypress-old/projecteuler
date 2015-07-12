import EulerTools

def problem12():
	i = 1
	triangleNumber = 0
	while True:
		triangleNumber += i
		numFactors = EulerTools.numberOfFactors(triangleNumber)
		print (numFactors)
		if (numFactors) >= 500:
			return triangleNumber
		i += 1
