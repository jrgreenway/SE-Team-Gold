from gc import callbacks
from typing import Callable
import pygame

from buttons.button import Button

QUESTIONS = [
    "How do I move?",
    "What should I do?",
    "How can I interact with the world?",
    "What are the bars on the top?",
    "What is the goal of the game?",
]

ANSWERS = [
    "Use the arrow keys to move around.",
    "Imagine you are a real person. What would you do at this time? Note the effect actions have on your metrics" + \
    " the bars on the top).",
    "You can interact with the world by pressing the space bar. You can interact with an object if you are close enough" + \
    " to it and are facing its direction. A pointer for this would be the name of the object popping up.",
    "The bars on the top are your metrics. The first one is your happines, the second one is the time left in the day. Below" + \
    " these you can also see your current funds as well as the time of the day.",
]

class Oracle:


    def __init__(
            self, 
            screen: pygame.Surface, 
            questions: list[str] = QUESTIONS, 
            answers: list[str] = ANSWERS,
            callBacks: dict[str, Callable] = {}
    ) -> None:
        self.screen = screen
        self.questions = questions
        self.answers = answers
        self.sprite = pygame.image.load("assets/oracleIcon.png")
        self.callbacks = callBacks
        pass

    
    def draw(self) -> Button:
        x, y = self.screen.get_size()

        buttonRect = pygame.Rect(
            x - self.sprite.get_width(), 
            y - self.sprite.get_height(), 
            self.sprite.get_width(), 
            self.sprite.get_height()
        )
        button = Button(buttonRect, self.callbacks['clickOracle'])

        self.screen.blit(self.sprite, buttonRect)
        return button