import time
start_time = time.clock()
n = 13
m = str(n)
primes = [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

while (len(m)!=n):
	for i in primes:
		if(str(i)[0]==m[len(m)-1]):
			m+=str(i)[1]
			primes.remove(i)
			break
print m
print time.clock() - start_time, "seconds"