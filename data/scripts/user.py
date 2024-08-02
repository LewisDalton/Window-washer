import pygame
import csv
import os

class User():
    def __init__(self, score) -> None:
        self.score = score

        self.username = ''
        self.data = os.path.join('data', 'highscores.csv')
    
    def save(self):
        # Make this funciton save data to a csv file
        
        with open(self.data, mode = 'w', newline = '') as f:
           headers = ['username', 'points']
           writer = csv.DictWriter(f, fieldnames=headers)
           
           writer.writeheader()
           writer.writerow({headers[0]: self.username, headers[1]: self.score.score})




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