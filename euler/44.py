def is_pent(n):
		return ((24*n+1)**0.5+1)/6.0 % 1 == 0
ans = 0
i = 1
pents = []
while ans == 0:
	i+=1
	p1 = (i*((3*i)-1))/2
	pents.append(p1)
	for c in pents	:
		if is_pent(p1+c) and is_pent(p1-c):
			ans = min(abs(p1-c),abs(c-p1))
print ans
