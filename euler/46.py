def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True	

def goldbach(n):
	#sjekke alle primtal som er mindre enn n
	primes = []
	for i in range (1, n):
		if is_prime(i):
			primes.append(i)
	for p in primes:
		for j in range (1, n-p):
			if p+(2*(j**2)) == n:
				return True

i = 1
ans = 0
while ans == 0:
	i+=2
	if not is_prime(i) and not goldbach(i):
		print i
print ans