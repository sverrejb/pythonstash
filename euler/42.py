def tri(i):
	return int((0.5*i)*(i+1))

def is_triangle(w):
	for i in range (0, 10000):
		if tri(i) > w:
			return False
		if tri(i) == w:
			return True

def word_value(w):
	val = 0
	for c in w:
		val += (ord(c)-64)
	return val

with open("words.txt") as myFile: 
    data = myFile.read().split(",")
data = ([s.replace('"', '') for s in data])

ans = 0

for a in data:
	if is_triangle(word_value(a)):
		ans += 1

print ans
