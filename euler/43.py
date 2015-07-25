import itertools

#UGLY SHITE METHOD. USE 
def is_special(j):
	if int(j[1]+j[2]+j[3]) % 2 != 0:
		return False
	if int(j[2]+j[3]+j[4]) % 3 != 0:
		return False
	if int(j[3]+j[4]+j[5]) % 5 != 0:
		return False
	if int(j[4]+j[5]+j[6]) % 7 != 0:
		return False
	if int(j[5]+j[6]+j[7]) % 11 != 0:
		return False
	if int(j[6]+j[7]+j[8]) % 13 != 0:
		return False
	if int(j[7]+j[8]+j[9]) % 17 != 0:
		return False
	return True




a = list(map("".join, itertools.permutations("0123456789")))

test = "1406357289"

print is_special(test)

print 

ans = 0
for i in a:
	if is_special(i):
		ans += int(i)

print ans