
import pygame

from game import Game

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 640))

# Set up the scenes and objects - will use a json for this

# Create the player

# Create the game TODO add the scenes, player, etc. to the constructor
game = Game(screen)
game.start()

pygame.quit()
