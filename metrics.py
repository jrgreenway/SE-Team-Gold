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
    def __init__(self, time: int = 480, happiness: int = 100, health: int = 100, money: int = 0) -> None:
        self.time = time
        self.happiness = happiness
        self.health = health
        self.money = money
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
    
    def getMoney(self):
        return self.money
    
    def isTimeDanger(self):
        # 30% of the day left
        return self.time >= 1068
    
    def isHappinessDanger(self):
        return self.happiness <= 30
    
    def isHealthDanger(self):
        return self.health <= 30

    #Methods

    # TODO Increment stays 4
    def updateTime(self, increment=4) -> bool:
        self.time += increment
        return self.time >= 1320
    
    def updateHappiness(self, increment=0) -> None:
        self.happiness = max(0, min(100, self.happiness + increment))
    
    def formatTime(self):
        hours = self.time // 60
        minutes = (self.time % 60) // 10 * 10
        return f"{hours:02d}:{minutes:02d}"
    
    def resetTime(self):
        self.time = 480
    
    def draw(self, screen: pygame.Surface) -> None:
        # Draw the happiness bar chart
        happiness_bar_width = 100  # Adjust the width based on the happiness value
        hapinness_bar_value = self.happiness
        happiness_bar_height = 20
        happiness_bar_color = (0, 255, 0)  # Gray color for happiness
        hapoiness_bar_container_color = (128, 128, 128)  # Black color for the container
        happiness_bar_container_rect = pygame.Rect(10, 10, happiness_bar_width, happiness_bar_height)
        happiness_bar_rect = pygame.Rect(10, 10, hapinness_bar_value, happiness_bar_height)
        happiness_icon = pygame.image.load("assets/happy.png")  # Replace "happiness_icon.png" with the actual filename of the icon image
        happiness_icon_rect = happiness_icon.get_rect()
        happiness_icon_rect.left = happiness_bar_container_rect.right + 5  # Adjust the position of the icon
        happiness_icon_rect.centery = happiness_bar_container_rect.centery
        screen.blit(happiness_icon, happiness_icon_rect)
        pygame.draw.rect(screen, hapoiness_bar_container_color, happiness_bar_container_rect)
        pygame.draw.rect(screen, happiness_bar_color, happiness_bar_rect)

        # Draw the time bar chart
        time_bar_width = 100
        time_bar_value = (1320 - self.time) / (840) * 100
        time_bar_height = 20
        time_bar_color = (time_bar_value > 60 and (0, 255, 0)) or (time_bar_value > 30 and (255, 255, 0)) or ((255, 0, 0))
        time_bar_container_color = (128, 128, 128)
        time_bar_container_rect = pygame.Rect(10, 40, time_bar_width, time_bar_height)
        time_bar_rect = pygame.Rect(10, 40, time_bar_value, time_bar_height)
        time_icon = pygame.image.load("assets/clock.png")
        time_icon_rect = time_icon.get_rect()
        time_icon_rect.left = time_bar_container_rect.right + 5
        time_icon_rect.centery = time_bar_container_rect.centery
        screen.blit(time_icon, time_icon_rect)
        pygame.draw.rect(screen, time_bar_container_color, time_bar_container_rect)
        pygame.draw.rect(screen, time_bar_color, time_bar_rect)

        # Draw the health bar chart
        health_bar_width = 100
        health_bar_value = self.health
        health_bar_height = 20
        health_bar_color = (health_bar_value > 60 and (0, 255, 0)) or (health_bar_value > 30 and (255, 255, 0)) or ((255, 0, 0))
        health_bar_container_color = (128, 128, 128)
        health_bar_container_rect = pygame.Rect(10, 70, health_bar_width, health_bar_height)
        health_bar_rect = pygame.Rect(10, 70, health_bar_value, health_bar_height)
        health_icon = pygame.image.load("assets/health.png")
        health_icon_rect = health_icon.get_rect()
        health_icon_rect.left = health_bar_container_rect.right + 5
        health_icon_rect.centery = health_bar_container_rect.centery
        screen.blit(health_icon, health_icon_rect)
        pygame.draw.rect(screen, health_bar_container_color, health_bar_container_rect)
        pygame.draw.rect(screen, health_bar_color, health_bar_rect)

        # Draw the money value
        money_value = self.money
        money_font = pygame.font.Font(None, 24)
        money_text = money_font.render(f"${money_value}", True, (255, 255, 255))
        money_text_rect = money_text.get_rect()
        money_text_rect.left = 10
        money_text_rect.top = 100
        screen.blit(money_text, money_text_rect)

    
    
    def changeMetrics(self, happiness_change=0, time_change=0, health_change=0, money_change=0):
        #if we add buffs/debuffs, suggest storing it in this class, then adding as modifier
        self.happiness += happiness_change
        if self.happiness > 100:
            self.happiness = 100
        self.time += time_change #time alterations stored as +ve
        self.health += health_change
        if self.health > 100:
            self.health = 100
        self.money += money_change

    def toJson(self) -> dict:
        return {
            "time": self.time,
            "happiness": self.happiness,
            "health": self.health,
            "money": self.money
        }

    

