import random
import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """A class to represent a single alien in a fleet."""

    def __init__(self, aigame):
        """Initialises alien and set its starting postition."""
        super().__init__()
        self.settings = Settings()
        # Screen
        self.screen, self.screen_rect = aigame.screen, aigame.screen_rect
        # Alien
        self.image = pygame.image.load(
            'E:\\Programming\\Projects\\Alien Invasion\\images\\Alien1_1.png')
        self.image = pygame.transform.scale(
            self.image, self.settings.alien_scale)
        self.rect = self.image.get_rect()
        # Places alien on top of screen
        self.rect.bottom = aigame.screen_rect.top
        self.rect.centerx = random.randint(
            self.screen_rect.left + 10, self.screen_rect.right - 10)

        self.x = self.rect.x
        self.y = self.rect.y

    def update_alien(self):
        self.rect.y = self.y
        self.y += self.settings.alien_speed

    def _blitme(self):
        self.screen.blit(self.image, self.rect)
