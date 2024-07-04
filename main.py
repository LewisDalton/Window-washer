import pygame

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_ESCAPE:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()