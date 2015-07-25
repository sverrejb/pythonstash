from datetime import datetime
startTime = datetime.now()

i = 285
ans = 0
pents = set()
hexes = set()

while ans == 0:
	i += 1 
	tri = i*(i+1)/2
	pents.add(i*(3*i-1)/2)
	hexes.add(i*(2*i-1))
	if tri in hexes and tri in pents:
		ans = tri
print ans
print(datetime.now()-startTime)