import pygame as pg

from graph import Graph
from settings import *

pg.init()

running = True;

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.set_caption("Ant Colony Optimisation")

graph = Graph(5)
   
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
    screen.fill(BLACK)
    graph.draw(screen)
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