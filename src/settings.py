import random

class Settings:
    def __init__(self):
        ## Game speed
        self.game_speed = 1
        # Screen
        self.bg_color = (0,0,0)
        self.screen_width, self.screen_height = 500, 700
        # Ship
        self.ship_speed = self.game_speed / 10
        self.ship_scale = (30,48) # Width and height for pygame transform scaling.
        # Bullet
        self.bullet_speed = self.game_speed / 8
        self.bullet_height, self.bullet_width = 12, 3
        self.bullet_color = (255,255,255)
        self.max_bullets = 3
        # Alien
        self.alien_speed = self.game_speed / 40
        self.max_aliens = 99 # Max aliens that can appear on screen
        self.alien_min_time, self.alien_max_time = 5000, 8000 # Time between alien spawns in Level 1
        self.alien_time_2 = random.randint(500,1000) # Time between alien spawns in Level 2
        self.alien_time_3 = random.randint(30,200) # Time between alien spawns in Level 3
        self.alien_scale = (30,48) # Width and height for pygame transform scaling.
        # Levels
        self.level_1up_score = 10
        """Debugging."""
        self.logs = 2 # Print logs to terminal, 0 == True, 1 == False, 2 == True + Animations