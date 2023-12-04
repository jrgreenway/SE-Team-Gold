from typing import Callable
import pygame

from buttons.button import Button

def draw_game_over_screen(screen: pygame.Surface, exitToTitleCB: Callable, exitToDesktopCB: Callable) -> list[Button]:

    # Set up the font
    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 72)

    # Set up the buttons
    button_width = 300
    button_height = 50
    button_padding = 20
    exit_to_title_button_rect = pygame.Rect((screen.get_width() - button_width) / 2, screen.get_height() // 2, button_width, button_height)
    exit_to_desktop_button_rect = pygame.Rect((screen.get_width() - button_width) / 2, exit_to_title_button_rect.bottom + button_padding, button_width, button_height)

    # Set up the button labels
    exit_to_title_label = font.render("Exit to Title Screen", True, (255, 255, 255))
    exit_to_desktop_label = font.render("Exit to Desktop", True, (255, 255, 255))

    screen.fill((255, 255, 255))

    #Draw game over message
    message = font2.render("Game Over", True, (158, 14, 14))
    messageRect = pygame.Rect((screen.get_width() - button_width) / 2, exit_to_title_button_rect.top - button_height - button_padding*3, button_width, button_height)
    screen.blit(message, messageRect)

    # Draw the buttons
    pygame.draw.rect(screen, (9, 117, 110), exit_to_title_button_rect)
    pygame.draw.rect(screen, (9, 117, 110), exit_to_desktop_button_rect)

    screen.blit(exit_to_title_label, exit_to_title_button_rect.move(10, 10))
    screen.blit(exit_to_desktop_label, exit_to_desktop_button_rect.move(10, 10))

    return [Button(exit_to_title_button_rect, exitToTitleCB), Button(exit_to_desktop_button_rect, exitToDesktopCB)]
