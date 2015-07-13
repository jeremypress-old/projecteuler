values = {}
def problem15():
	for y in range (21):
		for x in range(21):
			if x == 0 and y == 0:
				values[(y , x)] = 0
			elif (x == 0 and y == 1 or x == 1 and y == 0):
				values[(x, y)] = 1
			elif (x == 0):
				values[(x , y)] = values[(x, y - 1)]
			elif (y == 0):
				values[(x , y)] = values[(x - 1, y)]
			else:
				values[(x, y)] = values[(x, y - 1)] + values[(x - 1, y)]
	return values[(20, 20)]

