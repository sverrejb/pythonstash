def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 1
i = 1
ans = 0
while (i<4000000):
	i = fib(n)
	n+=1
	if(i%2==0):
		ans += i
print ans