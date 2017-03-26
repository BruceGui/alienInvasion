
#
# Gui Zhou
# 2017-03-26
#
#

import sys

import pygame
from bullet import Bullet


#
#  Check Key Down Events
#
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Action to keydown events"""
    if event.key == pygame.K_RIGHT:
        # Move Right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move Left
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move Up
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move Down
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

#
# Check Key Up Events
#
def check_keyup_events(event, ship):
    """Action to keyup events"""
    if event.key == pygame.K_RIGHT:
        # Move Right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move Left
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # Move Up
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # Move Down
        ship.moving_down = False

#
# Check All Events
#
def check_events(ai_settings, screen, ship, bullets):
    """A Game Functoin to check keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


#
# Fire When Press Space
#

def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire """
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


#
# Update bullet state
#
def update_bullet(bullets):
    """Update Bullet state"""
    bullets.update()

    # Remove the bullet can not see
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#
# Update Game Screen
#
def update_screen(ai_settings, screen, ship, bullets):
    """UPdate the game screen"""
    screen.fill(ai_settings.bg_color)

    # Update Bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()

