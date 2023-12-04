#Live document for current work - Code Avali - Chessbot NEA

import numpy as np
global board 
global White_Playing
global White_moves
global Black_moves 
global Moves_Tuple
space = ' '

# (3) ----------- Functions ------------------

def turn(Time_Stamp):
  if Time_Stamp % 2 == 1: 
    print(" Black Playing...") 
    Moves_Tuple = Black_moves
    return False, Moves_Tuple
  else:
    print(" White Playing...")
    Moves_Tuple = White_moves
    return True, Moves_Tuple

  #----

def action(move_to, move_from):

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

  return move_to, move_from 

  #----

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
  global Black_moves

  Moves_Tuple = []

  #Performing moves
  print("TEST:", move_to, move_from)

  peice = board[(move_from[1])][(move_from[0])]  #Collect moving peice into temp variable 
  board[(move_from[1])][(move_from[0])] = Empty_  #Remove moving peice
  board[(move_to[1])][(move_to[0])] = peice #Hence, write the peice into the location 

  #Check for peice to generate new moves
  if peice in (W_Pawn, B_Pawn):
    Moves_Tuple += pawn((move_to[0], move_to[1]), White_Playing)
  elif peice in (W_Rook, B_Rook, W_Quee, B_Quee):
    Moves_Tuple += straight((move_to[0], move_to[1]))

  #Hence; store new to respective holder
  if White_Playing:
    White_moves += Moves_Tuple
    White_moves = clean(move_from, White_moves)
    Black_moves = clean(move_to, Black_moves)
  else:
    Black_moves += Moves_Tuple
    Black_moves = clean(move_from, Black_moves)
    White_moves = clean(move_to, White_moves)

  return board 

  #----

def legal(move_to, move_from, move_space): 

  print(move_space)

  for i in range(len(move_space)):
    print(move_to, move_space[i][0])
    if move_from == move_space[i][0]:
      print("TEST - 1")
      if move_to == move_space[i][1]:
        print("TEST - 2")
        return True

  return False

  #----

def clean(delete, moves_structure):

  kept = []

  cleaned = tuple(delete)
  for i in range(len(moves_structure)):
    if moves_structure[i][0] != cleaned:
      kept.append(moves_structure[i])
    else:
      print(moves_structure[i][0], cleaned)

  return kept

  #----

def pawn(create, White_Playing):
  #from inital, collect the x and y components 

  create_x, create_y = create[0], create[1]

  #Hence, create a tuple containing new moves 

  new = []

  if White_Playing:
    create_y -= 1
    temp = (create_x, create_y)  

    #Add any additional conditions - Capture; enpassant 
  else: 
    create_y += 1
    temp = (create_x, create_y)   
    #Add any additional conditions - Caputre; enpassant 

  temp = (create, tuple(temp))
  new.append(temp)

  return new

  #-----

def straight(create):
  #from inital, collect the x and y components

  create_x, create_y = create[0], create[1]

  #Hence, create a tuple of new moves

  new = []

  x_pointer = create_x
  while x_pointer < 7:
    x_pointer += 1
    temp = (x_pointer, create_y)  
    temp = (create, tuple(temp))
    new.append(temp)
  x_pointer = create_x
  while x_pointer > 0:
    x_pointer -= 1 
    temp = (x_pointer, create_y)
    temp = (create, tuple(temp))
    new.append(temp)

  y_pointer = create_y 
  while y_pointer < 7:
    y_pointer += 1
    temp = (create_x, y_pointer)  
    temp = (create, tuple(temp))
    new.append(temp)
  y_pointer = create_y
  while y_pointer > 0:
    y_pointer -= 1 
    temp = (create_x, y_pointer)  
    temp = (create, tuple(temp))
    new.append(temp)

  return new

  #----

#1. ----------- Board creation -------------------

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

board = [[B_Rook, B_Knig, B_Bish, B_Quee, B_King, B_Bish, B_Knig, B_Rook],
        [B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn, B_Pawn],
        [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
        [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
        [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
        [Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_, Empty_],
        [W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn, W_Pawn], 
        [W_Rook, W_Knig, W_Bish, W_Quee, W_King, W_Bish, W_Knig, W_Rook]]

Moves_Tuple = []
White_moves = [((0, 6), (0, 5)), ((0, 6), (0, 4)), ((1, 6), (1, 5)), ((1, 6), (1, 4)), ((2, 6), (2, 5)), ((2, 6), (2, 4)), ((3, 6), (3, 5)), ((3, 6), (3, 4)), ((4, 6), (4, 5)), ((4, 6), (4, 4)), ((5, 6), (5, 5)), ((5, 6), (5, 4)), ((6, 6), (6, 5)), ((6, 6), (6, 4)), ((7, 6), (7, 5)), ((7, 6), (7, 4))]
Black_moves = [((0, 1), (0, 2)), ((0, 1), (0, 2)), ((1, 1), (1, 2)), ((1, 1), (1, 2)),  ((2, 1), (2, 2)), ((2, 1), (2, 2)),  ((0, 1), (0, 2)), ((0, 1), (0, 2)),  ((0, 1), (0, 2)), ((0, 1), (0, 2)),  ((0, 1), (0, 2)), ((0, 1), (0, 2)),  ((0, 1), (0, 2)), ((0, 1), (0, 2)),  ((0, 1), (0, 2)), ((0, 1), (0, 2)),]

#2. ----------- Performing a move --------------------

Playing = True
print(np.matrix(board))
Time_Stamp = -1
while Playing:
  #Pass the turn to the next player 
  Time_Stamp += 1 
  White_Playing, Moves_Tuple = turn(Time_Stamp)

  #TESTS:
  print("TEST, White moves:", White_moves)
  print("TEST, Black moves:", Black_moves)

  # Asking the user for a move
  Valid = False
  print("OUTER LOOP")
  while not Valid:
    print("INNER LOOP")
    #Get inputs from users - using string literals to produce visual spacing
    move_from = input(f"location to move from, (x,y) {space*10}")
    move_to = input(f"location to move to, (x,y) {space*12}")     

    #Process accordingly and normalise
    move_to, move_from = action(move_to, move_from)

    print("TEST", move_to, move_from)

    #Perform exceptions; 
    Valid = legal(move_to, move_from, Moves_Tuple)
    absurd(move_to, move_from)


  #Printing inputs
  board = perform(move_to, move_from, board)

  print(np.matrix(board))