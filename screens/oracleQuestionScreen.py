from typing import Callable
import pygame

from buttons.button import Button


def draw_oracle_question_screen(
        screen: pygame.Surface,
        questions: list[str],
        questionCB: Callable,
        backCB: Callable
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
    oracle_font = pygame.font.Font(None, 50)
    oracle_text = oracle_font.render("Oracle", True, (255, 255, 255))
    screen.blit(oracle_text, (screen.get_width() // 2 - oracle_text.get_width() // 2, 100))

    # Draw the questions
    question_font = pygame.font.Font(None, 30)
    question_buttons = []
    for i, question in enumerate(questions):
        question_text = question_font.render(question, True, (255, 255, 255))
        
        # Draw the questions
        question_font = pygame.font.Font(None, 30)
        question_buttons = []
        for i, question in enumerate(questions):
            question_text = question_font.render(question, True, (255, 255, 255))
            questionTop = 215 + 60 * i
            buttonTop = questionTop + question_text.get_height() // 2 - 25
            question_button = pygame.Rect(screen.get_width() // 2 - question_text.get_width() // 2 - 10, buttonTop, question_text.get_width() + 20, 50)
            pygame.draw.rect(screen, (0, 0, 255), question_button)
            screen.blit(question_text, (screen.get_width() // 2 - question_text.get_width() // 2, questionTop))
            question_buttons.append(Button(question_button, questionCB))

        # Draw a back to Game button
        back_font = pygame.font.Font(None, 30)
        back_text = back_font.render("Back to Game", True, (255, 255, 255))
        textTop = 215 + 60 * len(questions)
        buttonTop = textTop + back_text.get_height() // 2 - 25
        back_button = pygame.Rect(screen.get_width() // 2 - back_text.get_width() // 2 - 10, buttonTop, back_text.get_width() + 20, 50)
        pygame.draw.rect(screen, (0, 0, 255), back_button)
        screen.blit(back_text, (screen.get_width() // 2 - back_text.get_width() // 2, textTop))
        question_buttons.append(Button(back_button, backCB))

    return question_buttons
