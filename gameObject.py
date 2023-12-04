import os
import pickle
from typing import Optional
import pygame

class GameObject:
    '''
    The base class for all game objects. ex: laundry machine, oven, etc.
    
    Attributes:
    name: str - display name only when the player is close enough to interact with the object
    position: tuple - current position on screen (x, y) or pygame Vector2 - TODO research
        which is best - make sure it is consistent with the player class
    interactionThreshold: int / float - maximum distance from the player that the object can
        be interacted with
    sprite: pygame.image / bmp? - TODO need to research
    interactable: Boolean - whether the object can be interacted with or not currently (player
        is close enough)
    TODO - discuss whether metrics should be a dict / separate class / independent 
        variables
    effectOnMoney: int / float
    effectOnHappiness: int / float
    effectOnTime: int / float

    Methods:
    constructor: __init__(self, name, position, sprite, ...metrics) - TODO decide
        on optional parameters
    getters and setters for all attributes
    placeOnTop: placeOnTop(self, object) - places the object on top of the given object - updates
        the position of the object
    placeUnder: placeUnder(self, object) - places the object under the given object - updates
        the position of the object
    placeToRight: placeToRight(self, object) - places the object to the right of the given object -
        updates the position of the object
    placeToLeft: placeToLeft(self, object) - places the object to the left of the given object - 
        updates the position of the object
    checkInteractable: checkInteractable(self, player) - checks if the player is close enough to
        interact with the object - returns a boolean - if true update the interactable attribute
    '''

    def __init__(self, 
                 id: int,
                 happiness_effect=0,
                 health_effect=0,
                 time_effect=0,
                 money_effect=0,
                 next_day: bool=False,
                 navigateTo: Optional[int] = None,
                 interactive: bool=False,
                 position: pygame.Vector2 = pygame.Vector2(0, 0), 
                 sprite: Optional[pygame.Surface] = None,
                 isCollidable = True,
                 size: tuple = (128,128)
                 ) -> None:
        self.id = id
        self.position = position
        self.sprite = sprite
        self.interactive = interactive
        self.navigateTo = navigateTo
        self.happiness_effect = happiness_effect
        self.time_effect = time_effect
        self.next_day = next_day
        self.health_effect = health_effect
        self.money_effect = money_effect
        self.size = size # placeholder for if we make larger objects
        self.isCollidable = isCollidable

    def getID(self) -> int:
        return self.id
    
    def getInteractive(self):
        return self.interactive

    def getNavigateTo(self):
        return self.navigateTo
    
    def getHappinessEffect(self):
        return self.happiness_effect
    
    def getTimeEffect(self):
        return self.time_effect
    
    def getNextDay(self):
        return self.next_day
    
    def getHealthEffect(self):
        return self.health_effect
    
    def getMoneyEffect(self):
        return self.money_effect

    def getPosition(self) -> pygame.Vector2:
        return self.position
    
    def setPosition(self, position: pygame.Vector2) -> None:
        self.position = position

    def getSprite(self) -> pygame.Surface:
        if self.sprite is None:
            raise Exception("Sprite not set")
        return self.sprite
    
    def setSprite(self, sprite: pygame.Surface) -> None:
        self.sprite = sprite
    
    def getHitbox(self) -> pygame.Rect:
        return pygame.Rect(self.position.x,self.position.y,self.size[0],self.size[1])

    def toJson(self) -> dict:
        if self.sprite is None:
            raise Exception("Sprite not set")
        
        sprite32 = pygame.transform.scale(self.sprite, (32, 32))
        serialized_sprite = pygame.surfarray.array3d(sprite32)

        dir = "assets/objects/"

        bkg = pickle.dumps(serialized_sprite)
        fileName = dir + f"{self.id}.pickle"

        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(fileName, "wb") as f:
            f.write(bkg)

        return {
            'id': self.id,
            'position-absolute': {
                'x': self.position.x,
                'y': self.position.y
            },
            'texture': fileName,
            'navigateTo': self.navigateTo,
            'interactive': self.interactive,
            'metrics': {'happiness-effect': self.happiness_effect,
                        'time-effect': self.time_effect,
                        'health-effect': self.health_effect,
                        'money-effect': self.money_effect
                        },
            'next-day': self.next_day,
            'size': self.size,
            'collidable': self.isCollidable
        }

