import pygame

class Ship:
    """Main Ship class."""
    def __init__(self, aigame):
        """Initialises ship attributes"""
        # Creates main screen hitbox
        self.screen = aigame.screen
        self.screen_rect = aigame.screen.get_rect()

        # Ship Attributes
        self.settings = aigame.settings
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Sets Ship image and creates hitbox
        
        self.image = pygame.image.load('E:\\Programming\\Projects\\Alien Invasion\\images\\player_idle1.png')
        self.image = pygame.transform.scale(self.image, self.settings.ship_scale)
        self.rect = self.image.get_rect()

        # Start each new ship  at the bottom centre of the screen
        self.rect.midtop = self.screen_rect.midbottom
        self.rect.y = self.screen_rect.bottom + 20

        # Stores the Ship's position accurately in a float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self, aigame):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if aigame.game_on and self.rect.bottom > self.screen_rect.bottom:
            self.y -= 0.1
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        # Places the ship on the screen
        self.image = pygame.transform.scale(self.image, (23,37))
        self.screen.blit(self.image, self.rect)