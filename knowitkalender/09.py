import sys
import time
start = time.clock()
def is_pan(n):
	if ''.join(sorted(n)) == '0123456789':
		return True
for i in range(200,501):
	for j in range(500,1000):
		s = i+j
		if(1000<=s<=9999):
			if(is_pan("{}{}{}".format(i,j,s))):
				print i
				print time.clock() - start
				sys.exit()