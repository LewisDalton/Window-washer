import pygame
import math
import os

#  Sprites
class Player:
    def __init__(self, res_x, res_y) -> None:
        super().__init__()
        self.sprite_size = [160, 160]
        self.player_pos = [1000, 1000]
        self.movement_y = False
        self.movement_x = [False, False]

        self.sprites: list = []
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_left_hand.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_right_hand.png')))
        self.current_sprite: int = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.player_pos

    def update(self):
        self.player_pos[0] += self.movement_x[1] * 5
        self.player_pos[0] -= self.movement_x[0] * 5
        self.rect.topleft = self.player_pos
 
    def render(self, screen):
        screen.blit(self.image, self.player_pos)

    def update_anim(self):
        if self.movement_x[0] == True or self.movement_x[1] == True:
            self.current_sprite += 0.1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, self.sprite_size)