from typing import Callable
from buttons.button import Button
import pygame


def draw_map_screen(
        screen: pygame.Surface,
        officeCB: Callable,
        parkCB : Callable,
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

    

    # office_text = map_font.render("Office", True, (255, 255, 255))
    office = pygame.image.load("/assets/office.png")
    office_button_rect = pygame.Rect(screen.get_width() // 2 - 100, 200, 200, 50)
    screen.blit(office, (screen.get_width() // 2 - office.get_width() // 2, 215))
    pygame.draw.rect(screen, (0, 0, 255), office_button_rect, 2)

    park = pygame.image.load("/assets/park.png")
    park_button_rect = pygame.Rect(screen.get_width() // 2 - 100, 200, 200, 50)
    screen.blit(park, (screen.get_width() // 2 - office.get_width() // 2, 215))
    pygame.draw.rect(screen, (0, 0, 255), park_button_rect, 2)

    # Draw the Back to Main Menu button
    back_font = pygame.font.Font(None, 30)
    back_text = back_font.render("Back", True, (255, 255, 255))
    back_button = pygame.Rect(screen.get_width() // 2 - 150, 300, 300, 50)
    pygame.draw.rect(screen, (0, 0, 255), back_button)
    screen.blit(back_text, (screen.get_width() // 2 - back_text.get_width() // 2, 315))

    

    return [Button(office_button_rect, officeCB),Button(park_button_rect, parkCB), Button(back_button, backCB)]
