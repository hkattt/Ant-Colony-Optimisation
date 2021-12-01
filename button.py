import pygame as pg

from settings import *

class Button():
    def __init__(self, colour, x, y, width, height, text, text_size):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
    
    def draw(self, screen):
        """ Draws the button onto the screen """
        pg.draw.rect(screen, self.colour, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pg.draw.rect(screen, GREY, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            write(screen, self.text, self.colour, self.text_size, int(self.x + self.width / 2), int(self.y + self.height / 2))

    def update(self):
        """ Updates the colour of the button based on the position of the mouse"""
        dX, dY = pg.mouse.get_pos()
        if (self.mouse_over((dX, dY))):
            self.colour = GREEN
        else:
            self.colour = WHITE    

    def mouse_over(self, position):
        """ Checks if the mouse is over the button """
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False

def write(screen, text, colour, size, x, y):
    """ Draws text onto the screen """
    # setting the font size and type
    font = pg.font.Font("freesansbold.ttf", size)
    text_surface = font.render(text, True, colour)
    # creating the font rect
    text_rect = text_surface.get_rect()
    text_rect.center = x, y

    screen.blit(text_surface, text_rect)