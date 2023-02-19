
class game():
	"""docstring for sad"""
	def __init__(self, board):
		self.white_to_move = True
		self.board = board
		self.castle_a1 = True
		self.castle_h1 = True
		self.castle_a8 = True
		self.castle_h8 = True
		self.enpassant = None
		
	def get_logical_moves(self,piece,position,color):
		if piece == "knight":
			moves = self.get_knight_moves(position)
		if piece == "bishop":
			moves = self.get_bishop_moves(position)
		if piece == "rook":
			moves = self.get_rook_moves(position)
		if piece == "pawn":
			moves = self.get_pawn_moves(position,color)
		if piece == "queen":
			moves = self.get_queen_moves(position)
		if piece == "king":
			moves = self.get_king_moves(position)
		new_moves = []
		for move in moves:
			y,x = move
			new_move = (y,x,position)
			new_moves.append(new_move)
		return(new_moves)

	def get_knight_moves(self,position):
		y,x = position
		moves = [(y+2,x+1),(y+2,x-1),(y-2,x+1),(y-2,x-1),(y+1,x+2),(y+1,x-2),(y-1,x+2),(y-1,x-2)]
		new_moves = []
		for move in moves:
			x,y = move
			if x < 9 and x > 0 and y > 0 and y < 9:
				new_moves.append(move)
		return(new_moves)

	def get_bishop_moves(self,position):
		y,x = position
		moves = []
		count = 1
		while count < 8:
			move = (y+count,x+count)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y-count,x-count)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y+count,x-count)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y-count,x+count)
			moves.append(move)
			count += 1
		new_moves = []
		for move in moves:
			x,y = move
			if x < 9 and x > 0 and y > 0 and y < 9:
				new_moves.append(move)
		return(new_moves)

	def get_rook_moves(self,position):
		y,x = position
		moves = []
		count = 1
		while count < 8:
			move = (y+count,x)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y-count,x)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y,x-count)
			moves.append(move)
			count += 1
		count = 1
		while count < 8:
			move = (y,x+count)
			moves.append(move)
			count += 1
		new_moves = []
		for move in moves:
			x,y = move
			if x < 9 and x > 0 and y > 0 and y < 9:
				new_moves.append(move)
		return(new_moves)

	def get_pawn_moves(self,position,color):
		if color == "white":
			y,x = position
			moves = [(y,x+1),(y+1,x+1),(y-1,x+1)]
			if x == 2:
				moves.append((y,x+2))
			new_moves = []
			for move in moves:
				x,y = move
				if x < 9 and x > 0 and y > 0 and y < 9:
					new_moves.append(move)
			return(new_moves)
		if color == "black":
			y,x = position
			moves = [(y,x-1),(y+1,x-1),(y-1,x-1)]
			if x == 7:
				moves.append((y,x-2))
			new_moves = []
			for move in moves:
				x,y = move
				if x < 9 and x > 0 and y > 0 and y < 9:
					new_moves.append(move)
			return(new_moves)

	def get_queen_moves(self,position):
		moves = self.get_rook_moves(position)
		moves_2= self.get_bishop_moves(position)
		moves = moves+moves_2
		return(moves)

	def get_king_moves(self,position):
		y,x = position
		moves = [(y,x+1),(y+1,x+1),(y-1,x+1),(y+1,x),(y-1,x),(y,x-1),(y+1,x-1),(y-1,x-1)]
		if position == (5, 1):
			if self.castle_h1 == True:
				moves.append((7, 1))
			if self.castle_a1 == True:
				moves.append((3, 1))
		if position == (5, 8):
			if self.castle_h8 == True:
				moves.append((7, 8))
			if self.castle_a8 == True:
				moves.append((3, 8))
		new_moves = []
		for move in moves:
			x,y = move
			if x < 9 and x > 0 and y > 0 and y < 9:
				new_moves.append(move)
		return(new_moves)

	def get_all_possible_moves(self):
		if self.white_to_move == True:
			to_move = "white"
		else:
			to_move = "black"
		board = self.board
		enpassant = self.enpassant
		all_logical_moves = []
		valid_moves = []
		for rank in board:
			for piece in rank:
				piece,position,color = piece
				if piece != "none":
					moves = self.get_logical_moves(piece,position,color)
					all_logical_moves = all_logical_moves + moves
		
		for move in all_logical_moves:
			y,x,orgin = move
			destination = (y,x)
			if self.is_move_valid(orgin,destination,board,to_move) == True:
				valid_moves.append(move)
		if self.enpassant != None:
				destination,orgin = self.enpassant
				y,x = destination
				move = (y,x,orgin)
				valid_moves.append(move)
		moves = []
		for move in valid_moves:
			x,y,orgin = move
			destination = (x,y)
			dic = self.conv_board_to_dic(board)
			for pos in dic:
				if dic[pos]["piece"] == "king" and dic[pos]["color"] == to_move:
					print(pos)
					king_pos = pos
			if self.is_king_check(pos,to_move) == True:
				print("check",move)
			else:
				moves.append(move)
		print(moves)
		return(valid_moves)

	def conv_board_to_dic(self,board):
		dic = {}
		for row in board:
			for piece in row:
				piece,position,color = piece
				dic[position] = {
				"color":color,
				"piece":piece 
				}
		return(dic)

	def is_move_valid(self,orgin,destination,board,to_move):
		board = self.board
		if self.white_to_move == True:
			to_move = "white"
		else:
			to_move = "black"
		y,x = destination
		dic = self.conv_board_to_dic(board)
		if dic[orgin]['color'] == dic[destination]['color']:
			return(False)
		if dic[orgin]['color'] != to_move:
			return(False)
		if dic[orgin]['piece'] == "bishop" or dic[orgin]['piece'] == "rook" or dic[orgin]['piece'] == "queen":
			path = self.get_path(orgin,destination)
			for value in path:
				if dic[orgin]['color'] == dic[value]['color']:
					return(False)
		if dic[orgin]['piece'] == "pawn":
			oy,ox = orgin
			if y == oy:
				path = self.get_path(orgin,destination)
				for value in path:
					if dic[orgin]['color'] == dic[value]['color']:
						return(False)
				if dic[destination]['piece'] != 'none':
					return(False)
			else:
				if dic[destination]['color'] != dic[orgin]['color']:
					return(False)
		if dic[orgin]['piece'] == "king":
			if dic[orgin]['color'] == "white":
				if orgin == (5, 1) and destination == (7, 1):
					if dic[(6, 1)]['piece'] != 'none' or dic[(7, 1)]['piece'] != 'none':
						return(False)
				if orgin == (5, 1) and destination == (3, 1):
					if dic[(2, 1)]['piece'] != 'none' or dic[(3, 1)]['piece'] != 'none' or dic[(4, 1)]['piece'] != 'none':
						return(False)
			if dic[orgin]['color'] == "black":
				if orgin == (5, 8) and destination == (7, 8):
					if dic[(6, 8)]['piece'] != 'none' or dic[(7, 8)]['piece'] != 'none':
						return(False)
				if orgin == (5, 8) and destination == (3, 8):
					if dic[(2, 8)]['piece'] != 'none' or dic[(3, 8)]['piece'] != 'none' or dic[(4, 8)]['piece'] != 'none':
						return(False)
		return(True)

	def get_path(self,orgin,destination):
		path = []
		oy,ox = orgin
		dy,dx = destination
		if ox == dx:
			if dy > oy:
				y = oy+1
				while y != dy:
					path.append((y,dx))
					y += 1
			if oy > dy:
				y = dy+1
				while y != oy:
					path.append((y,dx))
					y += 1
		if oy == dy:
			if dx > ox:
				x = ox+1
				while x != dx:
					path.append((oy,x))
					x += 1
			if ox > dx:
				x = dx+1
				while x != ox:
					path.append((oy,x))
					x += 1
		if abs(dx - ox) == abs(dy - oy):
			if dx-ox < 0:
				if dy-oy > 0:
					x = dx+1 
					y = dy-1 
					while x != ox:
						path.append((y,x))
						x += 1
						y -= 1
				if dy-oy < 0:
					x = dx+1 
					y = dy+1 
					while x != ox:
						path.append((y,x))
						x += 1
						y += 1
			if dx-ox > 0:
				if dy-oy > 0:
					x = dx-1 
					y = dy-1 
					while x != ox:
						path.append((y,x))
						x -= 1
						y -= 1
				if dy-oy < 0:
					x = dx-1 
					y = dy+1 
					while x != ox:

						path.append((y,x))
						x -= 1
						y += 1
		return(path)
			
	def move(self,orgin,destination):
		valid_moves = self.get_all_possible_moves()
		enpassant = None
		if self.enpassant != None:
			enpassant = self.enpassant
		self.enpassant = None
		y,x = destination
		move = (y,x,orgin)
		if move in valid_moves:
			board = self.board
			oy,ox = orgin
			piece = board[ox-1][oy-1]
			piece,position,color = piece
			if piece == "king" and color == "white" and orgin == (5, 1):
				if destination == (7, 1):
					board[0][4] = ("none",(5, 1), "none")
					board[0][7] = ("none",(8, 1), "none")
					board[0][5] = ("rook",(6, 1), "white")
					board[0][6] = ("king",(7, 1), "white")
				if destination == (3, 1):
					board[0][4] = ("none",(5, 1), "none")
					board[0][0] = ("none",(1, 1), "none")
					board[0][3] = ("rook",(4, 1), "white")
					board[0][2] = ("king",(3, 1), "white")
			elif piece == "king" and color == "black" and orgin == (5, 8):
				if destination == (7, 8):
					board[7][4] = ("none",(5, 8), "none")
					board[7][7] = ("none",(8, 8), "none")
					board[7][5] = ("rook",(6, 8), "black")
					board[7][6] = ("king",(7, 8), "black")
				if destination == (3, 8):
					board[7][4] = ("none",(5, 8), "none")
					board[7][0] = ("none",(1, 8), "none")
					board[7][3] = ("rook",(4, 8), "black")
					board[7][2] = ("king",(3, 8), "black")
			else:
				fpiece = piece
				if piece == "king":
					if color == "white":
						self.castle_a1 = False
						self.castle_h1 = False
					if color == "black":
						self.castle_a8 = False
						self.castle_h8 = False
				if piece == "rook":
					if orgin == (8, 1):
						self.castle_h1 = False
					if orgin == (1, 1):
						self.castle_a1 = False
					if orgin == (8, 8):
						self.castle_h8 = False
					if orgin == (1, 8):
						self.castle_a8 = False
				piece = ("none",position,"none")
				board[ox-1][oy-1] = piece
				dy,dx = destination
				if enpassant != None:
					edestination,eorgin = enpassant
					if edestination == destination and orgin == eorgin:
						tempx,r = orgin
						p,tempx = destination
						piece = ("none",(p,r),"none")
						board[r-1][p-1] = piece


				if fpiece == "pawn":
					if color == "white":
						if ox == 2 and dx == 4:
							if y-2 > 0:	
								lpiece,g,lcolor = board[3][y-2]
								if lpiece == "pawn" and lcolor == 'black':
									self.enpassant = ((y,3),(y-1,4))
							if y < 7:
								rpiece,g,rcolor = board[3][y]
								if rpiece == "pawn" and rcolor == 'black':
									self.enpassant = ((y,3),(y+1,4))
					if color == "black":
						if ox == 7 and dx == 5:
							if y-2 > 0:	
								lpiece,g,lcolor = board[4][y-2]
								if lpiece == "pawn" and lcolor == 'white':
									self.enpassant = ((y,6),(y-1,5))
							if y < 7:
								rpiece,g,rcolor = board[4][y]
								if rpiece == "pawn" and rcolor == 'white':
									self.enpassant = ((y,6),(y+1,5))
				piece = board[dx-1][dy-1]
				x,position,y = piece
				piece = (fpiece,position,color)
				board[dx-1][dy-1] = piece
			self.board = board
			if self.white_to_move == True:
				self.white_to_move = False
			else:
				self.white_to_move=True
			return(True)
		else:
			return(False)

	def get_all_possible_moves_pro(self,color,board):
		to_move = color
		all_logical_moves = []
		valid_moves = []
		for rank in board:
			for piece in rank:
				piece,position,color = piece
				if piece != "none":
					moves = self.get_logical_moves(piece,position,color)
					all_logical_moves = all_logical_moves + moves
		
		for move in all_logical_moves:
			y,x,orgin = move
			destination = (y,x)
			if self.is_move_valid(orgin,destination,board,to_move) == True:
				valid_moves.append(move)
		return(valid_moves)

	def is_board_check(self,board,color):
		dic = self.conv_board_to_dic(board)
		if color == "white":
			ccolor = "black"
		if color == "black":
			ccolor = "white"
		moves = self.get_all_possible_moves_pro(ccolor,board)
		chek = False
		for move in moves:
			x,y,orgin = move
			if dic[(x,y)]["piece"] == "king":
				chek = True
		return(chek)

def temp_move(board,destination,orgin):
	y,x = destination
	move = (y,x,orgin)
	oy,ox = orgin
	piece = board[ox-1][oy-1]
	piece,position,color = piece
	if piece == "king" and color == "white" and orgin == (5, 1):
		if destination == (7, 1):
			board[0][4] = ("none",(5, 1), "none")
			board[0][7] = ("none",(8, 1), "none")
			board[0][5] = ("rook",(6, 1), "white")
			board[0][6] = ("king",(7, 1), "white")
		if destination == (3, 1):
			board[0][4] = ("none",(5, 1), "none")
			board[0][0] = ("none",(1, 1), "none")
			board[0][3] = ("rook",(4, 1), "white")
			board[0][2] = ("king",(3, 1), "white")
	elif piece == "king" and color == "black" and orgin == (5, 8):
		if destination == (7, 8):
			board[7][4] = ("none",(5, 8), "none")
			board[7][7] = ("none",(8, 8), "none")
			board[7][5] = ("rook",(6, 8), "black")
			board[7][6] = ("king",(7, 8), "black")
		if destination == (3, 8):
			board[7][4] = ("none",(5, 8), "none")
			board[7][0] = ("none",(1, 8), "none")
			board[7][3] = ("rook",(4, 8), "black")
			board[7][2] = ("king",(3, 8), "black")
	else:
		fpiece = piece
		piece = ("none",position,"none")
		board[ox-1][oy-1] = piece
		dy,dx = destination
		piece = board[dx-1][dy-1]
		x,position,y = piece
		piece = (fpiece,position,color)
		board[dx-1][dy-1] = piece
	return(board)

