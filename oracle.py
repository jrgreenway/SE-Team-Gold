from gc import callbacks
from typing import Callable
import pygame

from buttons.button import Button
from metrics import Metrics

QUESTIONS = [
    "How do I move?",
    "What should I do?",
    "How can I interact with the world?",
    "What are the bars on the top?",
    "What is the goal of the game?",
    "Why is my health red?",
    "Why is my happiness red?",
    "Why is my time red?",
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
    "Your health is red because it is low. You should probably eat something or go to the doctor. Look around you and find objects" + \
    " that can help you with that. You can know they are helpful as the popup will have a green square for the health metric to indicate" + \
    " that it will increase.",
    "Your happiness is red because it is low. You should probably do something fun. Look around you and find objects" + \
    " that can help you with that. You can know they are helpful as the popup will have a green square for the happiness metric to indicate" + \
    " that it will increase.",
    "Your time is red because it is low and the day is coming to an end. Remember that the day ends at 22:00. You should go to bed before that" + \
    " time to avoid waking up tired tomorrow.",
]


class OracleCallPermission:

    def __init__(self) -> None:
        self.callForTime = True
        self.callForHappiness = True
        self.callForHealth = True

    def setCallForTime(self, callForTime: bool) -> None:
        self.callForTime = callForTime

    def setCallForHappiness(self, callForHappiness: bool) -> None:
        self.callForHappiness = callForHappiness

    def setCallForHealth(self, callForHealth: bool) -> None:
        self.callForHealth = callForHealth

    def getCallForTime(self) -> bool:
        return self.callForTime
    
    def getCallForHappiness(self) -> bool:
        return self.callForHappiness
    
    def getCallForHealth(self) -> bool:
        return self.callForHealth


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
        self.callPermissions = OracleCallPermission()
        pass
    
    def resetNextDay(self) -> None:
        # Very bad for memory management but we don't care about this now
        self.callPermissions = OracleCallPermission() 

    def draw(self, playerMetrics: Metrics, currentFrame: int) -> Button:
        x, y = self.screen.get_size()

        # Check if any of the metrics is below 30
        danger = (playerMetrics.isHappinessDanger() and self.callPermissions.getCallForHappiness()) or \
            (playerMetrics.isHealthDanger() and self.callPermissions.getCallForHealth()) or \
            (playerMetrics.isTimeDanger() and self.callPermissions.getCallForTime())

        # Scale factor for animation
        scale_factor = 1.0

        if danger:
            # Calculate scale factor based on currentFrame
            scale_factor = 1.0 + abs((currentFrame % 60) - 30) / 120  # Adjust the values as needed

        # Scale the sprite and button size
        scaled_sprite = pygame.transform.scale(
            self.sprite, 
            (int(self.sprite.get_width() * scale_factor),
            int(self.sprite.get_height() * scale_factor))
        )
        
        scaled_button_rect = pygame.Rect(
            x - scaled_sprite.get_width(),
            y - scaled_sprite.get_height(),
            scaled_sprite.get_width(),
            scaled_sprite.get_height()
        )

        button = Button(scaled_button_rect, self.callbacks['clickOracle'])

        if danger:
            button.setAction(self.callbacks['clickOracleQuestion'])

        self.screen.blit(scaled_sprite, scaled_button_rect)
        return button
    
    def setQuestion(self, question: str) -> None:
        if question not in self.questions:
            return
        self.question = question

    def getQuestions(self) -> list[str]:
        return self.questions
    
    def getAnswer(self) -> str:
        return self.answers[self.questions.index(self.question)]