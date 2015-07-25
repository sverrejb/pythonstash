def find_max_straight(n):
	max = 0
	for i in n:
		for j in range(len(i)):
			val = reduce(lambda x,y:x*y, i[j:j+4])
			if val > max:
				max = val
	return max

def find_max_diag(n):
	max = 0
	for i in range (0,len(n)-3):
		for j in range (0,len(n[i])-3):
			val = 1
			for x in range (0,4):
				val *= n[i+x][j+x]
				if val > max:
					max = val
	return max

#creates matrix from file
f,m = open('11number.txt', 'r+'),[]
for l in f:
	m.append(map(int, l.split(' ')))
f.close()

m_rot = zip(*m[::-1]) #rotates matrix 90*
m_flip = [row[::-1] for row in m] #mirrors matrix

products = []
products.append(find_max_straight(m))
products.append(find_max_straight(m_rot))
products.append(find_max_diag(m))
products.append(find_max_diag(m_flip))

print max(products)