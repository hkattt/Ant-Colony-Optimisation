import pygame as pg
import numpy as np
import math

from settings import *

class Ant():
    def __init__(self, current_index, graph):
        self.current_index = current_index
        self.allowed = list(range(len(graph.nodes)))
        self.allowed.remove(current_index)
        self.gen_move_probabilities(graph)

    def move(self, graph):
        probabilities = self.gen_move_probabilities(graph)

    def gen_move_probabilities(self, graph):
        self.probabilities = np.zeros(len(graph.nodes))

        den = 0
        for potential_index in self.allowed:
            den += math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(graph.inv_distances[self.current_index, potential_index], BETA)

        for potential_index in self.allowed:
            num = math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(graph.inv_distances[self.current_index, potential_index], BETA)

            self.probabilities[potential_index] = num / den
        
    def draw_ant(self, screen, graph):
        x, y = graph.nodes[self.current_index].x, graph.nodes[self.current_index].y
        pg.draw.circle(screen, BLACK, (x, y), 8)

    def draw_potential(self, screen, graph):
        x, y = graph.nodes[self.current_index].x, graph.nodes[self.current_index].y
        for potential_index in self.allowed:
            potential_x, potential_y = graph.nodes[potential_index].x, graph.nodes[potential_index].y
            colour = np.interp(self.probabilities[potential_index], [0, 1], [22, 255])
            pg.gfxdraw.line(screen, x, y, potential_x, potential_y, (colour, colour, colour))

