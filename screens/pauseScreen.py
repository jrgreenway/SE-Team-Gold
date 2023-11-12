from typing import Callable
from buttons.button import Button
import pygame


def draw_pause_screen(
        screen: pygame.Surface,
        saveCB: Callable,
        exitCB: Callable,
        backCB: Callable
    ) -> list[Button]:
    ''' draw_pause_screen: pygame.Surface -> list[Button]
    Draws the pause screen to the screen and returns a list of all the buttons on the screen.
    '''
    # Dim the current screen
    dim_screen = pygame.Surface(screen.get_size())
    dim_screen.fill((0, 0, 0))
    dim_screen.set_alpha(128)
    screen.blit(dim_screen, (0, 0))

    # Draw the pause screen
    pause_font = pygame.font.Font(None, 50)
    pause_text = pause_font.render("PAUSED", True, (255, 255, 255))
    screen.blit(pause_text, (screen.get_width() // 2 - pause_text.get_width() // 2, 100))

    # Draw the Save button
    save_font = pygame.font.Font(None, 30)
    save_text = save_font.render("Save", True, (255, 255, 255))
    save_button = pygame.Rect(screen.get_width() // 2 - 100, 200, 200, 50)
    pygame.draw.rect(screen, (0, 0, 255), save_button)
    screen.blit(save_text, (screen.get_width() // 2 - save_text.get_width() // 2, 215))

    # Draw the Back to Main Menu button
    back_font = pygame.font.Font(None, 30)
    back_text = back_font.render("Back to Main Menu", True, (255, 255, 255))
    back_button = pygame.Rect(screen.get_width() // 2 - 150, 300, 300, 50)
    pygame.draw.rect(screen, (0, 0, 255), back_button)
    screen.blit(back_text, (screen.get_width() // 2 - back_text.get_width() // 2, 315))

    # Draw the Exit button
    exit_font = pygame.font.Font(None, 30)
    exit_text = exit_font.render("Exit", True, (255, 255, 255))
    exit_button = pygame.Rect(screen.get_width() // 2 - 100, 400, 200, 50)
    pygame.draw.rect(screen, (0, 0, 255), exit_button)
    screen.blit(exit_text, (screen.get_width() // 2 - exit_text.get_width() // 2, 415))

    return [Button(save_button, saveCB), Button(back_button, backCB), Button(exit_button, exitCB)]
