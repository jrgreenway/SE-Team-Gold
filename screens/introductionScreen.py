from typing import Callable
from pygame import Surface
import pygame

from buttons.button import Button


INTRODUCTION_MESSAGE = "Welcome to the Avatar Game! This is a game in which you will learn about the fun responsabilities of life. " + \
    "The goal of the game is to make it through to the end of the week without any of your main metrics, such as happiness, " + \
    "health, or money, reaching zero. You can interact with the objects in your world in order to keep your metrics high. Note that " + \
    "there are a few things you should remember. Every day, you should go to bed before 22:00 to avoid being tired and waking up sad and with less health. " + \
    "You also lose health over night due to getting hungry so make sure to eat plenty before going to bed. Finaly, remember to pay your taxes every day at the local council " + \
    "building. If you don't, you will lose money and get a fine. Don't worry, life's fair and you have to pay rent over night anyways. " + \
    "Ultimately, you should be able to find the perfect balance of work, training, and fun in order to make it through the week. " + \
    "Should things go bad, you will notice your friend Paul calling you with some hints. But until then, good luck at the game of life!"

def draw_introduction_screen(
        screen: Surface, 
        startFrame: int, 
        currentFrame: int,
        nextCB: Callable,
    ) -> list[Button]:
    ''' draw_introduction_screen: pygame.Surface -> list[Button]
    Draws the introduction screen to the screen and returns a list of all the buttons on the screen.
    '''
    
    # Dim the screen
    dim_screen = pygame.Surface(screen.get_size())
    dim_screen.fill((0, 0, 0))
    dim_screen.set_alpha(128)
    screen.blit(dim_screen, (0, 0))

    # Calculate the number of characters to show based on the frames
    characters_to_show = (currentFrame - startFrame) // 2

    # Ensure that the number of characters to show does not exceed the length of the answer
    characters_to_show = min(characters_to_show, len(INTRODUCTION_MESSAGE))

    # Render the text with the characters to show
    font = pygame.font.Font(None, 36)
    text_surface = font.render(INTRODUCTION_MESSAGE[:characters_to_show], True, (255, 255, 255))
    text_rect = text_surface.get_rect(left=50, top=100)

    # Split the text on multiple lines if the width exceeds the width of the screen
    if text_surface.get_width() > (screen.get_width() - 100):
        words = INTRODUCTION_MESSAGE[:characters_to_show].split(' ')
        lines = []
        current_line = ''
        for word in words:
            if font.size(current_line + ' ' + word)[0] <= screen.get_width() - 100:
                current_line += ' ' + word
            else:
                lines.append(current_line.strip())
                current_line = word
        lines.append(current_line.strip())

        # Render each line of text
        y_offset = text_rect.y
        for line in lines:
            line_surface = font.render(line, True, (255, 255, 255))
            line_rect = line_surface.get_rect(left=50, top=y_offset)
            screen.blit(line_surface, line_rect)
            y_offset += line_rect.height

    else:
        screen.blit(text_surface, text_rect)

    # Create the buttons
    buttons = []

    # Create the back button
    back_button_rect = pygame.Rect(0, 0, 100, 50)
    back_button_rect.center = (screen.get_width() // 2 - 100, screen.get_height() - 70)
    back_button = Button(back_button_rect, nextCB)
    buttons.append(back_button)

    # draw the Back text
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Continue', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2 - 100, screen.get_height() - 70))
    screen.blit(text_surface, text_rect)

    # Return the list of buttons
    return buttons