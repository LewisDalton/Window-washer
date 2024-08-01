import pygame
import os
import sys
import csv
from data.scripts.tools import Tool
from data.scripts.user import User

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

    def reset(self):
        self.score = 0

class Menu():
    def __init__(self, res_x, res_y, user) -> None:
        self.tool = Tool()

        self.menu_bg = pygame.image.load(os.path.join('assets', '.png_files' ,'menu_bg.jpg')).convert()
        self.menu_bg = pygame.transform.scale(self.menu_bg, (res_x, res_y))
        self.menu_bg_rect = self.menu_bg.get_rect()
        
        # Import user class 
        # ***Note*** i needed to pass user variable from game class to menu
        #  in this script so that the functions here render the same variable
        self.user = user

        # Text
        self.font = pygame.font.Font(os.path.join('assets', 'fonts', 'ARCADECLASSIC.TTF'), 64)
        self.text_box = self.font.render(self.user.username ,True, (255, 255, 255,))
        self.text_box_rect = pygame.Rect(200, 200, 195, 50)
        self.text_box_rect = self.tool.centre_screen(self.text_box_rect, res_x, res_y)
        self.text_box_rect.y -= 60

        # Buttons
        self.play_button = self.font.render('play' ,True, (255, 255, 255,))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect = self.tool.centre_screen(self.play_button_rect, res_x, res_y)
        pass

    def render_text_box(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.text_box_rect, 3)
        screen.blit(self.text_box, (self.text_box_rect.x +10, self.text_box_rect.y - 5))
        pass

    def update_text(self):
        self.text_box = self.font.render(self.user.username, True, (255, 255, 255,))

    def render_buttons(self, screen):
        screen.blit(self.play_button, self.play_button_rect)