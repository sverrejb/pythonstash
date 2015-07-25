import math
def sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

primes = list(sieve(10000000))
numbers = [541, 41, 17, 7]
matrix = [[] for i in range(len(numbers))]

for n in numbers:
	for i in range(len(primes)-n+1):
		x = sum(primes[i:i+n])
		if (x>10000000):
			break
		matrix[numbers.index(n)].append(x)

ans = set(matrix[0])
for i in range(1,len(matrix)):
	ans = ans.intersection(set(matrix[i])) 
print min(ans)	