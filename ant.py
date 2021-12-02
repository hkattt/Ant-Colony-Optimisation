import numpy as np
import math

from settings import *

class Ant():
    def __init__(self, current_index, graph):
        self.current_index = current_index
        self.allowed = list(range(len(graph.nodes)))
        self.allowed.remove(current_index)
        self.path = [current_index]
        self.gen_move_probabilities(graph)

    def run_iteration(self, graph):
        """ The ant creates a path in the given graph based on the pheromone trails
            and move probabilities. """
        node_indices = list(range(len(graph.nodes)))
        while len(self.allowed) != 0:
            # Selects the next node based on the move probabilites
            self.current_index = np.random.choice(node_indices, p=self.probabilities)
            self.allowed.remove(self.current_index)
            self.path.append(self.current_index)
            # Updates move probabilities
            self.gen_move_probabilities(graph)
        return graph.calc_path_distance(self.path)

    def gen_move_probabilities(self, graph):
        """ Generates the move probabilites of the ant for a given graph. 
            The probability array stores the probability of moving from the ant's
            current index to each respective index in the array."""
        self.probabilities = np.zeros(len(graph.nodes))

        den = 0
        for potential_index in self.allowed:
            den += math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(1 / graph.distances[self.current_index, potential_index], BETA)

        for potential_index in self.allowed:
            num = math.pow(graph.pheromone_trails[self.current_index, potential_index], ALPHA) \
                    * math.pow(1 / graph.distances[self.current_index, potential_index], BETA)

            # Updates the probability of moving from the ant's current index to the current potential index
            self.probabilities[potential_index] = num / den