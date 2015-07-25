from itertools import permutations
ans = float("inf")
def prime(n):
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
    return max(factors)

perms = [''.join(p) for p in permutations('123456789')]
array = []

for p in perms:
    array.append(int(p))
print len(array)
for perm in array:
	b = prime(perm)
	if (b<ans):
		ans = b
print ans