import pygame

# Initialize PyGame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60  # Frames per second

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creates Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill Screen Background
    screen.fill(BLACK)

    # Update Display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit PyGame
pygame.quit()