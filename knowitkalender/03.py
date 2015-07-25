board = [[True]*10 for i in range(10)]
xpos = 0
ypos = 0 
color = True
possible_moves = []

ans = 0
for b in board:
	ans += b.count(False)
print ans

def tryMove(x,y):	
	if(x>=0 and x<=9):
		if(y>=0 and y<=9):
			return True
	return False

def findMoves(x,y):
	moves = []
	if(tryMove(x+2, y+1)):
		moves.append(str(x+2)+str(y+1))
	if(tryMove(x+2, y-1)):
		moves.append(str(x+2)+str(y-1))
	if(tryMove(x-2, y+1)):
		moves.append(str(x-2)+str(y+1))
	if(tryMove(x-2, y-1)):
		moves.append(str(x-2)+str(y-1))
	if(tryMove(x+1, y+2)):
		moves.append(str(x+1)+str(y+2))
	if(tryMove(x+1, y-2)):
		moves.append(str(x+1)+str(y-2))
	if(tryMove(x-1, y+2)):
		moves.append(str(x-1)+str(y+2))
	if(tryMove(x-1, y-2)):
		moves.append(str(x-1)+str(y-2))
	return moves

for i in range(10):
	possible_moves = findMoves(xpos, ypos);
	possible_moves.sort()

	for move in possible_moves:
		if (board[int(str(move)[0])][int(str(move)[1])]==color):
			color = board[int(str(move)[0])][int(str(move)[1])]
			board[xpos][ypos] = not board[xpos][ypos]
			xpos = int(str(move)[0])
			ypos = int(str(move)[1])
			print "traveled to " + str(move)
			break
		
		print("No same color available")
		lastmove = possible_moves[len(possible_moves)-1]
		color = board[int(str(lastmove)[0])][int(str(lastmove)[1])]
		board[xpos][ypos] = not board[xpos][ypos]
		xpos = int(str(lastmove)[0])
		ypos = int(str(lastmove)[1])
		print "traveled to " + str(move)

ans = 0
for b in board:
	ans += b.count(False)
print ans