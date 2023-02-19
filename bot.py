from PIL import Image
from game import game

def fen_to_lis(fen):
	fen = fen.split(" ")
	board = fen[0]
	to_move = fen[1]
	castle_data = fen[2]
	board = board.split("/")
	board_lis = []
	y = 1
	x = 8
	for line in board:
		line_lis = []
		y = 1
		for char in line:
			if char in ['1','2','3','4','5','6','7','8']:
				count = 0
				while count < int(char):
					line_lis.append(('none',(y,x),'none'))
					y += 1
					count += 1
			else:
				if char == "r":
					piece = "rook"
					color = "black"
				if char == "n":
					piece = "knight"
					color = "black"
				if char == "b":
					piece = "bishop"
					color = "black"
				if char == "q":
					piece = "queen"
					color = "black"
				if char == "k":
					piece = "king"
					color = "black"
				if char == "p":
					piece = "pawn"
					color = "black"
				if char == "R":
					piece = "rook"
					color = "white"
				if char == "N":
					piece = "knight"
					color = "white"
				if char == "B":
					piece = "bishop"
					color = "white"
				if char == "Q":
					piece = "queen"
					color = "white"
				if char == "K":
					piece = "king"
					color = "white"
				if char == "P":
					piece = "pawn"
					color = "white"
				line_lis.append((piece,(y,x),color))
				y += 1
		x -= 1
		board_lis.append(line_lis)
	board = []
	while len(board_lis) > 0:
		board.append(board_lis[-1])
		board_lis.pop(-1)
	return(board)

def conv_to_num(position):
	y,x = position
	letters = ["a","b","c","d","e","f","g","h"]
	y = letters.index(y)
	y += 1
	position = (y,int(x))
	return(position)
	
def conv_to_letter(position):
	y,x = position
	letters = ["a","b","c","d","e","f","g","h"]
	y = y-1
	y = letters[y]
	position = (y,x)
	return(position)

def conv_move_to_letter(move):
	y,x,position = move
	position =  conv_to_letter(position)
	y,x = conv_to_letter((y,x))
	move = (y,x,position)
	return(move)

def board_to_image(board):
	im1 = Image.open(r"D:\users\Documents\code\python_projects\chess\images\board.png")
	for row in board:
		for piece in row:
			piece,pos,color = piece
			if piece != "none":
				im2 = Image.open(f"D:\\users\\Documents\\code\\python_projects\\chess\\images\\{color}_{piece}.png")
				x,y = pos
				##fliping board on y axis to match cordinates
				y = 9-y
				pos = (x*65-65,y*65-65)
				im1.paste(im2, pos,im2)
	im1.show()

board = fen_to_lis("8/8/8/2K2rk1/8/8/8/8 w - - 0 1")




game = game(board)
while True:
	board_to_image(game.board)
	move = str(input("Enter move: "))
	a = move[0]
	b = move[1]
	y = move[3]
	x = move[4]
	orgin = (a,b)
	destination = (y,x)
	orgin = conv_to_num(orgin)
	destination = conv_to_num(destination)
	y,x = destination
	sc = game.move(orgin,destination)
	if sc == False:
		print("invalid move try again \n")