import pygame
import random
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, ship_type="ship-1.png"):  # Default to "ship-1.png"
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
        self.speed = random.randint(2, 4)  # Side movement speed

        # Shooting Cooldown
        self.shoot_timer = random.randint(60, 120)

    def update(self):
        # Move the enemy **down** if it hasn't reached its target Y-position
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

            # Enemy Shooting Mechanism
            if self.shoot_timer == 0:
                return self.shoot()  # Return bullet for main.py to handle
        return None  # If no shooting happens, return None

    def shoot(self):
        from bullet import Bullet  # Import here to avoid circular import
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 5)  # Enemy bullet
        self.shoot_timer = random.randint(60, 120)  # Reset cooldown
        return bullet