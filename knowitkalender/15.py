def same_chars(s,n):
	return sorted(n) == sorted(s)

def divisors(x,y):
	return not (x % 10 == 0 and y % 10 == 0);

ans = []
for x in range(10,100):
	for y in range (10,100):
		s = str(x)+str(y)
		n = str(x*y)
		if(len(n)==4 and same_chars(s,n) and divisors(x,y)):
			ans.append(int(n))
print len(set(ans))