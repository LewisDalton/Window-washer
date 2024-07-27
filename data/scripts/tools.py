import pygame

class Tool():
    def __init__(self) -> None:
        pass

    def centre_screen(self, rect, res_x, res_y):
        # Make sure that the input is a rect pygame object
        # When importing an image use the x.get.rect() to get this and store it in a variable
        # use tool.centre_screen()
        # 1st argument is the rect you want to centre
        # the 2nd and 3rd arguments are the resolution width and height for the function

        pos_x = res_x / 2 - (rect.width / 2)
        pos_y = res_y / 2 - (rect.height / 2)

        return [pos_x, pos_y]