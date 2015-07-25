def collatz(n, count = 1):
	if n == 1:
		return count
	elif n%2==0:
		result = collatz(n/2, count+1)
		return result
	else:
		result = collatz((3*n)+1, count+1)
		return result

longest = 0
ans = 0
for i in range (1,1000000):
	col = collatz(i)
	if col > longest:
		longest = col
		ans = i
print ans

