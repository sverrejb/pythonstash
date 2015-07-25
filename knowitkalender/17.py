import time
start = time.clock()
board = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
xlim, ylim = len(board)-1, len(board[0])-1
move_chains= []
x, y = 0,0

def do_moves(x,y, move_string = "", counter = 1):
	moves = find_moves(x,y)
	if counter == 10:
		move_chains.append(move_string)
		return True
	for move in moves:
		do_moves(int(move[0]),int(move[1]), move_string + move, counter + 1)

def try_move(x,y):	
	if 0 <= x <= xlim and 0 <= y <= ylim:
		return board[x][y]>=0
	return False

def find_moves(x,y): #burde skrivast om til å returnere tuplar, string blir feil om antall rader eller kolonner blir 2-sifra
	moves = []
	if(try_move(x+2, y+1)):
		moves.append(str(x+2)+str(y+1))
	if(try_move(x+2, y-1)):
		moves.append(str(x+2)+str(y-1))
	if(try_move(x-2, y+1)):
		moves.append(str(x-2)+str(y+1))
	if(try_move(x-2, y-1)):
		moves.append(str(x-2)+str(y-1))
	if(try_move(x+1, y+2)):
		moves.append(str(x+1)+str(y+2))
	if(try_move(x+1, y-2)):
		moves.append(str(x+1)+str(y-2))
	if(try_move(x-1, y+2)):
		moves.append(str(x-1)+str(y+2))
	if(try_move(x-1, y-2)):
		moves.append(str(x-1)+str(y-2))
	return moves

do_moves(x,y)
print len(move_chains)
print time.clock() - start