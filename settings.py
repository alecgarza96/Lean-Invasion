class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the games settings."""
        #screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (255,255,255)

        #ship settings
        self.ship_speed_factor = 5

        #Bullet settings
        self.bullet_speed_factor = 6
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5

        #lean settings
        self.lean_speed_factor = 4
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
