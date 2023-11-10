import pygame
from screens.screenConstants import START_SCREEN, WELCOME_SCREEN, nextScreen

from screens.welcomeScreen import draw_welcome_screen


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
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.currentScreen = WELCOME_SCREEN
        self.frame = 0

    def awaitExitWelcomeScreen(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.currentScreen = nextScreen(self.currentScreen)

    def welcomeScreen(self) -> None:
        draw_welcome_screen(self.screen, self.frame)
        self.awaitExitWelcomeScreen()

    def handleCurrentScreen(self) -> None:
        if self.currentScreen == WELCOME_SCREEN:
            self.welcomeScreen()
        elif self.currentScreen == START_SCREEN:
            pass
        else:
            raise Exception("Invalid Screen")
        
    def start(self) -> None:
        '''
        Starts the game loop
        '''
        self.frame = 0
        # Game loop
        running = True
        while running:
            # Handle events - keyPresses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Update game state
            self.handleCurrentScreen()

            # Draw to the screen
            # self.screen.fill((255, 255, 255))
            pygame.display.flip()
            self.frame += 1
            self.frame %= 60
            self.clock.tick(60)