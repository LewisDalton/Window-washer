import pygame
import os
import math
import sys

# pygame setup

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Window Washer')
        self.screen = pygame.display.set_mode((828, 1040))

        self.clock = pygame.time.Clock()

        self.dt = 0

        self.sprite = pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png'))
        self.sprite = pygame.transform.scale(self.sprite, (160, 160))
        self.player_pos = [0, 0]
        self.velocity = 10



    def run(self):
        while True:

            move_x = 0
            move_y = 0

            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    move_y -= 1
                if keys[pygame.K_s]:
                    move_y += 1
                if keys[pygame.K_a]:
                    move_x -= 1 
                if keys[pygame.K_d]:
                    move_x += 1 
        
            # Normalizing the movement for diagonals
            if move_y != 0 and move_x != 0:
                move_y = move_y / math.sqrt(2)
                move_x = move_x / math.sqrt(2)

            '''while move_x != 0 or move_y != 0:
            current_sprite = player_up_left
            
            current_sprite = player_up_right
            else:
                current_sprite = player_idle'''

            # Applying the movement to the co-ordinates
            self.player_pos[0] += move_x * self.velocity
            self.player_pos[1] += move_y * self.velocity


            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill((84, 192, 214))

            # Drawing character images
            self.screen.blit(self.sprite, self.player_pos)

            # flip() the display to put your work on screen
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

Game().run()