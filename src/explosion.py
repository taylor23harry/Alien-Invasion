import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    """Explosion class for when a bullet collides with a Alien."""
    def __init__(self, aigame, bullet, alien):
        super().__init__()
        self.screen = aigame.screen
        self.image = pygame.image.load('E:\\Programming\\Projects\\Alien Invasion\\images\\boom1.PNG')
        self.rect = self.image.get_rect()
        # Set location to bullet.
        self.rect.y = alien.rect.centery
        self.rect.x = alien.rect.centerx
        self.rect.x -= 50
        self.rect.y -= 50
        # Animation
        self.current_image = 1
        self.first_pass = True

    def _draw_explosion(self):
        self.screen.blit(self.image, self.rect)