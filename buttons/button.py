from sys import implementation
from typing import Callable, Optional
from xmlrpc.client import boolean
import pygame

class Button:
    ''' Button class - represents a button on the screen

    Attributes:
    rect: pygame.Rect - the rectangle that represents the button
    action: Callable - the function that is called when the button is clicked

    Methods:
    constructor: __init__(self, rect, action - optional)
    check_click: check_click(self, pos) -> bool - checks if the click at the given position
        is on the button
    onClick: onClick(self) -> bool - calls the action function if it exists
    setAction: setAction(self, action) -> None - sets the action function to the given function
    '''

    def __init__(self, rect: pygame.Rect, action: Optional[Callable] = None) -> None:
        self.rect = rect
        self.action = action

    def check_click(self, pos: tuple) -> bool:
        ''' Button.check_click(self, pos) -> bool
        Checks if the click at the given position is on the button
        '''
        return self.rect.collidepoint(pos)
    
    def onClick(self, **kwargs) -> tuple[bool, str]:
        ''' Button.onClick(self, kwargs) -> bool, str
        Calls the action function if it exists and returns the result which is the new state
        of the running attribute of the game. Also, returns the next screen of the game.
        '''
        if self.action is not None:
            return self.action(**kwargs)
        return False, ''
    
    def setAction(self, action: Callable) -> None:
        ''' Button.setAction(self, action) -> None
        Sets the action function to the given function
        '''
        self.action = action