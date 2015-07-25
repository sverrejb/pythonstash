import sys
import math
def number_of_divisors(tri):
	ans = 0
	y = 1
	mr = math.sqrt(tri)
	while y <= mr:
	    if tri % y == 0:
	        ans += 2
	    y += 1
	return ans

i = 1
tri = 0
while (True):
	tri = tri + i
	if number_of_divisors(tri)>500:
		print tri
		sys.exit()
	i+=1