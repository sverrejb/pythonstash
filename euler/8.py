with open('8number.txt') as myFile: 
	data = myFile.read()
l = map(int, filter(lambda a: a != '\n', list(data)))
ans = []
for i in range(len(l)-14):
	ans.append(reduce(lambda x, y: x*y, l[i:i+13]))
print max(ans)