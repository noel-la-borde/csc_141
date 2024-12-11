import pygame
from pygame.sprite import Sprite

class Basket(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen= ai_game.screen 
        self.settings= ai_game.settings

        self.image = pygame.image.load('candy_collector/images/basket1.png')

        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.collector.rect.midbottom
    
        self.y = float(self.rect.y)

    def update(self):
        
        self.y -= self.settings.basket_speed
        
        self.rect.y = self.y
    
    def draw_basket(self):
        
        self.screen.blit(self.image, self.rect)