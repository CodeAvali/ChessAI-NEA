#Live document for current work - Code Avali - Chessbot NEA

import numpy as np
space = ' '

global White_Playing
global White_moves
global Black_moves 



# (3). Turns function

def turn(Time_Stamp):
  if Time_Stamp % 2 == 1: 
    print("TEST: Black Playing...") 
    return False
  else:
    print("TEST: White Playing...")
    return True

  #----

def action(move_to, move_from):

  #Normalise y to what is expecteD
  move_fromx, move_fromy = move_from.split(",")
  move_fromy = (int(move_fromy) - 9) * -1
  move_from = move_fromx + "," + str(move_fromy)

  move_tox, move_toy = move_to.split(",")
  move_toy = (int(move_toy) - 9) * -1
  move_to = move_tox + "," + str(move_toy)

  #Create into a tuple
  move_from = tuple((int(x)-1) for x in move_from.split(","))
  move_to = tuple((int(x)-1) for x in move_to.split(","))

  return move_to, move_from 

  #----

def absurd(move_to, move_from):
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
    print(Exception)
    return False
  else: 
    return True 

  #----

def perform(move_to, move_from, board):

  global White_moves

  #Performing moves
  print("TEST:", move_to, move_from)
  
  peice = board[(move_from[1])][(move_from[0])]  #Collect moving peice into temp variable 
  board[(move_from[1])][(move_from[0])] = Empty_  #Remove moving peice
  board[(move_to[1])][(move_to[0])] = peice #Hence, write the peice into the location 

  #Check for peice to generate new moves
  if peice == W_Pawn or peice == B_Pawn:
    White_moves += pawn((move_to[0], move_to[1]), White_Playing)
  elif peice == (W_Rook or B_Rook) or peice == (W_Queen or B_Queen):
    White_moves = straight((move_to[0], move_to[1]), White_Playing)

  #White_moves = clean(move_from, White_moves)

  print(White_moves)

  return board


  #----

def clean(move_from, moves):
  cleaned = str(move_from[0]) + str(move_from[1])
  #updated = tuple(x for x in moves_tuple if match(moves_tuple[x][0], cleaned, x))
  updated = tuple(x for x in moves if match(moves[x][0], cleaned, moves[x]))


  print(updated)

def match(move_from, cleaned, x):
  if cleaned == (str(move_from[0]) + str(move_from[1])):
    return True
  else:
    return False

  #----

def pawn(create, White_Playing):
  #from inital, collect the x and y components 

  create_x, create_y = create[0], create[1]

  #Hence, create a tuple containing new moves 

  new = ()

  if White_Playing:
    create_y -= 1
    temp = (create_x, create_y)  
    #Add any additional conditions - Capture; enpassant 
  else: 
    create_y += 1
    temp = (create_x, create_y)                                #PERFECT METHOD for masked tuple - yayayaya
    #Add any additional conditions - Caputre; enpassant 
    
  new += (create, tuple(temp))   #PERFECT METHOD for masked tuple - yayayaya
  print(new)
  
  return new

  #-----

def straight(create, White_playing):
  #from inital, collect the x and y components

  create_x, create_y = create[0], create[1]

  #Hence, create a tuple of new moves

  new = ()
  mod = ()

  x_pointer = create_x
  while x_pointer < 7:
    x_pointer += 1
    temp = (x_pointer, create_y)  
    new += (create, tuple(temp))
  x_pointer = create_x
  while x_pointer > 0:
    x_pointer -= 1 
    temp = (x_pointer, create_y)  
    new += (create, tuple(temp))

  y_pointer = create_y 
  while y_pointer < 7:
    y_pointer += 1
    temp = (create_x, y_pointer)  
    new += (create, tuple(temp))
  y_pointer = create_y
  while y_pointer > 0:
    y_pointer -= 1 
    temp = (create_x, y_pointer)  
    new += (create, tuple(temp))
    
  print(new)

  
  return new
  
    




  #----

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

White_moves = []
#black_moves = [("Hoping", "Will work")]

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

    #Process accordingly and normalise
    move_to, move_from = action(move_to, move_from)

    #Perform exceptions; 
    valid = absurd(move_to, move_from)

  #Printing inputs
  board = perform(move_to, move_from, board)

  print(np.matrix(board))


  #testing for [0, 4] index
  if (0,4) in White_moves:
    print("SUCCESS")
  else:
    print("FAIL")
