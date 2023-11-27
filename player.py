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
        self.width = 200
        self.height = 200 
        self.hitbox = pygame.Rect(self.screen.get_width() / 6, self.screen.get_height() / 2, self.width//4, self.height//4)
        self.facing = facing
        self.speed = speed
        self.gender = gender

        #New
         
        self.oldMetrics = Metrics(money=10)
        self.metrics = Metrics()

        self.interaction_threshold = 128
        self.not_interacting = True
        self.close_object = None

        # animations is dict with keys S, N, E, W
        # every key has a list of sprites as its value
        self.loadAnimations()
        self.sprite = self.animations[self.facing][0]
        
        self.isDebug = False
    
    def reset(self) -> None:
        #So that the player sprite doesn't start on an object
        self.hitbox = pygame.Rect(self.screen.get_width() / 6, self.screen.get_height() / 2, self.width//4, self.height//4)

    def resetNextDay(self) -> None:
        if (self.metrics.getMoney() < self.oldMetrics.getMoney()):
            self.oldMetrics = self.metrics
            self.metrics.updateHappiness(-15)
        else:
            self.oldMetrics = self.metrics
        
        self.metrics.resetTime()
        self.reset()

    #Getters

    def getName(self) -> str:
        return self.name
    
    def getGender(self) -> str:
        return self.gender
    
    def getPosition(self):
        return pygame.Vector2(self.hitbox.centerx, self.hitbox.centery)
    
    def getFacing(self):
        return self.facing
    
    def getMetrics(self):
        return self.metrics
    
    def getOldMetrics(self):
        return self.oldMetrics
    
    #Setters

    def setName(self, name: str):
        self.name = name

    def setPosition(self, position: pygame.Vector2):
        self.hitbox = pygame.Rect(position.x, position.y, self.width//4, self.height//4)
    
    def setFacing(self, facing:str):
        if facing in {"N", "E", "S", "W"}:
            self.facing = facing

    def setSpeed(self, speed: int):
        self.speed = speed

    def setGender(self, gender: str):
        self.gender = gender
    
    #Methods

    def makePopUp(self):
        object = self.close_object
        buffer = 2
        icon_size = 18
        popup_size = ((icon_size+buffer)*4+buffer,(icon_size+buffer)*2+buffer)
        alpha = 200
        popup = pygame.Rect(self.hitbox.topright[0]+10, self.hitbox.topright[1]-100, popup_size[0], popup_size[1])
        popup_surface = pygame.Surface((popup.width, popup.height))
        popup_surface.fill((255, 255, 255, 200))
        popup_surface.set_alpha(alpha)
        self.screen.blit(popup_surface, popup.topleft)

        isPos = lambda x: 0 if x>0 else 1 if x==0 else 2 if -21<x<0 else 3
        isPosTime = lambda x: 0 if x<0 else 1 if x==0 else 2 if 91>x>0 else 3
        colours = [pygame.Color(0,100,0,alpha), pygame.Color(255,255,255,alpha), pygame.Color(255,192,0, alpha), pygame.Color(255,0,0,200)]#green,white,amber,red 

        obj_metrics = [object.getHappinessEffect(), object.getHealthEffect(), object.getTimeEffect(), object.getMoneyEffect()]
        metric_colours = [colours[isPos(obj_metrics[i])] for i in [0,1,3]]
        metric_colours.insert(2,colours[isPosTime(obj_metrics[2])])
        images = [pygame.image.load("assets/happy.png"), pygame.image.load("assets/health.png"), pygame.image.load("assets/clock.png"), pygame.image.load("assets/money.png")]

        locx, locy = popup.topleft
        locy+=buffer
        for colour, image in zip(metric_colours, images):
            container = pygame.Rect(locx+buffer,locy, icon_size, icon_size*2+buffer)
            locx,locy = container.topright
            image = pygame.transform.scale(image, (icon_size,icon_size))
            image.set_alpha(alpha)
            colour_surface = pygame.Surface((icon_size,icon_size))
            colour_surface.fill(colour)
            colour_surface.set_alpha(alpha)
            self.screen.blit(colour_surface, (container.bottomleft[0], container.bottomleft[1]-icon_size))
            self.screen.blit(image, container.topleft)


    def interact(self, holdingKeys, object: Optional[GameObject]=None):#TODO sort out event that happens as a result of key press
        
        if object is None:
            if self.close_object is not None:
                self.close_object = None
            return
        
        self.close_object = object #makes and sets close object to the parsed object to make pop up
        self.makePopUp()

        if holdingKeys.count(pygame.K_e) == 0:
            self.not_interacting = True
        
        canInteract = pygame.K_e in holdingKeys and self.not_interacting \
                        and object is not None #and facing direction
        # navigateTo = 1
        
        if canInteract:
            self.not_interacting = False
            self.metrics.changeMetrics(object.getHappinessEffect(), object.getTimeEffect(), object.getHealthEffect(), object.getMoneyEffect())
            # click_object = pygame.Rect()
            # if object.navigateTo():
            #     navigateTo = object.navigateTo()

            # for key in holdingKeys:
            #     x = self.position.x
            #     y = self.position.y
            #     mouse_clicked = pygame.mouse.get_pressed()[0]
            #     if key == mouse_clicked:
            #         for obj in object:
            #             pygame.draw.rect(self.screen, pygame.Rect(obj.getPosition().x, obj.getPosition().y, 128, 128), 2)
            #             if obj.navigateTo():
            #                 navigateTo = obj.navigateTo()

            
        return object.getNavigateTo() if canInteract else None


    # TODO find which type of Event to import
    def move(self, holdingKeys, objects: list[GameObject]):#call in main loop.
        # TODO retrieve events only once in game main loop and pass them as
        # parameters to subsequent methods to avoid double triggers.
        obstructedDirections = self.checkCollisionWithScreen()
        
        for key in holdingKeys:
            temp_x, temp_y = self.hitbox.topleft
               
            
            if key == pygame.K_w and "N" not in obstructedDirections:
                temp_y -= self.speed  # Move up
                self.facing = "N"
            elif key == pygame.K_s and "S" not in obstructedDirections:
                temp_y += self.speed  # Move down
                self.facing = "S"
            elif key == pygame.K_a and "W" not in obstructedDirections:
                temp_x -= self.speed  # Move left
                self.facing = "W"
            elif key == pygame.K_d and "E" not in obstructedDirections:
                temp_x += self.speed  # Move right
                self.facing = "E"
            
            # Do this here for scenario (obj to the right but both -> and up arrows are pressed so we still move up)    
            #Update hitbox position
            temp_hitbox = pygame.Rect(temp_x, temp_y, 64, 64)
            
            collisions = [obj for obj in objects if obj.isCollidable and temp_hitbox.colliderect(obj.getHitbox())]
            if collisions == []:
                self.hitbox = temp_hitbox
        
        if self.isDebug:
            # draw hitboxes around objects
            for obj in objects:
                pygame.draw.rect(self.screen, (255,0,0), obj.getHitbox(), 2)
    
    #After player has moved, check for collision
    #If collision is detected, check from which direction the collision is
    #Return the direction(s) which are obstructed by an object/the screen as a list
    def checkCollisionWithScreen(self) -> list[str]:
        obstructedDirections = []

        #Check collision with sides of the screen
        if self.hitbox.top < 0:
            obstructedDirections.append("N")
        if self.hitbox.bottom > self.screen.get_height():
            obstructedDirections.append("S")
        if self.hitbox.left < 0:
            obstructedDirections.append("W")
        if self.hitbox.right > self.screen.get_width():
            obstructedDirections.append("E")

        return obstructedDirections

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
            #Scaled the images for that the sprite is smaller
            self.sprite = pygame.transform.scale(self.animations[self.facing][0], (self.width, self.height))
        else:
            #Each image lasts 15 frames so animation loops every 60 frames (maybe be too fast - will have to see when testing)))
            self.sprite = pygame.transform.scale(self.animations[self.facing][((currentFrame % 60)//15) % 4], (self.width, self.height))

    def draw(self) -> None:
        blit_location = pygame.Vector2(self.hitbox.centerx - self.width/2, self.hitbox.centery-((3/4)*self.height))
        self.screen.blit(self.sprite, blit_location)
        font = pygame.font.Font(None, 24)
        text = font.render(self.metrics.formatTime(), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (self.screen.get_width() - 10, 10)
        self.screen.blit(text, text_rect)

        #Used to check the size of the hitbox
        if self.isDebug:
            pygame.draw.rect(self.screen, (255,0,0), self.hitbox, 2)

        self.metrics.draw(self.screen)

    def toJson(self) -> dict:
        player_dict = {
            "name": self.name,
            "gender": self.gender,
            "facing": self.facing,
            "speed": self.speed,
            "position": {
                "x": self.hitbox.centerx, 
                "y": self.hitbox.centery
            }
        }
        return player_dict

