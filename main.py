#Chess AI / simulation - CodeAvali

from collections.abc import ValuesView
import math 
import copy 
import sys 
import random
import copy

#Define temp pecies using ASCII art - modified for pygame front
TURNS = 0 
EMPTY = ' '
BKING = "♚"
WKING = "♔"
BQUEE = "♛"
WQUEE = "♕"
BBISH = "♝"
WBISH = "♗"
BKNIG = "♞"
WKNIG = "♘"
BROOK = "♜"
WROOK = "♖"
BPAWN = "♟︎"
WPAWN = "♙"



def inital_state():
  # Returns starting state of the board
  return [[BROOK, BKNIG, BBISH, EMPTY, BQUEE, BBISH, BKNIG, BROOK],
          [BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN], 
          [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
          [WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN],
          [WROOK, EMPTY, WBISH, WKING, EMPTY, WBISH, WKNIG, WROOK]]


def temp_display(board):
  #board = inital_state()
  for line in board:
    print(line)

def player(count):
  # Returns player who has the next turn on the board 
  count += 1
  if count % 2 == 1:
    return True
  else:
    return False

def result(board, peice, move):
  #Returns board after taking move (i, j)

  i = peice[0]
  j = peice[1]

  #Check if the move is valid

  #Then
  peice = board[i][j]
  board_copy = copy.deepcopy(board)
  board_copy[i][j] = peice

  return board_copy

###############################################

def utility(board, count):
  white_turn = player(count)
  black_utility = 0 
  white_utility = 0 

  #Point conditions, - set ACC to tournment norms 
  w_items = ['♔','♕','♖','♗','♘','♙']
  b_items = ['♚','♛','♜','♝','♞','♟︎']
  apoints = [40, 9, 5, 3, 3, 1]
  
  #Other AI Actions/priorities;
  #DEVELOP = 0.2    

  for i in range(8):
    for j in range(8):
      location = board[i][j]
      if str(location) in w_items:
        for temp in range(len(w_items)):
          if str(location) == w_items[temp]:
            score = apoints[temp]
            white_utility += score
      elif str(location) in b_items:
        for temp in range(len(b_items)):
          if str(location) == b_items[temp]:
            score = apoints[temp]
            black_utility += score

  print(white_utility, black_utility)
  print("SCORE:", white_utility - black_utility)
          

        

    
  
#################################################

def terminal(board):

  white = False
  black = False

  for i in range(8):
    for j in range(8):

      location = board[i][j]

      if str(location) == "♔":
        white = True
      elif str(location) == "♚":
        black = True

  print(white, black)
  #return white, black 
        

#################################################

def actions(board, count):
  #Returns all possible actions for a state

  #1. Determine current turn 
  white_turn = player(count)

  #Hence, create a tuple list of all (i, j) moves

  # - - - - King movement - - - - 
  #  OOO
  #  OXO
  #  000


  # - - - - Queen movement
  #  O-O-O
  #  -OOO-
  #  00X00
  #  -000-
  #  0-O-O


  # - - - - Rook movement 
  #  --O--
  #  --O--
  #  OOXOO
  #  --0--
  #  --O--


  # - - - - Bishop movement 
  #  O---O
  #  -O-O-
  #  --X--
  #  -O-O-
  #  O---O


  # - - - - Knight movement 
  #  -O-O-
  #  O---O
  #  --X--
  #  O---O
  #  -O-O-


  # - - - - Pawn movement 
  # -A*A-
  # --O--
  # --X-- 
  


  




################################





def minimax(board):
  print('Hello minimax!')

### TEMP - main program ###


board = inital_state()
#print(board)
#board = result(board, (7,1), (4,4))
#print(board)
temp_display(board)
count = 0 
utility(board, count)
terminal(board)

for i in range(10):
  print(player(count))
  count += 1






#####
#TO DO -
#1. Program utility function to take into account Values
#2. Allow for moves
#3. Check for checkmate

#THEN

#1. Implement basic ai
#2. Implement pygame solution

#EXT:

#1. Introduce learning function
#2. Allowing for adaptive
#3. Tourneys/Training against AI