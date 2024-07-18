import pygame
import os
import time
import random

class Rock:
    def __init__(self, res_x, res_y) -> None:
        self.sprite_size = [160, 160]
        self.pos = [0,0]
        self.res_y = res_y
        self.res_x = res_x
        self.lanes = [res_x / 6 - (self.sprite_size[0] / 2),
                        res_x / 2 - (self.sprite_size[0] / 2),
                         (res_x - (res_x / 6)) - (self.sprite_size[0] / 2)]

        self.sprites: list = []
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'rock_0.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'rock_1.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'rock_2.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'rock_3.png')))
        self.current_sprite: int = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        pass

    def update(self):
        self.rect.topleft = self.pos

    def render(self, screen):
        screen.blit(self.image, self.pos) 

    def fall(self):
        self.pos[1] += 8

    def bottom(self):
        return self.pos[1] > self.res_y
    
    def lane_choice(self):
        return random.choice(self.lanes)
    
    def update_anim(self):
        self.current_sprite += 0.05

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, self.sprite_size)