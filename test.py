import pygame
import sys

pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Location Maps")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Button class
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, location_map):
        super().__init__()
        self.image = font.render(text, True, white)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.location_map = location_map

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

# Create buttons
buttons = pygame.sprite.Group()
buttons.add(Button(50, 50, "Home", "assets/bed.png"))
buttons.add(Button(150, 50, "Office", "assets/sink.png"))
# buttons.add(Button(250, 50, "Park", "park_map.png"))

# Screen text
screen_text = ""

def change_screen(location_map):
    global screen_text
    screen_text = f"Map of {location_map}"

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_hovered():
                    change_screen(button.location_map)

    screen.fill(black)

    # Draw buttons
    buttons.draw(screen)

    # Draw screen text
    screen_text_render = font.render(screen_text, True, white)
    screen.blit(screen_text_render, (50, 150))

    pygame.display.flip()
