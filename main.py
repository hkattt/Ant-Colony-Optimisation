import pygame as pg
import random
import time

from graph import Graph
from ant import *
from line import aaline
from button import *

def init_ants(number_of_ants):
    ants = []
    for _ in range(NUMBER_OF_NODES):
        node_index = random.randint(0, NUMBER_OF_NODES - 1)
        ant = Ant(node_index, graph)
        ants.append(ant)
    return ants

def update():
    """ Updates the particle and button """
    start_button.update()
    gen_button.update()

def events():
    """ Checks for and handle events """
    global graph, running, simulating
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
            dX, dY = pg.mouse.get_pos()
            if start_button.mouse_over((dX, dY)):
                if start_button.text == "Start":
                    simulating = True
                    start_button.text = "Stop"
                else:
                    simulating = False
                    start_button.text = "Start"

            elif gen_button.mouse_over((dX, dY)) and not simulating:
                reset()
               
def paint():
    """ Draws objects onto the screen """
    global best_path
    screen.fill(GREY)
    draw_path(screen, graph, best_path)
    graph.draw(screen)
    start_button.draw(screen)
    gen_button.draw(screen)
    pg.display.update()

def run():
    """ Main 'game' loop """
    while running:
        clock.tick(FPS)
        if simulating:
            run_iteration()
        update()
        events()
        paint()
        
def run_iteration():
    global ants, best_path, best_path_distance, simulating
    for ant in ants:
        if simulating == False:
            return
        distance = ant.run_iteration(graph)
        if distance < best_path_distance:
            best_path_distance = distance
            best_path = ant.path
        update()
        events()
        paint()
        time.sleep(0.01)
    graph.update_pheromone_trails(ants)
    ants = init_ants(NUMBER_OF_ANTS)

def draw_path(screen, graph, path):
    for i in range(len(path)):
        node_index1, node_index2 = path[i], path[(i + 1) % len(path)]
        node1 = graph.nodes[node_index1]
        node2 = graph.nodes[node_index2]
        aaline(screen, WHITE, (node1.x, node1.y), (node2.x, node2.y))

def reset():
    global graph, best_path, best_path_distance, graph, ants, simulating
    best_path = []
    best_path_distance = float('inf')
    graph = Graph(NUMBER_OF_NODES)
    ants = init_ants(NUMBER_OF_ANTS)
    simulating = False

pg.init()
pg.font.init()

running, simulating = True, False

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ant Colony Optimisation")

best_path = []
best_path_distance = float('inf')
graph = Graph(NUMBER_OF_NODES)
ants = init_ants(NUMBER_OF_ANTS)

start_button = Button(WHITE, 25, 25, 125, 50, "Start", 20)
gen_button = Button(WHITE, 165, 25, 125, 50, "Generate", 20)

if __name__ == "__main__":
    run()