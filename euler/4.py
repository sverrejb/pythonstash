def isPalindrome(s):
    return s == s[::-1]
ans = []
for i in range(100,1000):
	for j in range (100,1000):
		if (isPalindrome(str(i*j))):
			ans.append(i*j)
print max(ans)