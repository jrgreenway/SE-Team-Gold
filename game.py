import pygame


class Game:
    '''
    Contains the game loop and the main game state.
    
    Attributes:
    screen: pygame.display - the display that the game is drawn to
    scenes: list - list of all scenes in the game
    currentScene: Scene - the scene that the player is currently in
    player: Player - the player object
    currentFrame: int - the current frame of the animation
    moving: Boolean - whether the player is moving or not - updated by keyPress events
    interactableObject: GameObject - the object that the player can interact with

    Methods:
    constructor: __init__(self, scenes, currentScene, player, ...) - TODO decide
        on optional parameters
    getters and setters for all attributes
    start: start(self) - starts the game loop
    drawScene: drawScene(self) - draws the current scene to the screen with its objects
        and NPCs
    drawPlayer: drawPlayer(self, currentFrame, moving) - draws the player to the screen
    movePlayer: movePlayer(self, direction) - moves the player in the direction of the keyPress
    findInteractable: findInteractable(self) - finds the closest object to the player that
        can be interacted with - every frame go through the scene's objects and check if they can
        be interacted with - will cause the names of interactable objects to be displayed on them
        also updates the interactableObject attribute
    interact: interact(self) - calls the interact method of the player class with the 
        interactableObject as the parameter upon SpaceBar keyPress
    '''


    # Temporary Constructor for testing purposes
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.currentFrame = 0

    def setcurrentFrame(self, currentFrame):
        self.currentFrame = currentFrame

    def start(self) -> None:
        '''
        Starts the game loop
        '''

        clock = pygame.time.Clock()


        # Game loop
        running = True
        while running:
            # Handle events - keyPresses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Update game state
            
            # Draw to the screen
            self.screen.fill((255, 255, 255))
            pygame.display.flip()
            clock.tick(60)
            self.setcurrentFrame(self.currentFrame+1)

