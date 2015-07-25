ans = 0
for i in xrange(1, 1000):
    x = str(i**2)
    for j in xrange(1, len(x)):
        if int(x[:j]) + int(x[j:]) == i:
            ans += 1
print ans