import pygame
import os
import time

class Rock:
    def __init__(self, res_x, res_y) -> None:
        self.sprite_size = [160, 160]
        self.pos = [0,0]
        self.move = False

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

    def render(self, screen):
        screen.blit(self.image, self.pos) 

    def fall(self):
        print("Rock fell")

        while self.move == True:
            self.pos[1] += int(self.move) * 5