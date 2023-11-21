import json
from typing import Optional
import pygame
from gameObject import GameObject


from metrics import Metrics

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
                screen: pygame.Surface,
                name:str = "James",
                gender: str = "F",
                facing:str="S",
                speed=3
    ) -> None:
        self.name = name
        self.screen = screen
        self.position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.facing = facing
        self.speed = speed
        self.gender = gender
        self.metrics = Metrics(15, 0, 0, 10)
        self.interaction_threshold = 128
        self.not_interacting = True

        # animations is dict with keys S, N, E, W
        # every key has a list of sprites as its value
        self.loadAnimations()
        self.sprite = self.animations[self.facing][0]
    
    def reset(self) -> None:
        self.position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    #Getters

    def getName(self) -> str:
        return self.name
    
    def getGender(self) -> str:
        return self.gender
    
    def getPosition(self):
        return self.position
    
    def getFacing(self):
        return self.facing
    
    def getMetrics(self):
        return self.metrics
    
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

    def setGender(self, gender: str):
        self.gender = gender
    
    #Methods

    def interact(self, holdingKeys, object: Optional[GameObject]=None):#TODO sort out event that happens as a result of key press
        if holdingKeys.count(pygame.K_e) == 0:
            self.not_interacting = True
        
        canInteract = pygame.K_e in holdingKeys and self.not_interacting \
                        and object is not None #and facing direction
        if canInteract:
            self.not_interacting = False
            self.metrics.changeMetrics(object.getHappinessEffect(), object.getTimeEffect(), object.getHealthEffect())
            #print(f"interacted with {object.getID()}")

    # TODO find which type of Event to import
    def move(self, holdingKeys):#call in main loop.
        # TODO retrieve events only once in game main loop and pass them as
        # parameters to subsequent methods to avoid double triggers.
        for key in holdingKeys:
            if key == pygame.K_w:
                self.position.y -= self.speed  # Move up
                self.facing = "N"
            elif key == pygame.K_s:
                self.position.y += self.speed  # Move down
                self.facing = "S"
            elif key == pygame.K_a:
                self.position.x -= self.speed  # Move left
                self.facing = "W"
            elif key == pygame.K_d:
                self.position.x += self.speed  # Move right
                self.facing = "E"

    #Animate method (returns next sprite image)
    #Each walking animation in each direction had a 4 frame animation (1st and 3rd being the same image)
    #Sprite will have 12 images (3 for each direction) named (D1, D2, D3 (walking down), U1, U2, U3, (walking up)...)
    #Standing image will be D1 (first and 3rd frame of walking down animation)

    # TODO - include images in assets folder
    def loadAnimations(self) -> None:
        #Arrays of all of the images for the animation
        prefix = "assets/animations/"
        walkDown = [
            pygame.image.load(prefix + 'S_' + self.gender + "/S0.png"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S1.png"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S0.png"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S2.png"),
        ]

        walkUp = [
            pygame.image.load(prefix + 'N_' + self.gender + "/N0.png"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N1.png"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N0.png"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N2.png"),
        ]

        walkRight = [
            pygame.image.load(prefix + 'E_' + self.gender + "/E0.png"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E1.png"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E0.png"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E2.png"),
        ]

        walkLeft = [
            pygame.image.load(prefix + 'W_' + self.gender + "/W0.png"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W1.png"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W0.png"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W2.png"),
        ]

        self.animations = {"S": walkDown, "N": walkUp, "E": walkRight, "W": walkLeft}

    def animate(self, moving:bool, currentFrame) -> None:
        if not moving:
            self.sprite = self.animations[self.facing][0]
        else:
            #Each image lasts 15 frames so animation loops every 60 frames (maybe be too fast - will have to see when testing)))
            self.sprite = self.animations[self.facing][(currentFrame//15) % 4]

    def draw(self) -> None:
        self.screen.blit(self.sprite, (int(self.position.x), int(self.position.y)))
        font = pygame.font.Font(None, 24)
        text = font.render(self.metrics.formatTime(), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (self.screen.get_width() - 10, 10)
        self.screen.blit(text, text_rect)

    def toJson(self) -> dict:
        player_dict = {
            "name": self.name,
            "gender": self.gender,
            "facing": self.facing,
            "speed": self.speed,
            "position": {
                "x": self.position.x, 
                "y": self.position.y
            }
        }
        return player_dict

