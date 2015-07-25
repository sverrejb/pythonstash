import itertools

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def is_perms(i,j,x):
	sor_i = ''.join(sorted(str(i)))
	sor_j = ''.join(sorted(str(j)))
	sor_x = ''.join(sorted(str(x)))
	if sor_i == sor_j == sor_x:
		print i
		print j
		print x
		return True

for i in range (1000,10000):
	if is_prime(i):
		j = i + 3330
		if is_prime(j):
			x = j+3330
			if is_prime(x) and is_perms(i,j,x):
				print str(i)+str(j)+str(x)


