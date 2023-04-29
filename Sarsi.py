from random import randint, shuffle
from time import sleep

BOARDDIMENSION = 8
EMPTY = "  "

def CreateBoard():
	Board = []
	for Count in range(BOARDDIMENSION + 1):
		Board.append([])
		for Count2 in range(BOARDDIMENSION + 1):
			Board[Count].append(EMPTY)
	return Board

def GetColourName(WhoseTurn):
	if WhoseTurn == "W":
		return "White"
	else:
		return "Black"

def DisplayWinner(WhoseTurn):
	if WhoseTurn == "W":
		print("Black's Sarsi has been captured.	White wins!")
	else:
		print("White's Sarsi has been captured.	Black wins!")

def CheckIfGameWillBeWon(Board, EndY, EndX):
	if Board[EndY][EndX][1] == "S":
		return True
	else:
		return False

def DisplayBoard(Board):
	print()
	for y in range(1, BOARDDIMENSION + 1):
		print("      _______________________")
		print(y, end="	 ")
		for x in range(1, BOARDDIMENSION + 1):
			print("|" + Board[y][x], end="")
		print("|")
	print("      _______________________")
	print()
	print("      1  2  3  4  5  6  7  8")
	print()
	print()		



def CheckSarsiMoveIsLegal(Board, XDiff, YDiff):	
	CheckSarsiMoveIsLegal = False

	if XDiff <= 1 and YDiff <= 1:
		CheckSarsiMoveIsLegal = True

	return CheckSarsiMoveIsLegal

def CheckNobleMoveIsLegal(Board, XDiff, YDiff):	
	CheckNobleMoveIsLegal = False

	if XDiff == 1 and YDiff == 1:
		CheckNobleMoveIsLegal = True

	return CheckNobleMoveIsLegal

def CheckMonkMoveIsLegal(Board, XDiff, YDiff):	
	CheckMonkMoveIsLegal = False	

	if (XDiff == 1 and YDiff == 0) or (XDiff == 0 and YDiff == 1):
		CheckMonkMoveIsLegal = True

	return CheckMonkMoveIsLegal

def CheckEntMoveIsLegal(Board, XDiff, YDiff):
	CheckEntMoveIsLegal = False

	if (XDiff == 2 and YDiff == 0) or (XDiff == 0 and YDiff == 2):
		CheckEntMoveIsLegal = True

	return CheckEntMoveIsLegal


def CheckRecruitMoveIsLegal(Board, StartY, StartX, EndY, EndX, XDiff, YDiff, ColourOfPiece):
	
	CheckRecruitMoveIsLegal = False
	if ColourOfPiece == "W":
		if EndY == StartY - 1:
			if EndX == StartX and Board[EndY][EndX] == EMPTY:
				CheckRecruitMoveIsLegal = True
			elif XDiff == 1 and Board[EndY][EndX][0] == "B":
				CheckRecruitMoveIsLegal = True
	elif EndY == StartY + 1:
		if EndX == StartX and Board[EndY][EndX] == EMPTY:
			CheckRecruitMoveIsLegal = True
		elif XDiff == 1 and Board[EndY][EndX][0] == "W":
			CheckRecruitMoveIsLegal = True
	return CheckRecruitMoveIsLegal


def CheckGargoyleMoveIsLegal(Board, StartY, StartX, EndY, EndX):
	YMovement = EndY - StartY
	XMovement = EndX - StartX
	GargoyleMoveIsLegal = False
	if YMovement == 0:
		if XMovement >= 1:
			GargoyleMoveIsLegal = True
			for Count in range(1, XMovement):
				if Board[StartY][StartX + Count] != EMPTY:
					GargoyleMoveIsLegal = False
		elif XMovement <= -1:
			GargoyleMoveIsLegal = True
			for Count in range(-1, XMovement, -1):
				if Board[StartY][StartX + Count] != EMPTY:
					GargoyleMoveIsLegal = False
	elif XMovement == 0:
		if YMovement >= 1:
			GargoyleMoveIsLegal = True
			for Count in range(1, YMovement):
				if Board[StartY + Count][StartX] != EMPTY:
					GargoyleMoveIsLegal = False
		elif YMovement <= -1:
			GargoyleMoveIsLegal = True
			for Count in range(-1, YMovement, -1):
				if Board[StartY + Count][StartX] != EMPTY:
					GargoyleMoveIsLegal = False
	return GargoyleMoveIsLegal


def CheckMoveIsLegal(Board, StartY, StartX, EndY, EndX, WhoseTurn):
	MoveIsLegal = True
	PieceType = ""
	if (EndX == StartX) and (EndY == StartY):
		MoveIsLegal = False
	else:
		PieceType = Board[StartY][StartX][1]
		PieceColour = Board[StartY][StartX][0]
		if WhoseTurn == "W":
			if PieceColour != "W":
				MoveIsLegal = False
			if Board[EndY][EndX][0] == "W":
				MoveIsLegal = False
		else:
			if PieceColour != "B":
				MoveIsLegal = False
			if Board[EndY][EndX][0] == "B":
				MoveIsLegal = False
		if MoveIsLegal == True:
			XDiff = abs(EndX - StartX)
			YDiff = abs(EndY - StartY)
			if PieceType == "R":
				MoveIsLegal = CheckRecruitMoveIsLegal(Board, StartY, StartX, EndY, EndX, XDiff, YDiff, PieceColour)
			elif PieceType == "S":
				MoveIsLegal = CheckSarsiMoveIsLegal(Board, XDiff, YDiff)
			elif PieceType == "M":
				MoveIsLegal = CheckMonkMoveIsLegal(Board, XDiff, YDiff)
			elif PieceType == "G":
				MoveIsLegal = CheckGargoyleMoveIsLegal(Board, StartY, StartX, EndY, EndX)
			elif PieceType == "N":
				MoveIsLegal = CheckNobleMoveIsLegal(Board, XDiff, YDiff)
			elif PieceType == "E":
				MoveIsLegal = CheckEntMoveIsLegal(Board, XDiff, YDiff)
	return MoveIsLegal, PieceType

		
										
def GetMove(StartCell, EndCell):
	StartCell = int(input("Enter coordinates of square containing piece to move (xy format): "))
	EndCell = int(input("Enter coordinates of square to move piece to (xy format): "))
	return StartCell, EndCell

def GetPieceName(PieceCode):
	Codes = ["E", "M", "G", "R", "N", "S", "K", "T"]
	Pieces = ["Ent", "Monk", "Gargoyle", "Recruit", "Noble", "Sarsi", "King", "Thief"]

	for Count in range(8):
		if Codes[Count] == PieceCode:
			return Pieces[Count]

def MakeMove(Board, StartY, StartX, EndY, EndX, Colour, PieceType):

	PieceName = GetPieceName(PieceType)
	print(Colour, PieceName, "moved from", StartX, StartY, "to", EndX, EndY, "!")

	if Board[EndY][EndX] != EMPTY:
		print(Board[EndY][EndX], "was captured!")

	if Colour == "White" and EndY == 1 and Board[StartY][StartX][1] == "R":
		Board[EndY][EndX] = "WM"
	elif Colour == "Black" and EndY == 8 and Board[StartY][StartX][1] == "R":
		Board[EndY][EndX] = "BM"
	else:
		Board[EndY][EndX] = Board[StartY][StartX]

	Board[StartY][StartX] = EMPTY

	
def RandomBoard(ChallengeMode = False):

	Codes = [[c+t for t in "RRRRRRRRSMEGEGNN"] for c in "WB"]

	Codes = Codes[0] + Codes[1]

	
	if ChallengeMode:
		Codes += ["BK", "WK", "BT", "WT"]

	Board = []

	for Count in range(BOARDDIMENSION + 1):
		Board.append([])
		for Count2 in range(BOARDDIMENSION + 1):
			Board[Count].append(EMPTY)

	shuffle(Codes)

	WhiteSarsi = False
	BlackSarsi = False

	while len(Codes):
		Piece = Codes.pop()
		if randint(0, 1):

			
			if Piece == "WS":	WhiteSarsi = True				
			
			if Piece == "BS":	BlackSarsi = True

			y = randint(1, 8)
			x = randint(1, 8)
			if Board[y][x][1] != "S":
				Board[y][x] = Piece

	if not BlackSarsi:
		Board[5][1] == "BS"
	elif not WhiteSarsi:
		Board[5][8] == "WS"


	return Board


def Quiz():

	print("Score 10 points to win.")

	pts = 0

	while pts < 10:

		b = RandomBoard()
		DisplayBoard(b)

		Piece = EMPTY
		while Piece == EMPTY:
			StartY = randint(1, 8)
			StartX = randint(1, 8)
			Piece = b[StartY][StartX]
		
		print("Look at this board.")



		EndY, EndX = StartY, StartX



		ChangeY = False

		MoveFound = False
		while not MoveFound:
			if randint(0, 1):
				ChangeY = True
			if ChangeY:
				EndY = StartY + randint(-2, 2)
			
			if not ChangeY or randint(0, 1):
				EndX = StartX + randint(-2, 2)

			# piece must have moved. but allow same square 33% of the time
			if (StartX != EndX and StartY != EndY) or not randint(0, 2):
				# piece must be in bounds. but allow out of bounds 25% of the time
				if 0 < EndX < 9 and 0 < EndY < 9 or not randint(0, 3):
					MoveFound = True

		print(f"The player tries to move the piece from cell {StartX}{StartY} to cell {EndX}{EndY}...")

		print("This move is legal. True or False?")

		Answer = input().lower()
		while Answer not in ["true", "false"]:
			Answer = input("True or False?").lower()

		Answer = bool(Answer.lower().replace("false", ""))

		Correct = CheckMoveIsLegal(b, StartY, StartX, EndY, EndX, Piece[0])[0]
		
	
		if Answer == Correct:
			print("Well done. +1 point")
			pts += 1
		else:
			print("That answer was wrong. -1 point")
			pts -= 1
			exp = input("Study the code and explain what you did wrong there:")
			print("Thanks for reflecting.")
		
		sleep(1)

Quiz()
print("You won. Now continue with your worksheet.")


