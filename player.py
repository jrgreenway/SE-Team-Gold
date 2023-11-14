import pygame

class Player:
    ''' Player Class for the Avatar - could be renamed later
    
    Attributes:
    name: str
    position: tuple - current position on screen (x, y) or pygame Vector2 - TODO research
        which is best
    facing: str - direction the player is facing (N, S, E, W)
    speed: int / float - TODO decide on units
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

    def __init__(self) -> None:
        self.facing = "S"
        # animations is dict with keys S, N, E, W
        # every key has a list of sprites as its value
        self.loadAnimations()
        self.sprite = self.animations[self.facing][0]

    #Animate method (returns next sprite image)
    #Each walking animation in each direction had a 4 frame animation (1st and 3rd being the same image)
    #Sprite will have 12 images (3 for each direction) named (D1, D2, D3 (walking down), U1, U2, U3, (walking up)...)
    #Standing image will be D1 (first and 3rd frame of walking down animation)

    # TODO - include images in assets folder
    def loadAnimations(self) -> None:
        #Arrays of all of the images for the animation
        prefix = "assets/animations/"
        walkDown = [
            pygame.image.load(prefix + 'S_' + self.gender + "/S0.gif"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S1.gif"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S0.gif"),
            pygame.image.load(prefix + 'S_' + self.gender + "/S2.gif"),
        ]

        walkUp = [
            pygame.image.load(prefix + 'N_' + self.gender + "/N0.gif"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N1.gif"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N0.gif"),
            pygame.image.load(prefix + 'N_' + self.gender + "/N2.gif"),
        ]

        walkRight = [
            pygame.image.load(prefix + 'E_' + self.gender + "/E0.gif"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E1.gif"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E0.gif"),
            pygame.image.load(prefix + 'E_' + self.gender + "/E2.gif"),
        ]

        walkLeft = [
            pygame.image.load(prefix + 'W_' + self.gender + "/W0.gif"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W1.gif"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W0.gif"),
            pygame.image.load(prefix + 'W_' + self.gender + "/W2.gif"),
        ]

        self.animations = {"S": walkDown, "N": walkUp, "E": walkRight, "W": walkLeft}

    def animate(self, moving:bool, currentFrame) -> None:
        if not moving:
            self.sprite = self.animations[self.facing][0]
        else:
            #Each image lasts 15 frames so animation loops every 60 frames (maybe be too fast - will have to see when testing)))
            self.sprite = self.animations[self.facing][(currentFrame//15) % 4]
