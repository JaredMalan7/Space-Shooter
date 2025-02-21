import pygame
import random
import os

# Load enemy ship image and define enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join("assets", "enemy.png")  # Load enemy image
        self.image = pygame.image.load("assets/player.png") #Load Bullet
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 700)  # Random X position
        self.rect.y = random.randint(50, 150)   # Random starting Y position
        self.speed = random.randint(2, 4)  # Movement speed
        self.shoot_timer = random.randint(30, 90)  # Timer for shooting

    def update(self):
        # Enemy moves left & right
        self.rect.x += self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed = -self.speed  # Change direction

        # Enemy Shooting Mechanism
        self.shoot_timer -= 1
        if self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = random.randint(30, 90)  # Reset shoot timer

    def shoot(self):
        from bullet import Bullet  # Import here to avoid circular import
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 5)  # Enemy bullet
        return bullet  # This will be handled in `main.py`