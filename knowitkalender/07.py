from PIL import Image
from collections import Counter
im = Image.open("Santa.png")
pix = im.load()
w, h = im.size
array = []
for i in range (w):
	for j in range (h):
		array.append(pix[i,j])
ans = Counter(array)
print ans.most_common(10)[9][1]