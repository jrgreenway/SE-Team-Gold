import pygame

class Metrics():
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
        '''
    def __init__(self, time, happiness, health) -> None:
        self.time = self.setTime(time)
        self.happiness = self.setHappiness(happiness)
        self.health = self.setHealth(health)

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
        return self.health
    
    #Methods

    def updateTime(self, increment=1):
        self.setTime(self.time+increment)
    
    

