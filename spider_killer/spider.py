import pygame
from pygame.sprite import Sprite

class Spider(Sprite):
    """A class to represent a single spider in the fleet."""
    def __init__(self, ai_game):
        """Initialize the spider and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the spider image and set its rect attribute.
        self.image = pygame.image.load('images/Spider.png')
        self.rect = self.image.get_rect()
        # Start each new spider near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the spider's exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the spider to the right or left."""
        self.x += self.settings.spider_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Return True if spider is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    
    
    