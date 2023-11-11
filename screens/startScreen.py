
import pygame

from buttons.button import Button
from buttons.buttonCallbacks import exitButtonCB, loadButtonCB, startButtonCB

def draw_start_screen(screen: pygame.Surface) -> list[Button]:
    ''' draw_start_screen: pygame.Surface -> list[Button]
    Draws the start screen to the screen and returns a list of all the buttons on the screen.
    '''
    # Set up the font
    font = pygame.font.Font(None, 36)

    # Set up the buttons
    button_width = 200
    button_height = 50
    button_padding = 20
    start_button_rect = pygame.Rect((screen.get_width() - button_width) / 2, 200, button_width, button_height)
    load_button_rect = pygame.Rect((screen.get_width() - button_width) / 2, start_button_rect.bottom + button_padding, button_width, button_height)
    exit_button_rect = pygame.Rect((screen.get_width() - button_width) / 2, load_button_rect.bottom + button_padding, button_width, button_height)

    # Set up the button labels
    start_label = font.render("Start Game", True, (255, 255, 255))
    load_label = font.render("Load Game", True, (255, 255, 255))
    exit_label = font.render("Exit", True, (255, 255, 255))

    screen.fill((255, 255, 255))

    # Draw the buttons
    pygame.draw.rect(screen, (0, 255, 0), start_button_rect)
    pygame.draw.rect(screen, (0, 255, 0), load_button_rect)
    pygame.draw.rect(screen, (0, 255, 0), exit_button_rect)

    screen.blit(start_label, start_button_rect.move(10, 10))
    screen.blit(load_label, load_button_rect.move(10, 10))
    screen.blit(exit_label, exit_button_rect.move(10, 10))

    return [Button(start_button_rect, startButtonCB), Button(load_button_rect, loadButtonCB), Button(exit_button_rect, exitButtonCB)]
