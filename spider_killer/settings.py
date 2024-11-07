import pygame

class Settings:
    """A class to store all settings for Spider Killer."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800 
        self.bg_color = (0, 255, 255)
        self.bg_image = pygame.image.load("images/background.jpg") 
        # Killer settings
        self.killer_limit= 3
        # Fire settings
        self.fire_width = 3
        self.fire_height = 15
        self.fire_allowed = 20
       # Spider settings
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the spider point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.killer_speed = 8
        self.fire_speed = 9.0
        self.spider_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring settings
        self.spider_points = 50
    def increase_speed(self):
        """Increase speed settings and spider point values."""
        self.killer_speed *= self.speedup_scale
        self.fire_speed *= self.speedup_scale
        self.spider_speed *= self.speedup_scale

        self.spider_points = int(self.spider_points * self.score_scale)
        print(self.spider_points)