
#
# A class to handle the ship
# Gui Zhou
# 2017-03-19
#

import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Initialize the ship and is start position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Add the ship image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put the ship in is right position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.moving_speed = self.ai_settings.ship_speed_factor

        self.moving_right = False
        self.moving_down = False
        self.moving_left = False
        self.moving_up = False

    def update(self):
        """Update ship move state"""
        if self.moving_left and self.rect.left > 0:
            self.center -= self.moving_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.moving_speed
        elif self.moving_up and self.rect.bottom > 48:
            self.bottom -= self.moving_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.moving_speed

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw The Ship"""
        self.screen.blit(self.image, self.rect)

