
import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game state
    
    # Draw to the screen
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
