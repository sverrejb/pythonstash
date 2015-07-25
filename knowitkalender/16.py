import sys
for i in range (10000):
	x = 2**i
	if "472047" in str(x):
		print i
		sys.exit()