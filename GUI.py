import pygame
import sys
import time 
import chessAI as chess


pygame.init()
size = width, height = 600, 400

#Colors 
black = (0, 0, 0)
white = (255, 255, 255)
green = (80, 80, 80)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font(None, 28)
largeFont = pygame.font.Font(None, 40)
moveFont = pygame.font.Font(None, 60)


user = None 
board = chess.inital_state()
white_turn = False

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  screen.fill(green)

  #Simple menu; let user choose a player
  if user is None:

    # Draw title
    title = largeFont.render("Play Chess?", True, white)
    titleRect = title.get_rect()
    titleRect.center = ((width / 2), 50)
    screen.blit(title, titleRect)

    # Draw buttons 
    playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)

    playW = mediumFont.render("Play as White?", True, black)
    playWRect = playW.get_Rect()
    playWRect.center = playWButton.center
    pygame.draw.rect(screen, white, playWButton)
    screen.blit(playW, playWRect)

    playBButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
    playB = mediumFont.render("Play as Black", True, black)
    playBRect = playB.get_rect()
    playBRect.center = playBButton.center
    pygame.draw.rect(screen, white, playBButton)
    screen.blit(playB, playBRect)







