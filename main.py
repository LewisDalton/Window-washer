import pygame
import os
import math
import sys
from player import Player
from rock import Rock
from text import Score, Menu

# pygame setup

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Window Washer')

        self.res_x = 824
        self.res_y = 1020
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        self.bg = pygame.image.load(os.path.join('assets', '.png_files' ,'background.png')).convert()
        self.tiles = math.ceil(self.res_y / self.bg.get_height()) + 1
        self.scroll = 0

        self.clock = pygame.time.Clock()

        # Player
        self.player = Player(self.res_x, self.res_y)
        self.player.player_pos = [self.player.lanes[self.player.lane_index], 
                                  (self.res_y / 3 * 2) - (self.player.sprite_size[1] / 2)]

        # Rock
        self.rock = Rock(self.res_x, self.res_y)
        self.rock.pos = [(self.res_x / 2) - (self.rock.sprite_size[0] / 2) , 0]

        # Text
        self.score = Score()
        self.menu = Menu(self.res_x, self.res_y)

    def menu_loop(self):
        while True:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.quit()
                    if event.key == pygame.K_SPACE:
                        self.run()
            
            self.screen.blit(self.menu.menu_bg, self.menu.menu_bg_rect)
            self.screen.blit(self.menu.start_text, self.menu.centre_screen)
            pygame.display.update()
        pass

    def run(self):
        while True:
            
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:
                        self.menu_loop()
                    if event.key == pygame.K_d:
                        self.player.move_right()
                    if event.key == pygame.K_a:
                        self.player.move_left()
                
            # Rocks
            self.rock.fall()
            if self.rock.bottom():
                self.rock.pos[1] = 0 - self.rock.sprite_size[1]
                self.rock.pos[0] = self.rock.lane_choice()

            # Collision
            if self.player.rect.colliderect(self.rock.rect):
                pygame.quit()

            # Scrolling background
            self.scroll += 3

            for i in range(0, self.tiles):
                self.screen.blit(self.bg, (0, -i * self.bg.get_height() + self.scroll))

            if self.scroll > self.bg.get_height():
                self.scroll = 0
            
            # Updating positions
            self.player.update()
            self.player.update_anim()
            self.rock.update()
            self.rock.update_anim()
            self.score.update()

            # Rendering
            self.score.render(self.screen)
            self.player.render(self.screen)
            self.rock.render(self.screen)

            # the display to put your work on screen
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

Game().menu_loop()