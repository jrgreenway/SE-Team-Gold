import pygame

class Metrics:
    '''A class to represent the metrics of the avatar.
    Attributes:
        time (int): The time spent on a task.
        happiness (int): The happiness level of a person.
        health (int): The health level of a person.
        
    Methods:
        setTime: Sets the time.
        setHappiness: Sets the happiness.
        setHealth: Sets the health.
        getTime: Gets the time.
        getHappiness: Gets the happiness.
        getHealth: Gets the health.

        updateTime: Updates the time by increment (default 1).
        formatTime: Formats the time into a string.
        '''
    def __init__(self, time: int, happiness: int, health: int) -> None:
        self.time = time
        self.happiness = happiness
        self.health = health

    #def __add__(self, other: object()): could do a class+class which alters the metrics?

    #Setters/Getters

    def setTime(self, time):
        self.time = time

    def setHappiness(self, happiness):
        self.happiness = happiness
    
    def setHealth(self, health):
        self.health = health
    
    def getTime(self):
        return self.time
    
    def getHappiness(self):
        return self.happiness
    
    def getHealth(self):
        return self.health
    
    #Methods

    def updateTime(self, increment=-1):
        self.time += increment
    
    def formatTime(self):
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes:02d}:{seconds:02d}"
    

