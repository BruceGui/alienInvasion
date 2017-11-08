
#
# Gui Zhou
# 2017-03-26
#

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Management Ship Bullet"""

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet at the location of current ship """
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # Update Bullet Location
    def update(self):
        """Location Update"""
        self.y -= self.speed_factor
        self.rect.y = self.y


    # Draw The BulletN
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

