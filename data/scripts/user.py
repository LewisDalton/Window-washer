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
        username_exists = False
        score_higher = False
        headers = ['username', 'points']
        rows = []

        with open(self.data, newline='') as f_read:
            reader = csv.DictReader(f_read)
            for row in reader:
                if row['username'] == self.username:
                    username_exists == True
                    if int(row['points']) < self.score.score:
                        row['points'] = self.score.score
                rows.append(row)

        with open(self.data, mode = 'w', newline = '') as f_write:
            writer = csv.DictWriter(f_write, fieldnames=headers, lineterminator='\n')
            if username_exists == True:
                writer.writerows(rows)
                print('username is here')
            else:
                with open(self.data, mode = 'a', newline = '') as f_append:
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