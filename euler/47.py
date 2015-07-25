def num_of_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return len(set(factors))

i = 0
ans = 0
while ans == 0:
	i+=1
	seq = []
	j = 0
	if num_of_factors(j in range (i, i+4)) == 4:
		ans = i

print ans