
#
# Gui Zhou
# 2017-03-19
#

import sys
import pygame
import game_functions as gf

from settings import Settings
from pygame.sprite import Group
from ship import Ship


def run_game():
    """ initialize the game and create a surface object """

    game_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Alien_Invasion')

    ship = Ship(game_settings, screen)

    # Create a Group to Store Bullet
    bullets = Group()

    # Begin the main game loop
    while True:
        # Listen to event
        gf.check_events(game_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullet(bullets)
        # Let the newest surface to show
        gf.update_screen(game_settings, screen, ship, bullets)

if __name__ == '__main__':
    run_game()
