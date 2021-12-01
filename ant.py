import pygame as pg
import pygame.gfxdraw
import numpy as np
import math

from settings import *

class Ant():
    def __init__(self, current_index, graph):
        self.current_index = current_index
        self.allowed = list(range(len(graph.nodes)))
        self.allowed.remove(current_index)
        self.path = [current_index]
        self.probabilities = self.gen_move_probabilities(graph)

    def run_iteration(self, graph):
        node_indices = list(range(len(graph.nodes)))
        while len(self.allowed) != 0:
            self.current_index = np.random.choice(node_indices, p=self.probabilities)
            self.allowed.remove(self.current_index)
            self.path.append(self.current_index)
            self.gen_move_probabilities(graph)
        return graph.calc_path_distance(self.path)

    def gen_move_probabilities(self, graph):
        self.probabilities = np.zeros(len(graph.nodes))

        den = 0
        for potential_index in self.allowed:
            den += math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(1 / graph.distances[self.current_index, potential_index], BETA)

        for potential_index in self.allowed:
            num = math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(1 / graph.distances[self.current_index, potential_index], BETA)

            self.probabilities[potential_index] = num / den
        return self.probabilities