import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, is_player=False):
        super().__init__()
        self.image = pygame.Surface((5, 15))  # Small bullet shape
        self.image.fill((255, 0, 0) if not is_player else (0, 255, 0))  # Red for enemies, green for player
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -speed if is_player else speed  # Player bullets go up, enemy bullets go down

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()  # Remove bullets when off-screen