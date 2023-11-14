from typing import Callable
from buttons.button import Button
import pygame

def create_buttons(width: int, savedGames: list[str], buttonClick: Callable) -> list[Button]:
    """Create a list of Button objects from a list of saved games."""
    buttons = []
    for i, game in enumerate(savedGames):
        button = Button(pygame.Rect(0, 0, width, 50), lambda **kwargs: buttonClick(**kwargs, gameName=game))
        button.rect.x = 50
        buttons.append(button)
    return buttons


def draw_scrollbar(screen: pygame.Surface, scroll_pos: int, total_items: int, visible_height: int):
    """Draw a scrollbar on the right side of the screen."""
    bar_height = visible_height / total_items * visible_height
    bar_pos = scroll_pos / total_items * visible_height
    pygame.draw.rect(screen, (200, 200, 200), (screen.get_width() - 20, 0, 20, visible_height))
    pygame.draw.rect(screen, (100, 100, 100), (screen.get_width() - 20, bar_pos, 20, bar_height))


def draw_load_screen(
        screen: pygame.Surface, 
        savedGames: list[str], loadGameCB: Callable, 
        scrollPos: int,
        backCB: Callable
) -> list[Button]:
    """Draw a list of saved games as buttons that can be scrolled."""
    buttons = create_buttons(screen.get_width() - 100, savedGames, loadGameCB)
    visible_height = screen.get_height() - 100
    total_items = len(buttons)
    screen.fill((255, 255, 255))
    index = 0
    top = 100
    for button in buttons[scrollPos:]:
        button.rect.y = top + index * 60
        index += 1
        if button.rect.bottom > visible_height:
            break

        pygame.draw.rect(screen, (0, 255, 0), button.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(savedGames[buttons.index(button)], True, (255, 255, 255))
        screen.blit(text, (button.rect.x + 10, button.rect.y + 10))
    
    draw_scrollbar(screen, scrollPos, total_items, visible_height)

    # create a back button
    
    back_button = pygame.Rect(100, screen.get_height() - 75, 100, 50)
    pygame.draw.rect(screen, (0, 0, 255), back_button)
    font = pygame.font.Font(None, 36)
    back_label = font.render("Back", True, (255, 255, 255))
    screen.blit(back_label, back_button.move(10, 10))

    return buttons + [Button(back_button, backCB)]
    
    