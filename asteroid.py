import pygame
import random
import os

# Load asteroid image and define asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join("assets", "asteroid.png")  # Ensure image exists
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Resize asteroid
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)  # Random X position (screen width - asteroid width)
        self.rect.y = random.randint(-100, -40)  # Start above the screen
        self.speed = random.randint(2, 6)  # Random falling speed

    def update(self):
        self.rect.y += self.speed  # Move asteroid down
        if self.rect.top > 600:  # If asteroid goes off screen, reset position
            self.rect.x = random.randint(0, 760)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(2, 6)

