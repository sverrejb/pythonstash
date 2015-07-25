for n in xrange(6,1000000,10):
	s = str(n)
	x = int(s[-1:] + s[:-1])
	if 4*n == x:
		print n
		break