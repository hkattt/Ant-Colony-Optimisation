import pygame as pg
import random

from node import Node
from edge import Edge
from settings import *

class Graph():
    def __init__(self, numberOfNodes):
        self.nodes = set()
        self.edges = set()
        self.init_nodes(numberOfNodes)
        self.init_edges()
        
        
    def init_nodes(self, numberOfNodes):
        for _ in range(numberOfNodes):
            node = Node(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
            self.nodes.add(node)
    
    def init_edges(self):
        for node in self.nodes:
            for connectedNode in self.nodes:
                if node == connectedNode:
                    continue
                edge = Edge(node, connectedNode)
                self.edges.add(edge)

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
        for edge in self.edges:
            edge.draw(screen)

