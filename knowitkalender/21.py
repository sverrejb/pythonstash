f = open("21words.txt","r+")

wl = map(lambda x: x.strip(), f.readlines())
ans = []
for w in wl:
	s = 0
	for c in w:
		s+= ord(c)
	ans.append(s)

print sum(sorted(ans)[::-1][0:42])