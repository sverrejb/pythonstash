def has_prop(n):
	nums = {}
	while n!=1:
		if n in nums:
			return False
		nums[n] = True
		n = sum(map(lambda x: int(x)**2, str(n)))
	return True

for i in range (1,51):
	if has_prop(i):
		print "{},".format(i),