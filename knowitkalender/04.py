f = open('data2.txt', 'r')
lowest = 0.0
ans = ""
for line in f:
	try:
		linesplit = line.split()
		tmp = float(linesplit[3].replace(',','.'))
		month = int(linesplit[1][3:5])
		if tmp < lowest and month == 12:
			lowest = tmp
			ans = line
	except:
		pass
print ans.split()[1]