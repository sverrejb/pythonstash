import math
for n in xrange(6,1000000,10):
	s = str(n)
	x = (n % 10)*10**int(math.log10(n)) + int(n / 10)
	if 4*n == x:
		print n
		break