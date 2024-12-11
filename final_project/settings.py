import pygame
class Settings:

    def __init__(self):
        self.screen_width= 1200
        self.screen_height= 800
        self.bg_color = (255, 0, 0)
        self.bg_image= pygame.image.load("candy_collector/images/bg.jpg")
        

        
        self.collector_limit= 3

        
        self.basket_width = 3
        self.basket_height = 15
        self.basket_allowed = 20

        
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        
        self.collector_speed= 5
        self.basket_speed = 2.5
        self.candy_speed = 3
        self.candy_points = 50
        self.fleet_direction = 1
    
    def increase_speed(self):
        
        self.collector_speed *= self.speedup_scale
        self.basket_speed *= self.speedup_scale
        self.candy_speed *= self.speedup_scale

        self.candy_points = int(self.candy_points * self.score_scale)
        print(self.candy_points)
        

