import pygame
from pygame.sprite import Sprite

class Killer(Sprite):
    """A class to manage the killer."""

    def __init__(self, ai_game):
        """Initialize the killer and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the killer image and get its rect.
        self.image = pygame.image.load('images/killer.png')
        self.rect = self.image.get_rect()
        # Start each new killer at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the killer's exact horizontal position.
        self.x = float(self.rect.x)
        # Movement flag; start with a killer that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the killer's position based on the movement flag."""
        # Update the killer's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.killer_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.killer_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the killer at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_killer(self):
        """Center the killer on the screen."""    
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)