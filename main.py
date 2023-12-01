# CodeAvali - Educational Chessbot demonstration - LAST UPDATED: 29/11/23

import numpy as np

# (3). Turns function

def turn(Time_Stamp):
  White_Playing = True 
  if Time_Stamp % 2 == 1: 
    White_Playing = False
    print("Black Playing...")
  else:
    print("White Playing...")
  return White_Playing 
    
# (1) Board creation 

W_Pawn = "♙"
B_Pawn = '♟︎' 
W_Bish = '♗'
B_Bish = '♝' 
W_Knig = '♘'
B_Knig = '♞' 
W_Rook = '♖'
B_Rook = '♜'
W_Quee = '♕'
B_Quee = '♛'
W_King = '♔'
B_King = '♛'
Empty_ = '-'

WHITE = [W_Pawn, W_Bish, W_Knig, W_Rook, W_Quee, W_King]
BLACK = [B_Pawn, B_Bish, B_Knig, B_Rook, B_Quee, B_King]


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
    #Get inputs from users
    move_from = input("location to move from, {x, y}       ")
    move_from = tuple((int(x)-1) for x in move_from.split(","))
    move_to = input("location to move to, {x, y}         ")
    move_to = tuple((int(x)-1) for x in move_to.split(","))

    #Perform basic validation for moves
    Exception = ''
    if move_from == move_to:                          #Move goes to the same space;
      Valid = False
      Exception += 'MOVE VALIDATION: You cannot move to the same space'
    elif board[move_from[1]][move_from[0]] == Empty_:  #Peice being moved doesn't exist
      Valid = False
      Exception += 'MOVE VALIDATION: You cannot move an non-existent peice'
    elif White_Playing:
      if board[move_from[1]][move_from[0]] in BLACK:
        Valid = False
        Exception += 'MOVE VALIDATION: You cannot move a black peice as White'
      elif board[move_to[1]][move_to[0]] in WHITE:
        Valid = False
        Exception += 'MOVE VALIDATION: You can not move to a white peice as White'
    else:
      if board[move_from[1]][move_from[0]] in WHITE:
        Valid = False
        Exception += 'MOVE VALDIATION: You cannot move a white peice as Black'
      elif board[move_to[1]][move_to[0]] in BLACK:
        Valid = False
        Exception += 'MOVE VALDIATION: You cannot move to a black peice as White'

    if Exception != '':
      print(Exception)
      
  print(move_from, move_to)

  #Printing inputs
  peice = board[(move_from[1])][(move_from[0])]  #Collect moving peice into temp variable 
  board[(move_from[1])][(move_from[0])] = Empty_  #Remove moving peice
  board[(move_to[1])][(move_to[0])] = peice #Hence, write the peice into the location 

  print(np.matrix(board))



  



