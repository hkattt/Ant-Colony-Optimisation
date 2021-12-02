import pygame as pg

from settings import *

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        """ Draws the node onto the screen. """
        pg.draw.circle(screen, WHITE, (self.x, self.y), 10)
