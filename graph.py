import numpy as np
import random
import math

from node import Node
from settings import *

class Graph():
    def __init__(self, numberOfNodes):
        self.nodes = []
        self.init_nodes(numberOfNodes)
        self.gen_distances()
        self.gen_pheromone_trails()
    
    def init_nodes(self, numberOfNodes):
        for _ in range(numberOfNodes):
            node = Node(random.randint(20, WIDTH - 20), random.randint(100, HEIGHT - 20))
            self.nodes.append(node)
    
    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)   

    def gen_distances(self):
        size = len(self.nodes)
        self.distances = np.zeros(shape=(size, size))
        for i in range(size):
            for j in range(size):
                node1, node2 = self.nodes[i], self.nodes[j]
                self.distances[i, j] = math.dist((node1.x, node1.y), (node2.x, node2.y))

    def gen_pheromone_trails(self):
        size = len(self.nodes)
        self.pheromone_trails = np.full((size, size), 1 / (size - 1))
        np.fill_diagonal(self.pheromone_trails, 0)

    def update_pheromone_trails(self, ants):
        size = len(self.nodes)
        pheromone_changes = np.zeros((size, size))

        for ant in ants:
            path_distance = self.calc_path_distance(ant.path)

            for i in range(len(ant.path)):
                node_index1, node_index2 = ant.path[i], ant.path[(i + 1) % len(ant.path)]
                pheromone_changes[node_index1, node_index2] = Q / path_distance

        self.pheromone_trails = (RHO * self.pheromone_trails) + pheromone_changes

    def calc_path_distance(self, path):
        path_distance = 0
        for i in range(len(path)):
            node_index1, node_index2 = path[i], path[(i + 1) % len(path)]
            node1, node2 = self.nodes[node_index1], self.nodes[node_index2]
            path_distance += math.dist((node1.x, node1.y), (node2.x, node2.y))
        return path_distance