import pygame
import math
import os

#  Sprites
class Player:
    def __init__(self, res_x, res_y) -> None:
        super().__init__()
        self.sprite_size = [160, 160]
        self.movement_y = False
        self.movement_x = [False, False]
        self.lanes = [res_x / 6 - (self.sprite_size[0] / 2),
                res_x / 2 - (self.sprite_size[0] / 2),
                    (res_x - (res_x / 6)) - (self.sprite_size[0] / 2)]
        self.lane_index = 1
        self.player_pos = [self.lanes[self.lane_index], 1000]

        # Sprites
        self.sprites: list = []
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png')).convert_alpha())
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_left_hand.png')).convert_alpha())
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_right_hand.png')).convert_alpha())
        self.current_sprite: int = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, self.sprite_size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.player_pos

    def update(self):
        self.rect.topleft = self.player_pos
 
    def render(self, screen):
        screen.blit(self.image, self.player_pos)

    def update_anim(self):
        self.current_sprite += 0.08

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, self.sprite_size)
        
    def move_right(self):
        if self.lane_index < len(self.lanes) - 1:
            self.lane_index += 1
            self.player_pos[0] = self.lanes[self.lane_index]
        
    def move_left(self):
        if self.lane_index > 0:
            self.lane_index -= 1
            self.player_pos[0] = self.lanes[self.lane_index]