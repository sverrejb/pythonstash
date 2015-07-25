n, ans = 8001, []
for i in range(1,n):
	for j in range(1,i):
		ans.append(i*j)
print len(set(ans))