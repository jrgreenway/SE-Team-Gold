from typing import Callable
from assets.assetsConstants import FEMALE_CHAR_ASSET, MALE_CHAR_ASSET
from buttons.button import Button
import pygame

def draw_avatar_screen(
        screen: pygame.Surface,
        currentName: str,
        playerGender: str,
        onMaleSelected: Callable,
        onFemaleSelected: Callable,
        backCB: Callable,
        startGameCB: Callable
    ) -> list[Button]:
    ''' draw_avatar_screen: pygame.Surface, str, str, Callable, Callable -> list[Button]
    Draws the avatar screen to the screen and returns a list of all the buttons on the screen.
    '''
    
    # Set up the fonts
    title_font = pygame.font.SysFont("Arial", 50)
    label_font = pygame.font.SysFont("Arial", 30)

    # Set up the colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (128, 128, 128)

    # Load the images
    male_image = pygame.image.load(MALE_CHAR_ASSET)
    female_image = pygame.image.load(FEMALE_CHAR_ASSET)

    male_image = pygame.transform.scale(male_image, (128, 128))
    female_image = pygame.transform.scale(female_image, (128, 128))

    # Set up the input box
    input_box = pygame.Rect(250, 200, 300, 50)

    # Set up the radio buttons
    male_button = pygame.Rect(250, 300, 100, 50)
    female_button = pygame.Rect(450, 300, 100, 50)

    # Set up the buttons
    back_button = pygame.Rect(100, 500, 100, 50)
    start_button = pygame.Rect(600, 500, 100, 50)

    # Clear the screen
    screen.fill(white)

    # Draw the title
    title_text = title_font.render("Create your Avatar", True, black)
    screen.blit(title_text, (200, 100))

    # Draw the input box
    pygame.draw.rect(screen, gray, input_box)
    input_label = label_font.render("Avatar Name:", True, black)
    screen.blit(input_label, (100, 200))
    input_surface = label_font.render(currentName, True, black)
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 10))

    # Draw the radio buttons
    male_label = label_font.render("Male", True, black)
    screen.blit(male_label, (male_button.x + 10, male_button.y + 10))
    female_label = label_font.render("Female", True, black)
    screen.blit(female_label, (female_button.x + 10, female_button.y + 10))
    if playerGender == "M":
        pygame.draw.rect(screen, black, male_button, 2)
        screen.blit(male_image, (250, 350))
    elif playerGender == "F":
        pygame.draw.rect(screen, black, female_button, 2)
        screen.blit(female_image, (450, 350))

    # Draw the buttons
    pygame.draw.rect(screen, gray, back_button)
    back_label = label_font.render("Back", True, black)
    screen.blit(back_label, (back_button.x + 10, back_button.y + 10))
    pygame.draw.rect(screen, gray, start_button)
    start_label = label_font.render("Start", True, black)
    screen.blit(start_label, (start_button.x + 10, start_button.y + 10))

    return [Button(male_button, onMaleSelected), Button(female_button, onFemaleSelected), Button(back_button, backCB), Button(start_button, startGameCB)]

