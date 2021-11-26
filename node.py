import pygame as pg

from settings import *

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pg.draw.circle(screen, WHITE, (self.x, self.y), 10)

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.x == other.x and self.y == other.y)
    
    def __hash__(self):
        return self.x + self.y
