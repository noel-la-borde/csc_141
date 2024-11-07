import pygame
from pygame.sprite import Sprite

class Fire(Sprite):
    """A class to manage fireballs fired from the killer."""
    def __init__(self, ai_game):
        """Create a fire object at the killer's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
       
        self.image = pygame.image.load('images/fireball.png')
        # Create a fire rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.killer.rect.midtop
        # Store the fire position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the fire up the screen."""
        # Update the exact position of the fireball.
        self.y -= self.settings.fire_speed
        # Update the rect position.
        self.rect.y = self.y
    def draw_fire(self):
        """Draw the fire to the screen."""
        self.screen.blit(self.image, self.rect)