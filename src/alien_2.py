import random
import pygame
from pygame.sprite import Sprite


class Alien_2(Sprite):
    """Class to represent 2nd level Aliens."""

    def __init__(self, aigame):
        pygame.init()
        self.screen, self.screen_rect = aigame.screen, aigame.screen_rect
        # Self
        self.image = pygame.image.load(
            'E:\\Programming\\Projects\Alien Invasion\\images\\Paranoid_1.png')
        self.rect = self.image.get_rect()
        # Places alien at top centre of screen
        self.rect.bottom = aigame.screen_rect.top
        self.rect.centerx = random.randint(
            self.screen_rect.left + 10, self.screen_rect.right - 10)
        # Stores accurate location as float
        self.x, self.y = float(self.rect.x), float(self.rect.y)

    def _update(self):
        """Updates alien location."""
        self.rect.x, self.rect.y = self.x, self.y

    def _draw_alien_2(self):
        """Draws alien to screen."""
        self.screen.blit(self.image, self.rect)
