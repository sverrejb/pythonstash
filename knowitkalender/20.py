import sys
sys.setrecursionlimit(10000)
visited = {}
def digit_sum(x):
	return sum(map(int,str(abs(x[0])) + str(abs(x[1]))))

def traverse(loc):
	if loc in visited or digit_sum(loc) > 19:
		return
	visited[loc] = True
	x,y = loc[0],loc[1]
	moves = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
	for m in moves:
		traverse(m)

traverse((0,0))
print len(visited)