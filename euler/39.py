def is_orthogonal(a,b,c,):
	li = [a,b,c]
	li.sort()
	li = [x**2 for x in li]
	return li[0]+li[1]==li[2]
	
def number_of_solutions(i):
	ans = 0
	for a in range (1,i/2):
		for b in range (a,i/2):
			c = int((a**2+b**2)**0.5)
			if (a+b+c == i) and (is_orthogonal(a,b,c)):
				ans += 1
	return ans

ans = 0
biggest = 0

for i in range (0, 1000):
	val = number_of_solutions(i) 
	if val  > biggest:
		biggest = val
		ans = i
print ans
print biggest