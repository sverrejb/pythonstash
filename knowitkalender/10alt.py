table = range(1,1501)
while (len(table)!=1):
	if(len(table)%2!=0):
		del table[3::2]
	else:
		del table[1::2]
print table[0]