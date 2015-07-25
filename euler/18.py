sums = []
with open("18triangle.txt") as data:
	triangle = data.readlines()
	triangle = map(lambda x: x.strip('\n'), triangle)
	triangle = map(lambda x: x.split(), triangle)
	triangle = map(lambda x: map(int, x), triangle)

def traverse(sum = 0, pos = 0, counter = 0):
	if counter == len(triangle):
		sums.append(sum)
		return True
	x = triangle[counter][pos]
	traverse(sum + x, pos , counter + 1)
	traverse(sum + x, pos +1, counter +1)

traverse()
print max(sums)