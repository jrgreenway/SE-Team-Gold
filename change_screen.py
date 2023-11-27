from gc import callbacks
from typing import Callable
import pygame

from buttons.button import Button

OPTIONS = [
    "Go to Kitchen",
    "Go to bedroom",
    "Go to shop",
    "Go to office",
    
]
class Change_screen:
    def __init__(
        self, 
            screen: pygame.Surface, 
            options: list[str] = OPTIONS, 
    ) -> None:
        self.screen = screen
        self.options = options
        pass

    def draw(self,screen: pygame.Surface) -> Button:   
        button_rect = pygame.Rect(100, 100, 100, 50)  # Define button rectangle
        pygame.draw.rect(screen, (0, 255, 0), button_rect)  # Draw the button rectangle
        font = pygame.font.Font(None, 36)
        text = font.render("Click Me!", True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    def setOption(self, option: str) -> None:
        if option not in self.options:
            return
        self.option = option

    def getOptions(self) -> list[str]:
        return self.options
        


