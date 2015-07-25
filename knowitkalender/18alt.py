ans = {}
with open("words.txt") as f: 
    l = ["".join(sorted(x.lower().strip())) for x in f.readlines()]
    for t in l:
    	ans[t] = ans.get(t, 0) + 1
print max(ans, key=ans.get)