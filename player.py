import pygame
import math
import os

#  Sprites
class Player:
    def __init__(self, res_x, res_y) -> None:
        super().__init__()
        self.sprite = pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png'))
        self.sprite_size = [160, 160]
        self.sprite = pygame.transform.scale(self.sprite, self.sprite_size)
        self.player_pos = [0, 0]
        self.movement_y = False
        self.movement_x = [False, False]


        '''self.velocity = 10
        self.pos_x = 0
        self.pos_y = 0
        self.sprites: list = []
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_left_hand.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_right_hand.png')))
        self.current_sprite: int = 0
        self.image = self.sprites[self.current_sprite]'''

    def update_pos(self):
        self.player_pos[0] += self.movement_x[1] * 5
        self.player_pos[0] -= self.movement_x[0] * 5
 
    def render(self, screen):
        screen.blit(self.sprite, self.player_pos)