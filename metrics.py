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
        #for buffs, maybe have as a list of dicts for each buff, then a loop in changeMetrics() to determine total de/buff

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
    
    def changeMetrics(self, happiness_change=0, time_change=0, health_change=0):
        #if we add buffs/debuffs, suggest storing it in this class, then adding as modifier
        self.happiness += happiness_change
        self.time -= time_change #time alterations stored as +ve
        self.health += health_change

    

