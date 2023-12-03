#This file is STRICTLY for documentation purposes - and serves no other purpose - CodeAvali

import numpy as np
space = ' '

# (3). Turns function

def turn(Time_Stamp):
  if Time_Stamp % 2 == 1: 
    print("TEST: Black Playing...") 
    return False
  else:
    print("TEST: White Playing...")
    return True

# (1) Board creation 

W_Pawn = "♟︎"
B_Pawn = "♙"
W_Bish = '♝'
B_Bish = '♗' 
W_Knig = '♞'
B_Knig = '♘'
W_Rook = '♜'
B_Rook = '♖'
W_Quee = '♛'
B_Quee = '♕'
W_King = '♛'  
B_King = '♔'
Empty_ = '_'

WHITE = [W_Pawn, W_Bish, W_Knig, W_Rook, W_Quee, W_King]
BLACK = [B_Pawn, B_Bish, B_Knig, B_Rook, B_Quee, B_King]

#Move tuples

white_moves = [("Testing", "Help"), ("modified", "unlikely")]
black_moves = [("Hoping", "Will work")]

#white_moves += black_moves
#print(white_moves[2][1])

board = [[B_Rook, B_Knig, B_Bish, B_Quee, B_King, B_Bish, B_Knig, B_Rook],
         [B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn],
         [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
         [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
         [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
         [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
         [W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn], 
         [W_Rook, W_Knig, W_Bish, W_Quee, W_King, W_Bish, W_Knig, W_Rook]]

#Printing the chessboard
print(np.matrix(board))

#2. Performing a move

Playing = True
Time_Stamp = -1
while Playing:
  #Pass the turn to the next player 
  Time_Stamp += 1 
  White_Playing = turn(Time_Stamp)

  # Asking the user for a move
  Valid = False
  while not Valid: 
    Valid = True
    #Get inputs from users - using string literals to produce visual spacing
    move_from = input(f"location to move from, (x,y) {space*10}")
    move_to = input(f"location to move to, (x,y) {space*12}")     

    #Normalise y to what is expected
    move_fromx, move_fromy = move_from.split(",")
    move_fromy = (int(move_fromy) - 9) * -1
    move_from = move_fromx + "," + str(move_fromy)

    move_tox, move_toy = move_to.split(",")
    move_toy = (int(move_toy) - 9) * -1
    move_to = move_tox + "," + str(move_toy)

    #Create into a tuple
    move_from = tuple((int(x)-1) for x in move_from.split(","))
    move_to = tuple((int(x)-1) for x in move_to.split(","))

    #Perform exceptions; 
    Exception = ''
    if board[move_from[1]][move_from[0]] == Empty_:
      Exception += 'MOVE VALIDATION: There is no peice at inital'

    if White_Playing:
      if board[move_from[1]][move_from[0]] in BLACK:
        Exception += 'MOVE VALIDATION: You cannot move a black peice as White'
      elif board[move_to[1]][move_to[0]] in WHITE:
        Exception += 'MOVE VALIDATION: You can not move to a white peice as White'

    else:
      if board[move_from[1]][move_from[0]] in WHITE:
        Exception += 'MOVE VALDIATION: You cannot move a white peice as Black'
      elif board[move_to[1]][move_to[0]] in BLACK:
        Exception += 'MOVE VALDIATION: You cannot move to a black peice as White'

    if Exception != '':
      Valid = False
      print(Exception)

    #print(move_from, move_to) TEST

  #Printing inputs
  peice = board[(move_from[1])][(move_from[0])]  #Collect moving peice into temp variable 
  board[(move_from[1])][(move_from[0])] = Empty_  #Remove moving peice
  board[(move_to[1])][(move_to[0])] = peice #Hence, write the peice into the location 

  print(np.matrix(board))
