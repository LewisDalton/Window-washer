import pygame
import os
import math
import sys
from player import Player
from rock import Rock

# pygame setup

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Window Washer')

        self.res_x = 824
        self.res_y = 1020
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))

        self.clock = pygame.time.Clock()

        self.player = Player(self.res_x, self.res_y)
        self.player.player_pos = [(self.res_x / 2) - (self.player.sprite_size[0] / 2), 
                                  (self.res_y / 3 * 2) - (self.player.sprite_size[1] / 2)]

        self.rock = Rock(self.res_x, self.res_y)
        self.rock.pos = [(self.res_x / 2) - (self.rock.sprite_size[0] / 2) , 0]

    def run(self):
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
                    if event.key == pygame.K_d:
                        self.player.movement_x[1] = True
                    if event.key == pygame.K_a:
                        self.player.movement_x[0] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.movement_x[1] = False
                    if event.key == pygame.K_a:
                        self.player.movement_x[0] = False

            # Rocks
            self.rock.fall()
            if self.rock.bottom():
                self.rock.pos[1] = 0
                self.rock.pos[0] = self.rock.lane_choice()

            # Collision
            if self.player.rect.colliderect(self.rock.rect):
                print('You Died')

            # Drawing
            self.screen.fill((70, 163, 250))

            self.player.update()
            self.player.update_anim()
            self.player.render(self.screen)
            
            self.rock.update()
            self.rock.update_anim()
            self.rock.render(self.screen)

            # the display to put your work on screen
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
Game().run()