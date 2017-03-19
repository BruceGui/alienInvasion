
#
# A class to handle the ship
# Gui Zhou
# 2017-03-19
#

import pygame

class Ship():

    def __init__(self, screen):
        """ Initialize the ship and is start position"""
        self.screen = screen

        # Add the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put the ship in is right position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw The Ship"""
        self.screen.blit(self.image, self.rect)

