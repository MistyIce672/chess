import discord
from discord.ext import commands, tasks
import random
import string
from PIL import Image

intents = discord.Intents.all()
intents = intents
client = commands.Bot(command_prefix=["`","` "],intents=intents)

global games,board
games = {}

h = [("rook",(1,8),('black')),("knight",(2,8),('black')),("bishop",(3,8),('black')),("queen",(4,8),('black')),("king",(5,8),('black')),("bishop",(6,8),('black')),("knight",(7,8),('black')),("rook",(8,8),('black'))]
g = [("pawn",(1,7),('black')),("pawn",(2,7),('black')),("pawn",(3,7),('black')),("pawn",(4,7),('black')),("pawn",(5,7),('black')),("pawn",(6,7),('black')),("pawn",(7,7),('black')),("pawn",(8,7),('black'))]
f = [("none",(1,6),('none')),("none",(2,6),('none')),("none",(3,6),('none')),("none",(4,6),('none')),("none",(5,6),('none')),("none",(6,6),('none')),("none",(7,6),('none')),("none",(8,6),('none'))]
e = [("none",(1,5),('none')),("none",(2,5),('none')),("none",(3,5),('none')),("none",(4,5),('none')),("none",(5,5),('none')),("none",(6,5),('none')),("none",(7,5),('none')),("none",(8,5),('none'))]
d = [("none",(1,4),('none')),("none",(2,4),('none')),("none",(3,4),('none')),("none",(4,4),('none')),("none",(5,4),('none')),("none",(6,4),('none')),("none",(7,4),('none')),("none",(8,4),('none'))]
c = [("none",(1,3),('none')),("none",(2,3),('none')),("none",(3,3),('none')),("none",(4,3),('none')),("none",(5,3),('none')),("none",(6,3),('none')),("none",(7,3),('none')),("none",(8,3),('none'))]
b = [("pawn",(1,2),('white')),("pawn",(2,2),('white')),("pawn",(3,2),('white')),("pawn",(4,2),('white')),("pawn",(5,2),('white')),("pawn",(6,2),('white')),("pawn",(7,2),('white')),("pawn",(8,2),('white'))]
a = [("rook",(1,1),('white')),("knight",(2,1),('white')),("bishop",(3,1),('white')),("queen",(4,1),('white')),("king",(5,1),('white')),("bishop",(6,1),('white')),("knight",(7,1),('white')),("rook",(8,1),('white'))]

board = [h,g,f,e,d,c,b,a]

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def game(ctx,member : discord.Member = None):
	board = create_game(ctx.author.id,member.id)
	text = board_to_text(board)
	await ctx.channel.send("Game started!")
	await ctx.channel.send(text)

def create_game(player1,player2):
	game_id = (''.join(random.choices(string.digits, k=10)))
	games[game_id] = {
	"white" : player1,
	"black" : player2,
	"board" : board,
	"to_move": "white" 
	}
	print(player1,player2)
	return(board)

def board_to_image(board):
	im1 = Image.open(r"D:\users\Documents\code\python_projects\chess\images\board")
	im2 = Image.open(r"D:\users\Documents\code\python_projects\chess\images\pieces")
	Image.Image.paste(im1, im2, (50, 125))
	im1.show()


def board_to_text(board):
	text = ""
	for row in board:
		for piece in row:
			piece,position,color = piece
			if color == "white":
				if piece == "queen":
					text = f'{text} {"♛"}'
				if piece == "rook":
					text = f'{text} {"♜"}'
				if piece == "bishop":
					text = f'{text} {"♝"}'
				if piece == "king":
					text = f'{text} {"♚"}'
				if piece == "pawn":
					text = f'{text} {"♟"}'
				if piece == "knight":
					text = f'{text} {"♞"}'
			if color == "white":
				if piece == "queen":
					text = f'{text} {"♕"}'
				if piece == "rook":
					text = f'{text} {"♖"}'
				if piece == "bishop":
					text = f'{text} {"♗"}'
				if piece == "king":
					text = f'{text} {"♔"}'
				if piece == "pawn":
					text = f'{text} {"♙"}'
				if piece == "knight":
					text = f'{text} {"♘"}'
		text = f'{text}\n'
	return(text)

client.run("MTA3MjQyMjczOTEyMzY1MDU3MA.GPqj7c.9FiKb__i7vW54nu8eRd1tllUOn-fy_3dcuTqJA")