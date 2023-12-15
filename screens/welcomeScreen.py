import math
import pygame

def draw_welcome_screen(screen, currentFrame):
    ''' draw_welcome_screen: pygame.Surface, int -> None
    Draws the welcome screen to the screen.
    '''
    # Set background color
    background_color = (255, 255, 255)
    screen.fill(background_color)

    # Set font and text
    font_size = 30 + int(5 * abs(math.sin((currentFrame % 60) / 20)))
    font = pygame.font.Font(None, font_size)
    text = font.render("My Friend Paul", True, (0, 0, 0))

    # Center text on screen
    text_rect = text.get_rect(center=screen.get_rect().center)

    # Draw text on screen
    screen.blit(text, text_rect)

    # Set font and text for "Press enter to start..."
    font_size = 20 + int(3 * abs(math.sin((currentFrame % 60) / 20)))
    font = pygame.font.Font(None, font_size)
    text = font.render("Press space to start...", True, (0, 0, 0))

    # Center text below previous text
    text_rect = text.get_rect(center=(screen.get_rect().centerx, screen.get_rect().centery + 50))

    # Draw text on screen
    screen.blit(text, text_rect)