from sys import implementation
from typing import Callable, Optional
from xmlrpc.client import boolean
import pygame

class Button:

    def __init__(self, rect: pygame.Rect, action: Optional[Callable] = None) -> None:
        self.rect = rect
        self.action = action

    def check_click(self, pos: tuple) -> bool:
        return self.rect.collidepoint(pos)
    
    def onClick(self) -> bool:
        if self.action is not None:
            return self.action()
        return False
    
    def setAction(self, action: Callable) -> None:
        self.action = action