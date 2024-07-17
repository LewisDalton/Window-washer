import pygame
import os
import math
import sys
from player import Player

# pygame setup

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Window Washer')

        self.res_x = 824
        self.res_y = 1020
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.player = Player(self.res_x, self.res_y)
        self.player.player_pos = [(self.res_x / 2) - (self.player.sprite_size[0] / 2), 
                                  (self.res_y / 3 * 2) - (self.player.sprite_size[1] / 2)]
        
    def run(self):
        while True:
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill((84, 192, 214))
           
            self.player.update_pos()
            self.player.render(self.screen)

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

            # flip() the display to put your work on screen
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

Game().run()