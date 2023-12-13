from typing import Callable
from buttons.button import Button
import pygame

# location format is location: (sceneIndex, x, y)
def draw_map_screen(
        screen: pygame.Surface,
        locations: dict[str, tuple[int, int, int, str]],
        clickLocationCB: Callable,
        backCB: Callable,
    ) -> list[Button]:
    ''' draw_pause_screen: pygame.Surface -> list[Button]
    Draws the pause screen to the screen and returns a list of all the buttons on the screen.
    '''
    # Dim the current screen
    dim_screen = pygame.Surface(screen.get_size())
    dim_screen.fill((0, 0, 0))
    dim_screen.set_alpha(128)
    screen.blit(dim_screen, (0, 0))

    buttons = []

    # Draw the map screen
    for location in locations:
        _, x, y, spritePath = locations[location]
        location_button = pygame.Rect(x, y, 150, 50)
        if spritePath != "":
            location_sprite = pygame.image.load(spritePath)
            location_sprite = pygame.transform.scale(location_sprite, (160,160))
            location_button = pygame.Rect(x, y, location_sprite.get_width(), location_sprite.get_height())
            screen.blit(location_sprite, (x, y))


        buttons.append(Button(location_button, clickLocationCB))

    # Add a Back Button in the top right corner
    back_font = pygame.font.Font(None, 30)
    back_text = back_font.render("Back", True, (255, 255, 255))
    back_button_rect = pygame.Rect(screen.get_width() - back_text.get_width() - 10, 10, back_text.get_width() + 20, 50)
    pygame.draw.rect(screen, (0, 0, 255), back_button_rect)
    screen.blit(back_text, (screen.get_width() - back_text.get_width() - 10, 10))
    buttons.append(Button(back_button_rect, backCB))

    return buttons

    
