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

    #Animate method (returns next sprite image)
    #Each walking animation in each direction had a 4 frame animation (1st and 3rd being the same image)
    #Sprite will have 12 images (3 for each direction) named (D1, D2, D3 (walking down), U1, U2, U3, (walking up)...)
    #Standing image will be D1 (first and 3rd frame of walking down animation)

    def animate(self, moving:bool, currentFrame)：
        #Arrays of all of the images for the animation
        walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D1.png'), pygame.image.load('D3.png')]
        walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U1.png'), pygame.image.load('U3.png')]
        walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R1.png'), pygame.image.load('R3.png')]
        walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L1.png'), pygame.image.load('L3.png')]
    
        if not moving:
            return walkDown[0]
        else:
            if self.facing == "S":
                return walkDown[(currentFrame//5)%4] #Each image lasts 5 frames so animation loops every 20 frames (maybe be too fast - will have to see when testing)))
            elif self.facing == "N":
                return walkUp[(currentFrame//5)%4] 
            elif self.facing == "E":
                return walkRight[(currentFrame//5)%4]
            elif self.facing == "W":
                return walkLeft[(currentFrame//5)%4]
