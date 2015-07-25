f = open("15number.txt", "r+")
sum = 0
for l in f:
	sum += int(l)
print str(sum)[:10]