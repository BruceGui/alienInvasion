
#
# Gui Zhou
# 2017-03-19
#

import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    """ initialize the game and create a surface object """

    game_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Alien_Invasion')

    ship = Ship(screen)
    # Begin the main game loop
    while True:
        # Listen to event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Let the newest surface to show
        screen.fill(game_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()
