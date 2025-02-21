import pygame
from player import Player
from asteroid import Asteroid
from enemy import Enemy

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

#Load Player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Load Asteroid
asteroids = pygame.sprite.Group()
for _ in range(5): #Create 5 asteroid to start
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Load Enemies
enemies = pygame.sprite.Group()
for _ in range(3):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get pressed keys
    keys = pygame.key.get_pressed() #Gets current keyboard state

    #update Player Movement
    player.update(keys) # Calls update() to move the player

    #Update Asteroids
    asteroids.update()

    #Update Enemies
    enemies.update()


    # Fill Screen Background
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update Display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit PyGame
pygame.quit()