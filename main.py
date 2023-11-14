
import pygame

from game import Game
from player import Player

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set up the scenes and objects - will use a json for this

# Create the player

player = Player("F", screen, "S")

# Create the game TODO add the scenes, player, etc. to the constructor
game = Game(screen, player)
game.start()

pygame.quit()
