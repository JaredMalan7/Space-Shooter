import pygame
from player import Player
from asteroid import Asteroid
from enemy import Enemy
from bullet import Bullet

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

# Load Bullets
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Shooting
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top, 7, is_player=True)
            all_sprites.add(bullet)
            bullets.add(bullet)

    #Get pressed keys
    keys = pygame.key.get_pressed() #Gets current keyboard state

    #update Player Movement
    player.update(keys) # Calls update() to move the player

    #Update Enemies & shooting
    enemies.update()
    for enemy in enemies:
        bullet = enemy.shoot()
        if bullet:
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)


    #Update Asteroids
    asteroids.update()

    # Fill Screen Background
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update Display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit PyGame
pygame.quit()