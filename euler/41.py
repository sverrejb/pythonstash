import itertools
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

ans = 0
string = ""
array = []
for i in range (1,10):
	string  +=  str(i)
	array.append(string)

array.reverse()

for num in array:
	a = list(map("".join, itertools.permutations(num)))
	a.reverse()
	for i in a:
		j = int(i)
		if is_prime(j) and i>ans:
			ans = i

print ans