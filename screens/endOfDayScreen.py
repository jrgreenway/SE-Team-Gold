import math
from typing import Callable
import pygame

from buttons.button import Button
from metrics import Metrics

def draw_end_of_day_screen(
        screen: pygame.Surface, 
        startFrame: int, 
        currentFrame: int,
        oldMetrics: Metrics,
        newMetrics: Metrics,
        nextDayCB: Callable
) -> list[Button]:
    ''' draw_end_of_day_screen: pygame.Surface, int, int -> list[Button]
    Draws the end of day screen and returns a list of buttons.
    '''
    # 5 seconds and 5 seconds of animation

    # light blue color (RGB: 173, 216, 230)
    # deep blue color (RGB: 0, 0, 139)
    light_blue = (173, 216, 230)
    deep_blue = (0, 0, 139)

    color_cycle = [light_blue, deep_blue, deep_blue, light_blue]

    # Load the moon and sun icons
    moon_icon = pygame.image.load("assets/moon.png")
    sun_icon = pygame.image.load("assets/sun.png")

    # 5 seconds and 5 seconds of animation
    animation_duration = 8  # 10 seconds in total
    half_duration = animation_duration // 2

    # Calculate the progress of the animation
    # Convert frames to seconds
    progress = min((currentFrame - startFrame) / 60 , animation_duration)

    # Fill the screen with the background color

    background_color = color_cycle[math.floor(progress * 4 / animation_duration) % 4]
    screen.fill(background_color)


    # Calculate the angle of the arch based on the progress
    angle = math.pi * progress / half_duration
    radius = screen.get_width() / 2

    # Calculate the x and y coordinates of the moon and sun based on the angle
    sun_x = screen.get_width() / 2 + radius * math.sin(angle) - sun_icon.get_width() / 2
    sun_y = screen.get_height() - radius * math.cos(angle) - sun_icon.get_height() / 2
    moon_x = screen.get_width() / 2 - radius * math.sin(angle) - moon_icon.get_width() / 2
    moon_y = screen.get_height() + radius * math.cos(angle) - moon_icon.get_height() / 2

    # Draw the moon and sun at their calculated positions
    screen.blit(moon_icon, (moon_x, moon_y))
    screen.blit(sun_icon, (sun_x, sun_y))

    # Calculate the difference in metrics
    metric_diffs = {
        "Happiness" : newMetrics.getHappiness() - oldMetrics.getHappiness(),
        "Health" : newMetrics.getHealth() - oldMetrics.getHealth(),
        "Money" : newMetrics.getMoney() - oldMetrics.getMoney(),
    }

    # Set the font and font size for the summary text
    font = pygame.font.Font(None, 24)

    # Set the starting position for the summary text

    metric_text = font.render("A summary of your day", True, (255, 255, 255))

    text_x = screen.get_width() / 2 - metric_text.get_width() / 2
    text_y = screen.get_height() / 2 + 50

    screen.blit(metric_text, (text_x, text_y))

    text_y += metric_text.get_height() + 10

    # Display the summary for each metric
    for metric_name, metric_diff in metric_diffs.items():
        # Format the metric difference as a string with a sign (+ or -)
        metric_diff_str = f"{metric_diff:+}"
        
        # Create the text surface for the metric summary
        metric_text = font.render(f"{metric_name}: {metric_diff_str}", True, (255, 255, 255))
        text_x = screen.get_width() / 2 - metric_text.get_width() / 2
        # Blit the metric text onto the screen
        screen.blit(metric_text, (text_x, text_y))
        
        # Update the y position for the next metric summary
        text_y += metric_text.get_height() + 10

    # Create the button to go to the next day
    buttonRect = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() - 70, 100, 50)
    pygame.draw.rect(screen, (0, 0, 255), buttonRect)
    next_day_button = Button(
        buttonRect,
        nextDayCB,
    )
    buttonLabel = font.render("Next Day", True, (255, 255, 255))
    screen.blit(buttonLabel, buttonRect.move(10, 10))

    return [next_day_button]