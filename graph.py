import numpy as np
import random
import math

from node import Node
from settings import *

class Graph():
    def __init__(self, numberOfNodes):
        self.nodes = []
        self.init_nodes(numberOfNodes)
        self.gen_dist_map()
        self.inv_distances = 1 / self.distances
        self.gen_pheromone_trails()
    
    def init_nodes(self, numberOfNodes):
        for _ in range(numberOfNodes):
            node = Node(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
            self.nodes.append(node)
    
    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)

    def gen_dist_map(self):
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
