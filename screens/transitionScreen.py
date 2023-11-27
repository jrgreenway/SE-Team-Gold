from typing import Callable
import pygame

from buttons.button import Button


def draw_transition_screen(
        screen: pygame.Surface,
        options: list[str],
        questionCB: Callable,
    ) -> list[Button]:
    ''' draw_oracle_question_screen: pygame.Surface -> list[Button]
    Draws the oracle question screen to the screen and returns a list of all the buttons on the screen.
    '''
    # Dim the current screen
    dim_screen = pygame.Surface(screen.get_size())
    dim_screen.fill((0, 0, 0))
    dim_screen.set_alpha(128)
    screen.blit(dim_screen, (0, 0))

    # Draw the oracle screen
    option_font = pygame.font.Font(None, 50)
    option_text = option_font.render("Options", True, (255, 255, 255))
    screen.blit(option_text, (screen.get_width() // 2 - option_text.get_width() // 2, 100))

    # Draw the questions
    option_font = pygame.font.Font(None, 30)
    option_buttons = []
    for i, option in enumerate(options):
        option_text = option_font.render(option, True, (255, 255, 255))
        
        # Draw the questions
        option_font = pygame.font.Font(None, 30)
        option_buttons = []
        for i, option in enumerate(options):
            option_text = option_font.render(option, True, (255, 255, 255))
            optionTop = 215 + 60 * i
            buttonTop = optionTop + option_text.get_height() // 2 - 25
            option_button = pygame.Rect(screen.get_width() // 2 - option_text.get_width() // 2 - 10, buttonTop, option_text.get_width() + 20, 50)
            pygame.draw.rect(screen, (0, 0, 255), option_button)
            screen.blit(option_text, (screen.get_width() // 2 - option_text.get_width() // 2, optionTop))
            option_buttons.append(Button(option_button, questionCB))

        

    return option_buttons
