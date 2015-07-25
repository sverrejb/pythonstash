def cut(n):
	result = []
	for i in range(1,len(n)):
		result.append((int(n[0:i]),int(n[i:len(n)])))
	return result

def has_prop(n):
	parts = cut(str(n))
	for p in parts:
		if sum(p)**2 == n:
			return True
	return False

ans = 0
for i in range(1000000):
	if has_prop(i):
		ans+=1
print ans