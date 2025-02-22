import pygame
import random
import os
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, ship_type="ship-1.png", speed_increase=0, shoot_faster=0, bullets_per_shot=1):
        super().__init__()
        image_path = os.path.join("assets", ship_type)  # Load enemy image dynamically
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize enemy
        self.rect = self.image.get_rect()

        # X position is fixed but random within range
        self.rect.x = random.randint(100, 700)  # Random X position
        self.rect.y = -50  # Start ABOVE the screen

        self.target_y = random.randint(50, 150)  # Randomized Y position every time
        self.entry_speed = 2  # Speed of descending animation
        self.speed = random.randint(2, 4) + speed_increase  # Increase speed per level

        # Shooting Cooldown
        self.base_shoot_timer = random.randint(60, 120) - shoot_faster  # Faster shooting in higher levels
        self.shoot_timer = self.base_shoot_timer  # Reset timer
        self.bullets_per_shot = bullets_per_shot  # Number of bullets fired per shot

    def update(self):
        # Move the enemy down if it hasn't reached its target Y-position
        if self.rect.y < self.target_y:
            self.rect.y += self.entry_speed  # Move down slowly
        else:
            # Enemy moves left & right after reaching position
            self.rect.x += self.speed
            if self.rect.right >= 800 or self.rect.left <= 0:
                self.speed = -self.speed  # Change direction

            # Enemy Shooting Cooldown
            if self.shoot_timer > 0:
                self.shoot_timer -= 1  # Countdown

            # Enemy Shooting Mechanism (only fires when timer reaches 0)
            if self.shoot_timer <= 0:
                bullets = self.shoot()
                self.shoot_timer = self.base_shoot_timer  # Reset Cooldown
                return bullets  # Return list of bullets

        return []  # Return empty list if no bullets are shot

    def shoot(self):
        # Fires multiple bullets at once
        bullets = []
        for i in range(self.bullets_per_shot):
            bullet_x_offset = -10 + (i * 10)  # Space bullets apart
            bullet = Bullet(self.rect.centerx + bullet_x_offset, self.rect.bottom, 5)
            bullets.append(bullet)
        return bullets