import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, is_player=False):
        super().__init__()

        # Load different bullet images for player and enemy
        if is_player:
            image_path = os.path.join("assets", "player-bullet.png")  # Player bullet image
        else:
            image_path = os.path.join("assets", "enemy-bullet.png")  # Enemy bullet image

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (10, 20))  # Resize bullet

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -speed if is_player else speed  # Player bullets go up, enemy bullets go down

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()  # Remove bullets when off-screen