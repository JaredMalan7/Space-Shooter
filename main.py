import pygame
import random
from player import Player
from asteroid import Asteroid
from enemy import Enemy
from bullet import Bullet
from boss import Boss

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
for _ in range(5):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Load Enemies
enemies = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Level & Wave Progression Variables
current_level = 1
max_level = 3
current_wave = 1
enemies_per_wave = 3
total_enemies_defeated = 18
max_enemies_to_defeat = 18
wave_timer = 180

# Boss Variables
boss = None
boss_bullets = pygame.sprite.Group()
boss_spawned = False
level_transitioning = False
level_transition_timer = 300  # 5-second delay before next Level

# Enemy ship variations per level
enemy_types_by_level = {
    1: ["ship-1.png", "ship-2.png"],
    2: ["ship-3.png", "ship-4.png"],
    3: ["ship-5.png", "ship-6.png"]
}

# Boss ship variations per level
boss_types_by_level = {
    1: "boss-1.png",
    2: "boss-2.png",
    3: "boss-3.png"
}

def spawn_wave():
    global current_wave, enemies_per_wave, total_enemies_defeated

    if total_enemies_defeated >= max_enemies_to_defeat:
        return

    print(f"🌊 Spawning Wave {current_wave}")

    enemies_per_wave = min(current_wave + 2, max_enemies_to_defeat - total_enemies_defeated)

    for _ in range(enemies_per_wave):
        enemy_type = random.choice(enemy_types_by_level[current_level])
        enemy = Enemy(enemy_type,
                      speed_increase=(current_level - 1) * 1,
                      shoot_faster=(current_level - 1) * 10,
                      bullets_per_shot=current_level)
        all_sprites.add(enemy)
        enemies.add(enemy)

    current_wave += 1

def spawn_boss():
    global boss, boss_spawned, current_level

    if not boss_spawned and current_level <= max_level:
        print(f"⚠️ Boss-{current_level} is entering the battle! ⚠️")
        boss_image = boss_types_by_level[current_level]
        boss = Boss(boss_image, bullets_per_shot=current_level + 1)
        all_sprites.add(boss)
        boss_spawned = True

# Spawn first wave
spawn_wave()

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top, 7, is_player=True)
            all_sprites.add(bullet)
            bullets.add(bullet)

    keys = pygame.key.get_pressed()
    player.update(keys)

    for enemy in enemies:
        bullets_from_enemy = enemy.update()
        for bullet in bullets_from_enemy:
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

    if boss:
        boss_bullets_list = boss.update()
        for boss_bullet in boss_bullets_list:
            all_sprites.add(boss_bullet)
            boss_bullets.add(boss_bullet)

    asteroids.update()
    bullets.update()
    enemy_bullets.update()
    boss_bullets.update()

    def handle_collisions():
        global total_enemies_defeated, level_transitioning, boss, boss_spawned, running

        if pygame.sprite.spritecollide(player, asteroids, False):
            player.take_damage()

        enemy_hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if enemy_hits:
            total_enemies_defeated += len(enemy_hits)
            print(f"Enemies Defeated: {total_enemies_defeated}")

        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            player.take_damage()

        if pygame.sprite.spritecollide(player, boss_bullets, True):
            player.take_damage()

        if pygame.sprite.spritecollide(player, enemies, False):
            print("Game Over! Player crashed into an enemy.")
            pygame.quit()

        asteroid_hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
        if asteroid_hits:
            for _ in range(len(asteroid_hits)):
                new_asteroid = Asteroid()
                all_sprites.add(new_asteroid)
                asteroids.add(new_asteroid)

        if boss:
            boss_hits = pygame.sprite.spritecollide(boss, bullets, True)
            for _ in boss_hits:
                boss.take_damage(5)

            if boss.health <= 0:
                print(f"Boss-{current_level} Defeated!")

                # ENSURE ALL BOSS BULLETS ARE REMOVED IMMEDIATELY
                for bullet in boss_bullets:
                    all_sprites.remove(bullet)  # Remove from screen
                boss_bullets.empty()  # Clear bullet group

                # ENSURE BOSS IS REMOVED COMPLETELY
                all_sprites.remove(boss)
                boss.kill()
                boss = None
                boss_spawned = False

                if current_level < max_level:
                    level_transitioning = True
                    level_transition_timer = 300
                else:
                    print("🎉 YOU WIN! Game Over.")
                    running = False

    handle_collisions()

    if not enemies and total_enemies_defeated < max_enemies_to_defeat:
        wave_timer -= 1
        if wave_timer <= 0:
            spawn_wave()
            wave_timer = 180

    if total_enemies_defeated >= max_enemies_to_defeat and not boss_spawned and not level_transitioning:
        spawn_boss()

    # ENSURE NO BOSS APPEARS DURING LEVEL TRANSITION
    if level_transitioning:
        level_transition_timer -= 1
        if level_transition_timer <= 0:
            current_level += 1
            print(f"🚀 LEVEL {current_level} STARTING! 🚀")

            total_enemies_defeated = 0
            current_wave = 1
            boss = None
            boss_spawned = False
            enemies.empty()
            enemy_bullets.empty()
            boss_bullets.empty()

            spawn_wave()
            level_transitioning = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    player.draw_health_bar(screen)
    if boss:
        boss.draw_health_bar(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()