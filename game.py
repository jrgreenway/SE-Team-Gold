from tkinter import END
from typing import Callable
import pygame
from gameObject import GameObject
from buttons.button import Button
from metrics import Metrics
from oracle import Oracle
from scene import Scene
from scenes.sceneDrawer import scene_loader
from screens.avatarScreen import draw_avatar_screen
from screens.endOfDayScreen import draw_end_of_day_screen
from screens.gameScreen import draw_game_screen
from screens.loadScreen import draw_load_screen
from screens.oracleAnswerScreen import draw_oracle_answer_screen
from screens.oracleQuestionScreen import draw_oracle_question_screen
from screens.pauseScreen import draw_pause_screen
from screens.screenConstants import *
from screens.startScreen import draw_start_screen

from screens.welcomeScreen import draw_welcome_screen

from player import Player

daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
    def __init__(
            self, 
            screen: pygame.Surface, 
            player: Player, 
            defaultScene: Scene, 
            buttonCBs: dict[str, Callable], 
            savedGames: list[str],
    ) -> None:
        self.screen = screen
        self.currentFrame = 0
        self.currentScreen = WELCOME_SCREEN
        self.running = True
        self.player = player
        self.currentScene = defaultScene
        self.defaultScene = defaultScene
        self.holdingKeys = []
        self.oracle = Oracle(screen, callBacks=buttonCBs)

        self.textAnimationStartFrame = 0

        self.buttonCBs = buttonCBs
        self.savedGames = savedGames

        self.dayEndFrame = 0

        self.scrollPos = 0
        self.keyDown = False

        self.currentDay = "Monday"

    def setSavedGames(self, savedGames: list[str]) -> None:
        self.savedGames = savedGames

    def nextDay(self):
        self.currentDay = daysOfWeek[(daysOfWeek.index(self.currentDay) + 1) % len(daysOfWeek)]
        self.currentScene = self.defaultScene

    def loadPlayer(self, playerName: str, playerGender: str, playerPosition: pygame.Vector2, speed: int) -> None:
        self.player.setName(playerName)
        self.player.setGender(playerGender)
        self.player.setPosition(playerPosition)
        self.player.setSpeed(speed)
    
    def loadMetrics(self, happiness: int, time: int, health: int, money: int) -> None:
        self.player.setMetrics(
            happiness=happiness,
            time=time,
            health=health,
            money=money
        )

    def setcurrentFrame(self, currentFrame):
        self.currentFrame = currentFrame

    def checkMoving(self):
        if pygame.K_w in self.holdingKeys or pygame.K_s in self.holdingKeys or \
            pygame.K_a in self.holdingKeys or pygame.K_d in self.holdingKeys:
            return True
        else:
            return False

    def setCurrentScreen(self, currentScreen: str) -> None:
        self.currentScreen = currentScreen

    def setCurrentScene(self, currentScene: Scene) -> None:
        self.currentScene = currentScene

    def setCurrentDay(self, currentDay: str) -> None:
        self.currentDay = currentDay

    def awaitExitWelcomeScreen(self) -> None:
        ''' Game.awaitExitWelcomeScreen() -> None
        Waits for the user to press the space bar to exit the welcome screen
        '''
        keys = pygame.key.get_pressed()
        # TODO improve with events instead of keys
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
                    self.running, self.currentScreen = clicked[0].onClick(game=self)

    def welcomeScreen(self) -> None:
        ''' Game.welcomeScreen() -> None
        Draws the welcome screen and waits for the user to press the space bar to exit
        '''
        draw_welcome_screen(self.screen, self.currentFrame)
        self.awaitExitWelcomeScreen()

    def startScreen(self, events) -> None:
        ''' Game.startScreen(events) -> None
        Draws the start screen and handles mouse clicks on the buttons
        '''
        buttons = draw_start_screen(self.screen, startCB=self.buttonCBs['start'], loadCB=self.buttonCBs['load'], exitCB=self.buttonCBs['exit'])
        self.handleMoseClicksStartScreen(events, buttons)

    def handleAvatarScreenEvents(self, events, buttons) -> None:
        ''' Game.handleAvatarScreenEvents(events, buttons) -> None
        Handles mouse clicks on the avatar screen
        '''
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.player.setName(self.player.getName()[:-1])
                else:
                    self.player.setName(self.player.getName() + event.unicode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(
                        currentScreen=self.currentScreen,
                        player = self.player
                    )

    # TODO these will be moved to Player Class
    def setMale(self, **_) -> tuple[bool, str]:
        self.player.setGender("M")
        return True, self.currentScreen

    # TODO these will be moved to Player Class
    def setFemale(self, **_) -> tuple[bool, str]:
        self.player.setGender("F")
        return True, self.currentScreen

    def createAvatarScreen(self, events) -> None:
        ''' Game.createAvatarScreen(events) -> None
        Draws the create avatar screen and handles mouse clicks on the buttons
        '''

        # todo go back to callbacks if this works
        buttons = draw_avatar_screen(
            self.screen, 
            self.player.getName(),
            self.player.getGender(),
            onMaleSelected=self.setMale,
            onFemaleSelected=self.setFemale,
            backCB=self.buttonCBs['back'],
            startGameCB=self.buttonCBs['startGame']
        )

        self.handleAvatarScreenEvents(events, buttons)

    def createGameScreen(self, events) -> None:
        ''' Game.createGameScreen(events) -> None
        Draws the game screen and handles mouse clicks on the buttons
        '''
        draw_game_screen(self.screen, self.currentScene)

        #Pass objects into the player.move method
        objects = self.currentScene.getObjects()
        self.player.move(self.holdingKeys, objects)
        navigateto = self.player.interact(self.holdingKeys, self.giveInteractable())
        if navigateto:
            self.currentScene = scene_loader(navigateto)
        else: 
            self.player.interact(self.holdingKeys, self.giveInteractable())
        self.player.animate(self.checkMoving(), self.currentFrame)
        self.player.draw(self.currentDay)
        oracleButton = self.oracle.draw(self.player.getMetrics(), self.currentFrame)
        self.handleGameScreenEvents(events, [oracleButton])

    def handleGameScreenEvents(self, events, buttons: list[Button]) -> None:
        ''' Game.handleGameScreenEvents(events) -> None
        Handles mouse clicks on the game screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(
                        game=self, 
                        currentScreen=self.currentScreen,
                        oracle=self.oracle,
                        question=None
                    )
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not self.keyDown:
                    self.currentScreen = PAUSE_SCREEN
                    self.keyDown = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.keyDown = False

    def createPauseScreen(self, events) -> None:
        ''' Game.createPauseScreen(events) -> None
        Draws the pause screen and handles mouse clicks on the buttons
        '''
        # draw the game screen so we can display the overlay effect
        draw_game_screen(self.screen, self.currentScene)
        self.player.draw(self.currentDay)
        buttons = draw_pause_screen(self.screen, self.buttonCBs['save'], self.buttonCBs['exit'], self.buttonCBs['backToMainMenu'])
        self.handlePauseScreenEvents(events, buttons)

    def handlePauseScreenEvents(self, events, buttons) -> None:
        ''' Game.handlePauseScreenEvents(events, buttons) -> None
        Handles mouse clicks on the pause screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(game=self, currentScreen=self.currentScreen)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not self.keyDown:
                    self.currentScreen = GAME_SCREEN
                    self.keyDown = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.keyDown = False

    def createLoadScreen(self, events) -> None:
        ''' Game.createLoadScreen(events) -> None
        Draws the load screen and handles mouse clicks on the buttons
        '''
        buttons = draw_load_screen(
            self.screen, 
            self.savedGames, 
            loadGameCB=self.buttonCBs['loadGame'], 
            scrollPos=self.scrollPos,
            backCB=self.buttonCBs['back']
        )
        self.handleLoadScreenEvents(events, buttons)

    def handleLoadScreenEvents(self, events, buttons) -> None:
        ''' Game.handleLoadScreenEvents(events, buttons) -> None
        Handles mouse clicks on the load screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                index = buttons.index(clicked[0]) if len(clicked) > 0 else -1
                if len(clicked) > 0 and event.button == 1:
                    self.running, self.currentScreen = clicked[0].onClick(
                        game=self, 
                        currentScreen=self.currentScreen,
                        gameName=self.savedGames[index] if index < len(self.savedGames) else None
                    )
                if event.button == 4:
                    self.scrollPos = max(0, self.scrollPos - 1)
                elif event.button == 5:
                    self.scrollPos = min(len(self.savedGames) - 1, self.scrollPos + 1)

    def drawQuestionScreen(self, events) -> None:
        ''' Game.drawQuestionScreen(events) -> None
        Draws the question screen and handles mouse clicks on the buttons
        '''
        draw_game_screen(self.screen, self.currentScene)
        self.player.draw(self.currentDay)
        buttons = draw_oracle_question_screen(
            self.screen, 
            self.oracle.getQuestions(), 
            self.buttonCBs['clickOracleQuestion'],
            self.buttonCBs['back']
        )
        self.handleQuestionScreenEvents(events, buttons)

    def handleQuestionScreenEvents(self, events, buttons) -> None:
        ''' Game.handleQuestionScreenEvents(events, buttons) -> None
        Handles mouse clicks on the question screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                index = buttons.index(clicked[0]) if len(clicked) > 0 else -1
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(
                        game=self, 
                        currentScreen=self.currentScreen,
                        oracle=self.oracle,
                        question=self.oracle.getQuestions()[index] if index < len(self.oracle.getQuestions()) else None
                    )

    def drawAnswerScreen(self, events) -> None:
        draw_game_screen(self.screen, self.currentScene)
        self.player.draw(self.currentDay)
        buttons = draw_oracle_answer_screen(
            self.screen,
            self.oracle.getAnswer(),
            self.buttonCBs['back'],
            self.buttonCBs['closeOracle'],
            self.textAnimationStartFrame,
            self.currentFrame
        )
        self.handleAnswerScreenEvents(events, buttons)

    def handleAnswerScreenEvents(self, events, buttons) -> None:
        ''' Game.handleAnswerScreenEvents(events, buttons) -> None
        Handles mouse clicks on the answer screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(
                        currentScreen=self.currentScreen,
                        oracle=self.oracle,
                    )

    def createDayEndScreen(self, events) -> None:
        ''' Game.createDayEndScreen(events) -> None
        Draws the end of day screen and handles mouse clicks on the buttons
        '''
        buttons = draw_end_of_day_screen(
            self.screen,
            self.dayEndFrame, 
            self.currentFrame, 
            self.player.getOldMetrics(),
            self.player.getMetrics(),
            self.buttonCBs['nextDay']
        )
        self.handleDayEndScreenEvents(events, buttons)


    def handleDayEndScreenEvents(self, events, buttons) -> None:
        ''' Game.handleDayEndScreenEvents(events, buttons) -> None
        Handles mouse clicks on the end of day screen
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [button for button in buttons if button.rect.collidepoint(event.pos)]
                if len(clicked) > 0:
                    self.running, self.currentScreen = clicked[0].onClick(
                        player = self.player,
                        oracle = self.oracle,
                        game = self
                    )

    def handleCurrentScreen(self, events) -> None:
        ''' Game.handleCurrentScreen(events) -> None
        Handles the current screen
        '''

        if self.currentScreen is not ORACLE_ANSWER_SCREEN:
            self.textAnimationStartFrame = 0
        if self.currentScreen is not DAY_END_SCREEN:
            self.dayEndFrame = 0

        if self.currentScreen == WELCOME_SCREEN:
            self.welcomeScreen()
        elif self.currentScreen == START_SCREEN:
            self.startScreen(events)
        elif self.currentScreen == CREATE_AVATAR_SCREEN:
            self.createAvatarScreen(events)
        elif self.currentScreen == GAME_SCREEN:
            self.createGameScreen(events)
        elif self.currentScreen == PAUSE_SCREEN:
            self.createPauseScreen(events)
        elif self.currentScreen == LOAD_SCREEN:
            self.createLoadScreen(events)
        elif self.currentScreen == ORACLE_QUESTION_SCREEN:
            self.drawQuestionScreen(events)
        elif self.currentScreen == ORACLE_ANSWER_SCREEN:
            if self.textAnimationStartFrame == 0:
                self.textAnimationStartFrame = self.currentFrame
            self.drawAnswerScreen(events)
        elif self.currentScreen == DAY_END_SCREEN:
            if self.dayEndFrame == 0:
                self.dayEndFrame = self.currentFrame
            self.createDayEndScreen(events)
        else:
            raise Exception("Invalid Screen")
        
    def toJson(self) -> dict:
        ''' Game.toJson() -> dict
        Returns a dictionary representation of the game
        '''
        return {
            'currentScreen': self.currentScreen,
            'currentScene': self.currentScene.getID(),
            'currentDay': self.currentDay,
            'player': self.player.toJson()
        }
    

    def giveInteractable(self):
        ''' Game.giveInteractable() -> gameObject|None
        Returns the closest interactable object in the interaction threshold
        TODO add facing right direction condition
        '''
        objects = self.currentScene.getInteractableObjects()
        if objects == []:
            return None
        player_position = self.player.getPosition()
        distance_to_func = lambda obj: player_position.distance_to(obj.getHitbox().center)
        close_object = min(objects, key=distance_to_func)
        if distance_to_func(close_object) <= self.player.interaction_threshold:
            return close_object
        else: return None
        

    def start(self) -> None:
        ''' Game.start() -> None
        Starts the game loop
        '''
        clock = pygame.time.Clock()

        # pygame.mixer.init()
        # pygame.mixer.music.load("assets/audio/soundtrack.mp3")
        # pygame.mixer.music.play(-1)

        # Game loop
        while self.running:
            self.currentFrame += 1
            
            if self.currentFrame % 60 == 0 and self.currentScreen == GAME_SCREEN:
                self.currentScreen = self.player.metrics.updateTime() and DAY_END_SCREEN or GAME_SCREEN
            
            # self.currentFrame %= 60
            # Handle events - keyPresses
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key not in self.holdingKeys:
                    self.holdingKeys.append(event.key)
                elif event.type == pygame.KEYUP:
                    self.holdingKeys.remove(event.key)
            # Update game state
            self.handleCurrentScreen(events)
            pygame.display.flip()
            clock.tick(60)

    def get_game_state(self):
        player_name = self.player.getName()
        day_of_week = self.currentDay
        player_time = self.player.getMetrics().formatTime()
        game_state = f"{player_name}, {day_of_week}, {player_time}"
        return game_state
