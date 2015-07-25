def d(n):
	sum = 1
	for i in xrange(2,int(n**0.5)+1):
		if (n%i==0):
			sum+=i + n/i
	return sum

ans = 0
for i in range (1,10001):
	a = d(i)
	b = d(a)
	if b==i and i != a:
		ans += a+b
print ans/2