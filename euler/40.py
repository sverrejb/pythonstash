max_value = 1000000
frac = ""
for i in range (1, max_value):
	frac+= str(i)

ans = 1
for i in range (1,7):
	ans *= int(frac[(10**i)-1])
print ans