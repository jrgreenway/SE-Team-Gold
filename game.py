import pygame
from screens.avatarScreen import draw_avatar_screen
from screens.screenConstants import CREATE_AVATAR_SCREEN, START_SCREEN, WELCOME_SCREEN, nextScreen
from screens.startScreen import draw_start_screen

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
        self.running = True
        self.playerName = "" # TODO this will be linked with the Player Class
        self.playerGender = "male" # TODO this will be linked with the Player Class

    def awaitExitWelcomeScreen(self) -> None:
        ''' Game.awaitExitWelcomeScreen() -> None
        Waits for the user to press the space bar to exit the welcome screen
        '''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.currentScreen = nextScreen(self.currentScreen)

    def handleMoseClicksStartScreen(self, events, buttons) -> None:
        ''' Game.handleMoseClicksStartScreen(events, buttons) -> None
        Handles mouse clicks on the start screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick()

    def welcomeScreen(self) -> None:
        ''' Game.welcomeScreen() -> None
        Draws the welcome screen and waits for the user to press the space bar to exit
        '''
        draw_welcome_screen(self.screen, self.frame)
        self.awaitExitWelcomeScreen()

    def startScreen(self, events) -> None:
        ''' Game.startScreen(events) -> None
        Draws the start screen and handles mouse clicks on the buttons
        '''
        buttons = draw_start_screen(self.screen)
        self.handleMoseClicksStartScreen(events, buttons)

    def handleAvatarScreenEvents(self, events, buttons) -> None:
        ''' Game.handleAvatarScreenEvents(events, buttons) -> None
        Handles mouse clicks on the avatar screen
        '''
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.playerName = self.playerName[:-1]
                else:
                    self.playerName += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(currentScreen=self.currentScreen)

    # TODO these will be moved to Player Class
    def setMale(self, **k) -> tuple[bool, str]:
        self.playerGender = "male"
        return True, self.currentScreen

    # TODO these will be moved to Player Class
    def setFemale(self, **_) -> tuple[bool, str]:
        self.playerGender = "female"
        return True, self.currentScreen

    def createAvatarScreen(self, events) -> None:
        ''' Game.createAvatarScreen(events) -> None
        Draws the create avatar screen and handles mouse clicks on the buttons
        '''

        # todo go back to callbacks if this works
        buttons = draw_avatar_screen(
            self.screen, 
            self.playerName,
            self.playerGender,
            onMaleSelected=self.setMale,
            onFemaleSelected=self.setFemale
        )

        self.handleAvatarScreenEvents(events, buttons)


    def handleCurrentScreen(self, events) -> None:
        ''' Game.handleCurrentScreen(events) -> None
        Handles the current screen
        '''
        if self.currentScreen == WELCOME_SCREEN:
            self.welcomeScreen()
        elif self.currentScreen == START_SCREEN:
            self.startScreen(events)
        elif self.currentScreen == CREATE_AVATAR_SCREEN:
            self.createAvatarScreen(events)
        else:
            raise Exception("Invalid Screen")
        
    def start(self) -> None:
        ''' Game.start() -> None
        Starts the game loop
        '''
        self.frame = 0
        # Game loop
        while self.running:
            # Handle quit event
            events = pygame.event.get()
            if pygame.QUIT in [event.type for event in events]:
                self.running = False

            # Update game state
            self.handleCurrentScreen(events)

            # Draw to the screen
            pygame.display.flip()
            self.frame += 1
            self.frame %= 60
            self.clock.tick(60)