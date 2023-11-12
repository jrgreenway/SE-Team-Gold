from buttons.button import Button
import pygame

from buttons.buttonCallbacks import exitButtonCB, saveButtonCB


def draw_pause_screen(screen: pygame.Surface) -> list[Button]:
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

    # Draw the Exit button
    exit_font = pygame.font.Font(None, 30)
    exit_text = exit_font.render("Exit", True, (255, 255, 255))
    exit_button = pygame.Rect(screen.get_width() // 2 - 100, 300, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), exit_button)
    screen.blit(exit_text, (screen.get_width() // 2 - exit_text.get_width() // 2, 315))

    return [Button(save_button, saveButtonCB), Button(exit_button, exitButtonCB)]
