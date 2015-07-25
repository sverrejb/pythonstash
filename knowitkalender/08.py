import time
start_time = time.clock()
def sum_of_divisors_equals_self(n):
	sum = 1
	for i in xrange(2,int(n**0.5)+1):
		if (n%i==0):
			sum+=i + n/i
			if (sum>n):
				return False
	return sum == n
for i in xrange (2,10000):
	if(sum_of_divisors_equals_self(i)):
		print "{},".format(i),
print
print time.clock() - start_time