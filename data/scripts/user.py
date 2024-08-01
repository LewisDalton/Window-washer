import pygame
import csv
import os

class User():
    def __init__(self) -> None:
        self.username = ''
        self.data = os.path.join('data', 'highscores.csv')
    
    def create_user():
        
        pass

    def save(self):
        # Make this funciton save data to a csv file
        pass


        '''if self.score > int(f_read.read()):
            f_write.write(str(self.score))
            f_write.close()'''
        pass

    def read(self):
        '''with open('highscores.csv', newline = '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['lewis'])
        '''
        pass