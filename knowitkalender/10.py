table = range(1,1501)
while (len(table)!=1):
	last = max(table)
	del table[1::2]
	if (last in table):
		del table[0]
print table[0]