import pygame
import random
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join("assets", "ship-1.png")  # Load enemy image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 700)  # Random X position
        self.rect.y = random.randint(50, 150)   # Random starting Y position
        self.speed = random.randint(2, 4)  # Movement speed

        # Shooting Cooldown Fix
        self.shoot_timer = 0  # Initial shoot delay
        self.shoot_cooldown = random.randint(60, 120)  # Set cooldown (1-2 seconds)

    def update(self):
        # Enemy moves left & right
        self.rect.x += self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed = -self.speed  # Change direction

        # Enemy Shooting Cooldown
        if self.shoot_timer > 0:
            self.shoot_timer -= 1  # Countdown

        # Shoot only when cooldown reaches 0
        if self.shoot_timer <= 0:
            self.shoot_timer = self.shoot_cooldown  # Reset cooldown
            return self.shoot()  # Return a bullet instead of modifying groups

        return None  # If not shooting, return None

    def shoot(self):
        from bullet import Bullet  # this is here to avoid a bullet circular import
        return Bullet(self.rect.centerx, self.rect.bottom, 5)  # Create an enemy bullet