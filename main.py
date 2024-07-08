import pygame
import os
import math

# pygame setup
pygame.init()
screen_width = 828
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

# Sprites
player_idle = pygame.image.load(os.path.join('assets', '.png_files' ,'idle_character.png'))
player_idle = pygame.transform.scale(player_idle, (160, 160))

# velocity
player_velocity = 10

object_velocity = 10

# Co-ordinates
player_coordinates_x = 0
player_coordinates_y = 0

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_ESCAPE:
            running = False

        # Player controls
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

    # Applying the movement to the co-ordinates
    player_coordinates_x += move_x * player_velocity
    player_coordinates_y += move_y * player_velocity

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((84, 192, 214))

    # Drawing character images
    screen.blit(player_idle, (player_coordinates_x, player_coordinates_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()