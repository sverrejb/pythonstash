def has_prop(n):
	while n!=1:
		if n == 4:
			return False
		n = sum(map(lambda x: int(x)**2, str(n)))
	return True

for i in range (1,51):
	if has_prop(i):
		print "{},".format(i),