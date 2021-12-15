import sys
import pygame
import random
from pygame.sprite import Sprite
from ship import Ship
from alien import Alien
from alien_2 import Alien_2
from bullet import Bullet
from explosion import Explosion
from settings import Settings


def start_menu_off(aigame):
    aigame.background = pygame.image.load(
        'E:\\Programming\\Projects\\Alien Invasion\\images\\stars.jpg')
    aigame.background_rect = aigame.background.get_rect()


class AlienInvasion:
    """Main game class that manages game behaviour."""

    def __init__(self):
        """Initialises the main game attributes."""
        pygame.init()
        pygame.font.init()
        self.game_font = pygame.font.Font(None, 30)
        # Creates settings instance.
        self.settings = Settings()
        # Initialises screen.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        # creates ship, alien and explosion instances.
        self.ship = Ship(self)
        self.alien = Alien(self)
        self.alien_2 = Alien_2(self)
        # Creates sprite groups.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.aliens_2 = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        # Background.
        self.background = pygame.image.load(
            'E:\\Programming\\Projects\\Alien Invasion\\images\\start_screen.jpg')
        self.background_rect = self.background.get_rect()
        self.background_rect.center = self.screen_rect.center
        # Other Attributes.
        self.max_bullets = self.settings.max_bullets
        # Timer Attributes for Ship and Alien animation.
        self.timer = 0
        self.animation_timer = 0
        self.current_image = 1
        self.current_explosion = 1
        # Amount of time the game waits before spawning aliens after start screen.
        self.game_start_timer = 0
        self.alien_timer = random.randint(
            self.settings.alien_min_time, self.settings.alien_max_time)
        # Score counter
        self.score = 0

        # Start game after start screen

        self.game_on = 0

    def run_game(self):
        """Starts the game loop."""
        while True:
            self._check_events()
            self._update_screen()
            self._check_collisions()

    def _animate_image(self):
        """Changes images of Ship, Alien and Explosions to show illusion
         of animation."""
        # Increment timer
        self.timer += 1
        self.animation_timer += 1
        self.game_start_timer += 1
        if self.timer == self.alien_timer:
            self.spawn_alien()
            self._randomise_spawn()
            self.timer = 0
        if self.animation_timer == 200:
            if self.current_image == 1:
                self.ship.image = pygame.image.load(
                    'E:\\Programming\\Projects\\Alien Invasion\\images\\player_idle2.png')
                if self.settings.logs == 2:
                    print(f"Set Alien and ship images to 2.")
                for a in self.aliens:
                    a.image = pygame.image.load(
                        'E:\\Programming\\Projects\\Alien Invasion\\images\\Alien1_2.png')
                self.current_image = 2
                self.animation_timer = 0
                # if self.settings.logs == 1:
                #    print("Changed Ship and Alien images to 2")
            else:
                self.ship.image = pygame.image.load(
                    'E:\\Programming\\Projects\\Alien Invasion\\images\\player_idle1.png')
                if self.settings.logs == 2:
                    print(f"Set Alien and ship images to 1.")
                for a in self.aliens:
                    a.image = pygame.image.load(
                        'E:\\Programming\\Projects\\Alien Invasion\\images\\Alien1_1.png')
                self.current_image = 1
                self.animation_timer = 0
                # if self.settings.logs == 1:
                #    print("Changed Ship and Alien images to 1")
        # Animate explosions
        """The following block uses timers and a boolean to animate to the 1st,
         2nd, 3rd image of explosion. Then back to
         2nd and 1st again, before deleting itslef."""
        if self.animation_timer % 50 == 0:
            for e in self.explosions:
                if e.current_image == 1:
                    if self.settings.logs > 2:
                        print(f"Set {e} image to 2.")
                    e.image = pygame.image.load(
                        'E:\\Programming\\Projects\\Alien Invasion\\images\\boom2.PNG')
                    if e.first_pass == True:
                        e.current_image = 2
                elif e.current_image == 2:
                    e.image = pygame.image.load(
                        'E:\\Programming\\Projects\\Alien Invasion\\images\\boom3.PNG')
                    if self.settings.logs > 2:
                        print(f"Set {e} image to 3.")
                    if e.first_pass == True:
                        e.current_image = 3
                else:
                    e.image = pygame.image.load(
                        'E:\\Programming\\Projects\\Alien Invasion\\images\\boom1.PNG')
                    if self.settings.logs > 2:
                        print(f"Set {e} image to 1.")
                        e.current_image = 1
                    else:
                        self.explosions.remove(e)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_on == 0:
                    self.game_on = 1
                    start_menu_off(self)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the right.
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fires bulets
            self._fire_bullets()
            if self.game_on == 0:
                self.game_on = 1
                start_menu_off(self)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop moving the ship to the left.
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            # Quit game if 'q' is pressed
            sys.exit()

    def _update_bullets(self):
        """Updates position of bullets and deletes old bullets."""
        # Removes bullets off screen
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Updates bullets on screen.
        self.bullets.update()
        for b in self.bullets:
            b.draw_bullet()

    def _update_alien(self):
        """Draws each alien."""
        # Deletes alien when it gets to the bottom of the screen
        for a in self.aliens:
            if a.rect.top > self.screen_rect.bottom:
                self.aliens.remove(a)
        # Draws and updates each alien individually
        for a in self.aliens:
            a.image = pygame.transform.scale(
                a.image, self.settings.alien_scale)
            a.update_alien()
        #    a._blitme()

    def _fire_bullets(self):
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.max_bullets:
            self.bullets.add(new_bullet)
            if self.settings.logs >= 1:
                print(f"Bullet Fired! Total bullets : {len(self.bullets)}")

    def spawn_alien(self):
        new_alien = Alien(self)
        if len(self.aliens) < self.settings.max_aliens and self.game_start_timer > 1000:
            self.aliens.add(new_alien)
            if self.settings.logs >= 1:
                print(f"Alien spawned! Toal aliens : {len(self.aliens)}")

    def _check_collisions(self):
        """Checks to see if X and Y coordinates of any bullets collide with Aliens."""
        for bullet in self.bullets:
            for a in self.aliens:
                if bullet.rect.top > a.rect.top and bullet.rect.top < a.rect.bottom and bullet.rect.centerx > a.rect.left and bullet.rect.centerx < a.rect.right:
                    self._alien_hit(self, bullet, a)
                    self.aliens.remove(a)
                    self.bullets.remove(bullet)
                    self.score += 1

    def _alien_hit(self, aigame, bullet, a):
        """Registers the hit and calls the explosion animation."""
        new_explosion = Explosion(self, bullet, a)
        self.explosions.add(new_explosion)

    def _draw_explosions(self):
        """Draws the explosion images."""
        for explosion in self.explosions:
            explosion._draw_explosion()

    def _randomise_spawn(self):
        """Randomises the value the timer needs to reach before spawning another alien."""
        self.alien_timer = random.randint(
            self.settings.alien_min_time, self.settings.alien_max_time)

    def _draw_score(self):
        """Draws the score on the top left."""
        score_text = self.game_font.render(
            f"Score : {str(self.score)}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.x, score_rect.y = self.screen_rect.right - \
            (score_rect.right - score_rect.left) - 10, 5
        self.screen.blit(score_text, score_rect)

    def _check_for_level_up(self):
        """Compares score to that of level up requirements, and modifies game accordingly."""
        if self.score >= self.settings.level_1up_score:
            self._levelup(1)

    def _levelup(self, level):
        """Changes game behaviour for a levelup."""
        if level == 1:  # Current level
            """Spawn alien2."""
            new_alien_2 = Alien_2(self)
            if len(self.aliens) < self.settings.max_aliens and self.game_start_timer > 1000:
                self.aliens_2.add(new_alien_2)

    def _update_screen(self):
        """Updates the screen with new info."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background, self.background_rect)
        # Draws images to screen
        if self.game_on == 1:
            # self._check_for_level_up()
            self.ship.blitme()
            self.ship.update(self)
            self._update_bullets()
            self._update_alien()
            self.aliens.draw(self.screen)
            self._draw_explosions()
            self._animate_image()
            self._draw_score()
        # Flips the newest drawn screen for the old one.
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
