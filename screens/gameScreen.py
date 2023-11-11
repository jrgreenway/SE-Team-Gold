import pygame

from scenes.sceneDrawer import scene_drawer

# TODO the currentScene may be changed to a string later
def draw_game_screen(screen: pygame.Surface, currentScene: int) -> None:
    ''' drawGameScreen: pygame.Surface, int -> None
    Draws the game screen to the screen
    '''
    scene_drawer(screen, currentScene)