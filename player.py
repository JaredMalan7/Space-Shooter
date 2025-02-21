import pygame
import os


# Load player image and define player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(400, 500))
        self.speed = 5  # Movement speed
        self.health = 3 # Player starts with 3 health points

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed  # Move left
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed  # Move right

    def take_damage(self):
        #Reduces player health when hit
        self.health -= 1
        if self.health <= 0:
            print("Game Over!")
            pygame.quit()  # Exit game when health reaches 0

    #Draws the health bar as 3 green rectangles at the top-left corner.
    def draw_health_bar(self, screen):
        bar_width = 30
        bar_height = 10
        spacing = 5
        x = 20
        y = 20
        neon_green = (57, 255, 20) #neon green

        for i in range(self.health):
            pygame.draw.rect(screen, neon_green, (x + (i * (bar_width + spacing)), y, bar_width, bar_height))