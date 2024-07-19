import pygame
import os

class Score():
    def __init__(self) -> None:
        self.score = 0
        self.font = pygame.font.Font(os.path.join('assets', 'fonts', 'Roboto-Medium.ttf'), 32)
        self.score_text = self.font.render(str(self.score) ,True, (255, 255, 255,))
        self.score_rect = self.score_text.get_rect()

    def update(self):
        self.score += 1
        self.score_text = self.font.render(str(self.score) ,True, (255, 255, 255,))

    def render(self, screen):
        screen.blit(self.score_text, self.score_rect)
