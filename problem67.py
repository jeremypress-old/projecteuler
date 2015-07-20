values = {}
pyramid = []
f = open('files/triangle.txt', 'r')
for line in f:
	row = list(line.split(' '))
	for i in range(len(row)):
		row[i] = int(row[i])
	pyramid.append(row)
print(pyramid)
values[(0, 0)] = pyramid[0][0]
def problem67():
	bestVal = 0
	for row in range(1, len(pyramid)):
		for item in range(len(pyramid[row])):
			print(row, item)
			if (item == 0): #left edge
				values[(row, item)] = pyramid[row][item] + values[(row - 1, item)]
			elif (item == row): #right edge
				values[(row, item)] = pyramid[row][item] + values[(row - 1, item - 1)]
			else:
				values[(row, item)] = pyramid[row][item] + max(values[(row - 1, item - 1)], values[(row - 1, item)])
	bottomRow = len(pyramid) - 1
	for i in range(bottomRow):
		bestVal = max(bestVal, values[(bottomRow, i)])
	return bestVal