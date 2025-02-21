import pygame
import random
import os

# Load enemy ship image and define enemy class
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
        self.shoot_timer = random.randint(30, 90)  # Timer for shooting

    def update(self):
        # Enemy moves left & right
        self.rect.x += self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed = -self.speed  # Change direction

