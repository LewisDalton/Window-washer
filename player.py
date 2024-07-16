import pygame
import math
import os

#  Sprites
class Player:
    def __init__(self) -> None:
        super().__init__()
        self.velocity = 10
        self.pos_x = 0
        self.pos_y = 0
        self.sprites: list = []
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_left_hand.png')))
        self.sprites.append(pygame.image.load(os.path.join('assets', '.png_files' ,'moving_up_right_hand.png')))
        self.current_sprite: int = 0
        self.image = self.sprites[self.current_sprite]
        pass

    def controls(self):

    keys = pygame.key.get_pressed()

    move_x = 0
    move_y = 0

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
    self.pos_x += move_x * self.velocity
    self.pos_y += move_y * self.velocity
 
 