def allowed(n):
	allowed_chars = ['0','1','6','8','9']
	for i in str(n):
		if i not in allowed_chars:
			return False
	return True

def equals_flip(n):
	return int(str(n).replace('6', '%temp%').replace('9', '6').replace('%temp%', '9')[::-1])==n	

ans = 0
for i in range(0,100000):
	if allowed(i) and equals_flip(i):
		ans += 1
print ans