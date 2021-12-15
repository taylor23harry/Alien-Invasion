import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullet properties and behaviour."""
    def __init__(self, aigame):
        """Creates bullet instance at ship's position."""
        super().__init__()
        self.screen = aigame.screen
        self.settings = aigame.settings
        self.color = self.settings.bullet_color

        # Creates the bullet shape
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Places the bullet at the top of the ship
        self.rect.midtop = aigame.ship.rect.midtop
        
        # Store the ship's position accurately as a float
        self.y = float(self.rect.y)

    def update(self):
        """Update the bullet location."""
        self.y -= self.settings.bullet_speed
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet rect on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)