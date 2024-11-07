import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from killer import Killer
from fire import Fire
from spider import Spider 
from time import sleep


class SpiderKiller:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Spider Killer")
        # Create an instance to store game statistics,
        # and create a scoreboard.
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        # Set the background color.
        self.bg_color = (0, 255, 255, 255)
  
       
        self.killer= Killer(self)
        self.fire = pygame.sprite.Group()
        self.spider = pygame.sprite.Group()

        # Start Spider Killer in an inactive state.
        self.game_active = False
        # Make the Play button.
        self.play_button = Button(self, "Start Game")
        
    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            self._check_events()
            # Redraw the screen during each pass through the loop.
            self.screen.blit(self.settings.bg_image, (0, 0))
            
            if self.game_active:
                self.killer.update()
                self._update_fire()
                self._update_spider()
                self.killer.blitme()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.game_active:
                # Reset the game settings.
                self.settings.initialize_dynamic_settings()
                # Reset the game statistics.
                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_killer()
                self.game_active = True
                # Get rid of any remaining fireballs and spiders.
                self.fire.empty()
                self.spider.empty()
                # Create a new fleet and center the .
                self._create_fleet()
                self.killer.center_killer()
                # Hide the mouse cursor.
                pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            self.killer.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.killer.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_fire()
    def _check_keyup_events(self, event):
        """Respond to key releases."""
           
        if event.key == pygame.K_RIGHT:
            self.killer.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.killer.moving_left = False
                    
            # Move the killer to the right.
            self.killer.rect.x += 1    

    def _fire_fire(self):
        """Create a new fire and add it to the fireball's group."""
        if len(self.fire) < self.settings.fire_allowed:
            new_fire = Fire(self)
            self.fire.add(new_fire)

        
    def _update_fire(self):
        """Update position of fire and get rid of old fireballs."""
        # Update fire positions.
        self.fire.update()

        # Get rid of fire that have disappeared.
        for fire in self.fire.copy():
            if fire.rect.bottom <= 0:
                self.fire.remove(fire)
        
        self._check_fire_spider_collisions()
    
    def _check_fire_spider_collisions(self):
        """Respond to fireball-spider collisions."""
        # Remove any fireballs and spiders that have collided.
        # Check for any fireball that have hit spiders.
        # If so, get rid of the fireball and the spider.
        collisions = pygame.sprite.groupcollide(
                self.fire, self.spider, True, True)
        
        if collisions:
            for spider in collisions.values():
                self.stats.score += self.settings.spider_points * len(spider)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.spider:
        # Destroy existing fireballs and create new fleet.
            self.fire.empty()
            self._create_fleet()
            self.settings.increase_speed()
        # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Create the fleet of spiders."""
        # Create a spider and keep adding spiders until there's no room left.
        # Spacing between spiders is one spider width and one spider height.
        spider = Spider(self)
        spider_width, spider_height = spider.rect.size
        
        current_x, current_y = spider_width, spider_height
        while current_y < (self.settings.screen_height - 3 * spider_height):

            while current_x < (self.settings.screen_width - 2 * spider_width):
                self._create_spider(current_x, current_y)
                current_x += 2 * spider_width
            # Finished a row; reset x value, and increment y value.
            current_x = spider_width
            current_y += 2 * spider_height       

    def _create_spider(self, x_position, y_position):
        """Create a spider and place it in the row."""
        new_spider = Spider(self)
        new_spider.x = x_position
        new_spider.y = y_position
        new_spider.rect.x = x_position
        new_spider.rect.y = y_position
        self.spider.add(new_spider)
    
    def _update_spider(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.spider.update()
        # Look for spider-killer collisions.
        if pygame.sprite.spritecollideany(self.killer, self.spider):
            self._killer_hit()
    
        # Look for spiders hitting the bottom of the screen.
        self._check_spider_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any spiders have reached an edge."""
        for spider in self.spider.sprites():
            if spider.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for spider in self.spider.sprites():
            spider.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _killer_hit(self):
        """Respond to the killer being hit by a spider."""
        if self.stats.killer_left > 0:
            # Decrement killer_left, and update scoreboard.
            self.stats.killer_left -= 1
            self.sb.prep_killer()
            # Get rid of any remaining fireballs and spiders.
            self.fire.empty()
            self.spider.empty()
            # Create a new fleet and center the killer.
            self._create_fleet()
            self.killer.center_killer()
            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_spider_bottom(self):
        """Check if any spider have reached the bottom of the screen."""
        for spider in self.spider.sprites():
            if spider.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the killer got hit.
                self._killer_hit()
                break

       

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.spider.draw(self.screen)
        self.killer.blitme()
        for fire in self.fire.sprites():
            fire.draw_fire()
        
        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            # Make the most recently drawn screen visible.
        # Draw the score information.
        self.sb.show_score()
        pygame.display.flip()
        

    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpiderKiller()
    ai.run_game()
    