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
    "In order to move around, you can use the W A S D keys. You can use W to move up, A to move left, S to move down" + \
    " and D to move right.",
    "Imagine you are a real person. What would you do at this time? Note the effect actions have on your metrics" + \
    " (the bars on the top).",
    "You can interact with the world by pressing E. You can interact with an object if you are close enough" + \
    " to it and are facing its direction. You will know you can interact with an object when a popup appears on the" + \
    " character's top right. The popup will tell you the effect the object will have on your metrics.",
    "The bars on the top are your metrics. The first one is your happines, the second one is the time left in the day. Finally," + \
    " there is the health bar. Below these you can also see your current funds. Note that you can see the current time of the " + \
    " day in the top right corner of the screen.",
    "The goal of the game is to live your life to the fullest. You can do this by interacting with the world and" + \
    " making the right choices. However, be careful, as your choices will have consequences. You can also" + \
    " interact with the oracle to get some hints on what to do next. Remember to watch your metrics and" + \
    " make sure you don't run out of time or money. Have Fun!",
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
    
    def setQuestion(self, question: str) -> None:
        if question not in self.questions:
            return
        self.question = question

    def getQuestions(self) -> list[str]:
        return self.questions
    
    def getAnswer(self) -> str:
        return self.answers[self.questions.index(self.question)]