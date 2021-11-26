import pygame as pg
import pygame.gfxdraw
import numpy as np

from graph import Graph
from ant import Ant
from settings import *

pg.init()
pg.font.init()

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ant Colony Optimisation")

graph = Graph(5)
ant = Ant(0, graph)
   
def update():
    """ Updates the particle and button """
    pass

def events():
    """ Checks for and handle events """
    global running
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
               
def paint():
    """ Draws objects onto the screen """
    screen.fill(GREY)
    ant.draw_potential(screen, graph)
    graph.draw(screen)
    ant.draw_ant(screen, graph)
    pg.display.update()

def run():
    """ Main 'game' loop """
    while running:
        clock.tick(FPS)
        update()
        events()
        paint()        

if __name__ == "__main__":
    run()