def sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

primes = list(sieve(1000))

ans = 0
for p in primes:
	r = int(str(p)[::-1])
	if (p != r):
		if(r in primes):
			ans+=1
print ans