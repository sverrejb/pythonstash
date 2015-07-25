import operator
f = open("words.txt", "r+")
ans = {}
for l in f:
	l = "".join(sorted(l.lower()))
	ans[l] = ans.get(l, 0) + 1
f.close()
print max(ans.iteritems(), key=operator.itemgetter(1))[0]