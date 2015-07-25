import math
import time
start = time.clock()
def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

n = 9
m = str(n)

primes = []
for i in range(10,100):
	if (isPrime(i)):
		primes.append(i);

while (len(m)!=9):
	for j in primes:
		if(str(j)[0]==m[len(m)-1]):
			m+=str(j)[1]
			primes.remove(j)
			break
print m
print time.clock() - start, "seconds"