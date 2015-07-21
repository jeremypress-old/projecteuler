from itertools import permutations
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def problem24():
	counter = 1
	for permutation in permutations(digits):
		print(counter)
		if (counter == 1000000):
			return permutation
		counter += 1