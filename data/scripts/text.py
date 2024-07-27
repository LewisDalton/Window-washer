import pygame
import os
import sys
import csv
from data.scripts.tools import Tool

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
        '''with open('highscores.csv', newline = '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['lewis'])
        '''
        pass

    def reset(self):
        self.score = 0

    def save(self):
        # Make this funciton save data to a csv file
        with open('highscores.csv', newline='') as f:
            writer = csv.DictWriter(f)

            pass


        '''if self.score > int(f_read.read()):
            f_write.write(str(self.score))
            f_write.close()'''
        pass

class Menu():
    def __init__(self, res_x, res_y) -> None:
        self.tool = Tool()

        self.menu_bg = pygame.image.load(os.path.join('assets', '.png_files' ,'menu_bg.jpg')).convert()
        self.menu_bg = pygame.transform.scale(self.menu_bg, (res_x, res_y))
        self.menu_bg_rect = self.menu_bg.get_rect()
        
        # Text
        self.font = pygame.font.Font(os.path.join('assets', 'fonts', 'ARCADECLASSIC.TTF'), 64)
        self.username = ''
        self.text_box = self.font.render(self.username ,True, (255, 255, 255,))
        self.text_box_rect = self.text_box.get_rect()
        self.text_box_rect = self.tool.centre_screen(self.text_box_rect, res_x, res_y)

        # Buttons
        self.play_button = self.font.render('play' ,True, (255, 255, 255,))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect = self.tool.centre_screen(self.play_button_rect, res_x, res_y)
        pass

    def render_text_box(self, screen):
        screen.blit(self.text_box, (0, 0))

    def update_text(self):
        self.text_box = self.font.render(self.username ,True, (255, 255, 255,))

    def render_buttons(self, screen):
        screen.blit(self.play_button, self.play_button_rect)