import pygame
import random
from player import Player
from asteroid import Asteroid
from enemy import Enemy
from bullet import Bullet
from boss import Boss  # Import Boss class

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

# Load Player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load Asteroids
asteroids = pygame.sprite.Group()
for _ in range(5):  # Create 5 asteroids at start
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Load Enemies
enemies = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Wave & Game Progression Variables
current_wave = 1
enemies_per_wave = 3  # Starts with 3 enemies
total_enemies_defeated = 18
max_enemies_to_defeat = 18  # Stop spawning after 18 enemies are defeated
wave_timer = 180  # Timer before next wave (3 seconds at 60 FPS)

# Boss Variables
boss = None
boss_bullets = pygame.sprite.Group()
boss_spawned = False

# Function to spawn a new wave of enemies
def spawn_wave():
    global current_wave, enemies_per_wave, total_enemies_defeated

    if total_enemies_defeated >= max_enemies_to_defeat:
        print("All enemies defeated! Prepare for Boss Battle...")
        return

    enemies_per_wave = min(current_wave + 2, max_enemies_to_defeat - total_enemies_defeated)

    for _ in range(enemies_per_wave):
        enemy_type = "ship-1.png" if current_wave % 2 == 1 else "ship-2.png"

        if current_wave >= 3:
            enemy_type = random.choice(["ship-1.png", "ship-2.png"])

        enemy = Enemy(enemy_type)
        all_sprites.add(enemy)
        enemies.add(enemy)

    current_wave += 1

# Boss Fight Logic
def spawn_boss():
    global boss, boss_spawned

    if not boss_spawned:
        print("Boss is entering the battle!")
        boss = Boss()
        all_sprites.add(boss)

        enemy1 = Enemy("ship-1.png")
        enemy2 = Enemy("ship-2.png")

        all_sprites.add(enemy1, enemy2)
        enemies.add(enemy1, enemy2)

        boss_spawned = True

# Spawn first wave at game start
spawn_wave()

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Shooting
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top, 7, is_player=True)
            all_sprites.add(bullet)
            bullets.add(bullet)

    # Get pressed keys
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Update Enemies & Handle Shooting
    for enemy in enemies:
        bullet = enemy.update()
        if bullet:
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

    # Boss Shooting Logic
    if boss:
        boss_bullets_list = boss.update()
        for boss_bullet in boss_bullets_list:
            all_sprites.add(boss_bullet)
            boss_bullets.add(boss_bullet)

    # Update Asteroids & Bullets
    asteroids.update()
    bullets.update()
    enemy_bullets.update()
    boss_bullets.update()

    # Collision Handling
    def handle_collisions():
        global total_enemies_defeated

        # 1. Player collides with Asteroids (Takes damage)
        if pygame.sprite.spritecollide(player, asteroids, False):
            player.take_damage()

        # 2. Player Bullets hitting Enemies (Destroy Enemies)
        enemy_hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if enemy_hits:
            total_enemies_defeated += len(enemy_hits)
            print("Enemy Destroyed!")

        # 3. Enemy Bullets hitting the Player (Takes damage)
        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            player.take_damage()

        # 4. Enemy colliding with Player (Game Over)
        if pygame.sprite.spritecollide(player, enemies, False):
            print("Game Over! Player crashed into an enemy.")
            pygame.quit()

        # 5. Player Bullets hitting Asteroids (Destroy Asteroids)
        asteroid_hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
        if asteroid_hits:
            print("Asteroid Destroyed!")
            for _ in range(len(asteroid_hits)):
                new_asteroid = Asteroid()
                all_sprites.add(new_asteroid)
                asteroids.add(new_asteroid)

        # 6. Player Bullets hitting Boss (Reduce Boss HP)
        if boss:
            boss_hits = pygame.sprite.spritecollide(boss, bullets, True)
            for _ in boss_hits:
                boss.take_damage(5)

            if boss.health <= 0:
                print("Boss Defeated!")
                boss.kill()
                pygame.quit()

        # 7. Boss Bullets hitting Player (Takes damage)
        if pygame.sprite.spritecollide(player, boss_bullets, True):
            player.take_damage()

    # Handle all collisions
    handle_collisions()

    # Check if all enemies are defeated before spawning a new wave or boss
    if not enemies:
        if total_enemies_defeated < max_enemies_to_defeat:
            wave_timer -= 1
            if wave_timer <= 0:
                spawn_wave()
                wave_timer = 180  # Reset timer for next wave
        else:
            spawn_boss()

    # Fill Screen Background
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Draw Player Health Bar
    player.draw_health_bar(screen)

    # Draw Boss Health Bar
    if boss:
        boss.draw_health_bar(screen)

    # Update Display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit PyGame
pygame.quit()