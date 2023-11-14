from typing import Any
import pygame
from game import Game
class Player():
    ''' Player Class for the Avatar - could be renamed later
    
    Attributes:
    name: str
    position: pygame Vector2 - set with setPosition, otherwise default to centre of screen.
    facing: str - direction the player is facing (N, S, E, W)
    speed: int / float - grid unit per frame
    sprite: pygame.image / bmp? - TODO need to research - the sprite for the player 
        TODO could be a list of sprites for the animations?
    TODO - discuss whether metrics should be a dict / separate class / independent 
        variables
    money: int / float
    happiness: int / float
    time: int / float

    Methods:
    constructor: __init__(self, name, position, facing, sprite, ...metrics) - TODO decide
        on optional parameters
    getters and setters for all attributes
    move: move(self, direction) - updates the position of the character in the given 
        direction (which is the new value of facing)
    updateMetrics: updateMetrics(self, metric, value) - TODO this approach would work best
        if metrics is an interface probably
    interact: interactObject(self, object) - uses the object's attributes to update the metrics
        of the player
    animate: animate(self, currentFrame, moving: Boolean) - updates the sprite of the player
        based on the current frame and whether the player is moving or not - called on every
        frame in the game logic 
    '''
    def __init__(self,
                screen,
                name:str = "James",
                facing:str="S",
                speed=1
                ) -> None:
        self.name = self.setName(name)
        self.screen = screen
        self.position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.facing = facing
        self.speed = speed
        # temporary for testing
    
    #Getters

    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position
    
    def getFacing(self):
        return self.facing
    
    #Setters

    def setName(self, name: str):
        self.name = name

    def setPosition(self, position: pygame.Vector2):
        self.position = position
    
    def setFacing(self, facing:str):
        if facing in {"N", "E", "S", "W"}:
            self.facing = facing # could add a raise ValueError if not in {}.

    def setSpeed(self, speed: int):
        self.speed = speed
    
    #Methods

    def move(self):#call in main loop.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.position.y -= self.speed  # Move up
                elif event.key == pygame.K_DOWN:
                    self.position.y += self.speed  # Move down
                elif event.key == pygame.K_LEFT:
                    self.position.x -= self.speed  # Move left
                elif event.key == pygame.K_RIGHT:
                    self.position.x += self.speed  # Move right