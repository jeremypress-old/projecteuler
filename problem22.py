import string
score = dict(zip(string.ascii_lowercase, range(1, 27)))
f = open('files/names.txt', 'r')
names = f.read().split(",")
for i in range(len(names)):
	names[i] = names[i].strip('"').lower()
names.sort()

def problem22():
	total = 0
	for i in range(len(names)):
		wordScore = 0
		for letter in names[i]:
			wordScore += score[letter]
		total += wordScore * (i + 1)
	return total

