import sys 
from time import sleep
import pygame 
from settings import Settings
from collector import Collector
from basket import Basket
from candy import Candy
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class CandyCollector: 

    def __init__(self):
        
        pygame.init()
        self.clock= pygame.time.Clock()
        self.settings= Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Candy Collector")
        self.stats = GameStats(self)
        self.bg_color= (255, 0, 0)
        self.collector = Collector(self)
        self.sb = Scoreboard(self)
        self.basket = pygame.sprite.Group()
        self.candy = pygame.sprite.Group()
        

        self.game_active = False

        self.play_button = Button(self, "Play Game")

        self._create_fleet()

        
          
    def run_game(self):
        
        while True:
            self._check_events()

            self.screen.blit(self.settings.bg_image, (0, 0))

            if self.game_active:
                self.collector.update()
                self._update_basket()
                self._update_candy()

            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.collector.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.collector.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_basket()

    def _check_keyup_events(self, event):
            
        if event.key == pygame.K_RIGHT:
            self.collector.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.collector.moving_left = False

    def _create_candy(self, x_position, y_position):

        new_candy = Candy(self)
        new_candy.x = x_position
        new_candy.rect.x = x_position
        new_candy.rect.y = y_position
        self.candy.add(new_candy)
    
    def _fire_basket(self):
        
        if len(self.basket) < self.settings.basket_allowed:
            new_basket = Basket(self)
            self.basket.add(new_basket)

    def _update_basket(self):
        self.basket.update()

        for basket in self.basket.copy():
            if basket.rect.bottom <= 0:  
                self.basket.remove(basket)
        
        self._check_basket_candy_collisions()

    def _check_basket_candy_collisions(self):

        collisions = pygame.sprite.groupcollide(self.basket, self.candy, True, True)

        if collisions:
            for candy in collisions.values():
                self.stats.score += self.settings.candy_points * len(candy)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.candy:
            self.basket.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        
        candy = Candy(self)
        candy_width, candy_height = candy.rect.size

        current_x, current_y = candy_width, candy_height
        while current_y < (self.settings.screen_height - 3 * candy_height):

            while current_x < (self.settings.screen_width - 2 * candy_width):
                self._create_candy(current_x, current_y)
                current_x += 2 * candy_width
            
            current_x = candy_width
            current_y += 2 * candy_height
       

    def _update_screen(self):
       
        self.screen.blit(self.settings.bg_image, (0, 0))
        for basket in self.basket.sprites():
            basket.draw_basket()
        self.collector.blitme()
        self.candy.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()
       
        pygame.display.flip()
    
    def _update_candy(self):
        
        self._check_fleet_edges()
        self.candy.update()

        if pygame.sprite.spritecollideany(self.collector, self.candy):
            self._collector_hit()
        
        self._check_candy_bottom()

    def _collector_hit(self):

        if self.stats.collector_left > 0:  
            self.stats.collector_left -= 1
            self.sb.prep_collector()
                
            self.basket.empty()
            self.candy.empty()
                
            self._create_fleet()
            self.collector.center_collector()
                
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
        
    
    def _check_fleet_edges(self):

        for candy in self.candy.sprites():
            if candy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):

        for candy in self.candy.sprites():

            candy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_candy_bottom(self):
        
        for candy in self.candy.sprites():
            if candy.rect.bottom >= self.settings.screen_height:
                
                self._collector_hit()
                break

    def _check_play_button(self, mouse_pos):
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_collector()
            self.game_active = True

            self.basket.empty()
            self.candy.empty()
            
            self._create_fleet()
            self.collector.center_collector()

            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    
    ai = CandyCollector()
    ai.run_game()
    
