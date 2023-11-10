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