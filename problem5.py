def problem5():
	counter = 20 #small lower bound
	while True:
		print(counter)
		if isDivBy20(counter):
			return counter
		else:
			counter += 20 #has to be even

def isDivBy20(x):
	for value in range(1 , 21):
		if x % value != 0:
			return False
	return True

