import pygame as pg

from settings import *

class Edge():
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def draw(self, screen):
        pg.draw.line(screen, WHITE, (self.node1.x, self.node1.y), (self.node2.x, self.node2.y))

    def __eq__(self, other):
        if isinstance(other, Edge):
            con1 = self.node1 == other.node1 and self.node2 == other.node2
            con2 = self.node1 == other.node2 and self.node2 == other.node1
            return con1 or con2

    def __hash__(self):
        return self.node1.__hash__() + self.node2.__hash__()
