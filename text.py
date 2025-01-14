import pygame
import os
import sys
import csv

class Score():
    def __init__(self) -> None:
        self.score = 0
        self.font = pygame.font.Font(os.path.join('assets', 'fonts', 'ARCADECLASSIC.TTF'), 64)
        self.score_text = self.font.render(str(self.score) ,True, (255, 255, 255,))
        self.score_rect = self.score_text.get_rect()

    def update(self):
        self.score += 1
        self.score_text = self.font.render(str(self.score) ,True, (255, 255, 255,))

    def render(self, screen):
        screen.blit(self.score_text, (10, 10))

    def read(self):
        with open('highscores.csv', newline = '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print()

    def reset(self):
        self.score = 0

    def save(self):
        # Make this funciton save data to a csv file
        with open('highscores.csv', newline='') as f:
            pass


        '''if self.score > int(f_read.read()):
            f_write.write(str(self.score))
            f_write.close()'''
        pass

class Menu():
    def __init__(self, res_x, res_y) -> None:
        self.menu_bg = pygame.image.load(os.path.join('assets', '.png_files' ,'menu_bg.jpg')).convert()
        self.menu_bg = pygame.transform.scale(self.menu_bg, (res_x, res_y))
        self.menu_bg_rect = self.menu_bg.get_rect()
        
        # Text
        self.font = pygame.font.Font(os.path.join('assets', 'fonts', 'ARCADECLASSIC.TTF'), 64)
        self.start_text = self.font.render("PRESS SPACE TO START" ,True, (255, 255, 255,))
        self.start_rect = self.start_text.get_rect()
        self.centre_screen = (res_x / 2 - (self.start_rect[2] /2), res_y / 2 - (self.start_rect[3] / 2))
        pass

