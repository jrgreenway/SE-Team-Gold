
import pygame
from requests import get
from buttons.buttonCallbacks import createButtonCBDict

from game import Game
from player import Player
from scenes.sceneDrawer import scene_loader
from utils.gameLoader import get_saved_games, load_game
from utils.gameSaver import save_game

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 640))

# Set up the scenes and objects - will use a json for this
defaultScene = scene_loader(1) # use default scene 1 for now
# Create the player
player = Player(gender="F", screen=screen, facing="S")

# Create the game TODO add the scenes, player, etc. to the constructor

game = Game(screen, player, defaultScene, createButtonCBDict(), get_saved_games())

# initialize the callbacks
game.start()

pygame.quit()
