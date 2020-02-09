
#
# Game Setting Class
# Gui Zhou
# 2017-03-19
#

class Settings():
    """ Store all settings about aliens """

    def __init__(self):
        """Initialize setting"""
        self.screen_width = 500
        self.screen_height = 400
        self.bg_color = (211, 34, 53)

        # Ship moving speed
        self.ship_speed_factor = 0.2

        # Bullet Settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 4
        self.bullet_height = 21
        self.bullet_color = 45, 90, 78
        self.bullet_allowed = 9
