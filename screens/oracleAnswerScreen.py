from typing import Callable
import pygame

from buttons.button import Button


def draw_oracle_answer_screen(
        screen: pygame.Surface,
        answer: str,
        backCB: Callable,
        closeCB: Callable,
        startFrame: int,
        currentFrame: int,
    ) -> list[Button]:
    ''' draw_oracle_answer_screen: pygame.Surface -> list[Button]
    Draws the oracle answer screen to the screen and returns a list of all the buttons on the screen.
    '''
    # Dim the current screen
    dim_screen = pygame.Surface(screen.get_size())
    dim_screen.fill((0, 0, 0))
    dim_screen.set_alpha(128)
    screen.blit(dim_screen, (0, 0))

    # Calculate the number of characters to show based on the frames
    characters_to_show = (currentFrame - startFrame) // 2

    # Ensure that the number of characters to show does not exceed the length of the answer
    characters_to_show = min(characters_to_show, len(answer))

    # Render the text with the characters to show
    font = pygame.font.Font(None, 36)
    text_surface = font.render(answer[:characters_to_show], True, (255, 255, 255))
    text_rect = text_surface.get_rect(left=50, top=100)

    # Split the text on multiple lines if the width exceeds the width of the screen
    if text_surface.get_width() > (screen.get_width() - 100):
        words = answer[:characters_to_show].split(' ')
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
    back_button = Button(back_button_rect, backCB)
    buttons.append(back_button)

    # draw the Back text
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Back', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2 - 100, screen.get_height() - 70))
    screen.blit(text_surface, text_rect)

    # Create the close button
    close_button_rect = pygame.Rect(0, 0, 100, 50)
    close_button_rect.center = (screen.get_width() // 2 + 100, screen.get_height() - 70)
    close_button = Button(close_button_rect, closeCB)
    buttons.append(close_button)

    # draw the Close text
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Close', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2 + 100, screen.get_height() - 70))
    screen.blit(text_surface, text_rect)

    # Return the list of buttons
    return buttons