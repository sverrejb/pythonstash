ans = 0
with open("names.txt") as data:
	names = sorted(data.read().replace('"', "").split(','))
	
	i = 1
	for name in names:
		sum = 0
		for c in name:
			sum += ord(c)-64
		ans += sum * i
		i+=1
print ans