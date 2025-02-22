import pygame
import random
import os
from bullet import Bullet

class Boss(pygame.sprite.Sprite):
    def __init__(self, boss_image, health=100, bullets_per_shot=2, fire_rate=40):
        super().__init__()
        image_path = os.path.join("assets", boss_image)  # Load boss image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize boss
        self.rect = self.image.get_rect(center=(400, -100))  # Start off-screen

        self.target_y = 100  # Where the boss stops moving down
        self.entry_speed = 2  # Speed of descending animation
        self.speed = 3  # Side movement speed
        self.health = health  # Boss starts with different HP based on level
        self.shoot_timer = random.randint(fire_rate, fire_rate + 20)  # Shooting cooldown
        self.bullets_per_shot = bullets_per_shot  # Boss shoots multiple bullets per level

    def update(self):
        # Move down until it reaches its target position
        if self.rect.y < self.target_y:
            self.rect.y += self.entry_speed
        else:
            # Move left & right after reaching position
            self.rect.x += self.speed
            if self.rect.right >= 800 or self.rect.left <= 0:
                self.speed = -self.speed  # Change direction

            # Boss Shooting Cooldown
            if self.shoot_timer > 0:
                self.shoot_timer -= 1  # Countdown

            # Boss Shooting Mechanism
            if self.shoot_timer == 0:
                return self.shoot()

        return []

    def shoot(self):
        # Boss shoots two bullets at once.
        bullets = []
        for i in range(self.bullets_per_shot):
            bullet_x_offset = -15 + (i * 15)  # Space bullets apart
            bullet = Bullet(self.rect.centerx + bullet_x_offset, self.rect.bottom, 6)
            bullets.append(bullet)

        self.shoot_timer = random.randint(40, 80)  # Reset cooldown
        return bullets

    def draw_health_bar(self, screen):
        # Displays the boss health bar at the top center.
        bar_width = 300
        bar_height = 15
        x = 250  # Centered on the screen
        y = 10  # Top of the screen
        red = (255, 0, 0)
        green = (0, 255, 0)

        # Background of health bar (empty part)
        pygame.draw.rect(screen, red, (x, y, bar_width, bar_height))

        # Foreground (health remaining)
        health_percentage = max(self.health / 100, 0)  # Prevent negative width
        pygame.draw.rect(screen, green, (x, y, bar_width * health_percentage, bar_height))

    def take_damage(self, damage):
        #Reduces boss health when hit.
        self.health -= damage
        if self.health <= 0:
            print("Boss Defeated!")
            self.kill()  # Remove boss from game



