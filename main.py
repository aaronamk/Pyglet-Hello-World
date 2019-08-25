#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet
from pyglet.window import key

from entity import Entity
from pacman import Pacman
from tiles import Bricks, Grass 

#Set resource location
pyglet.resource.path = ['./Pictures']
pyglet.resource.reindex()

#Create game window
pacman_window = pyglet.window.Window(800, 800)

#entity list
entity_list = []

#Images
entity_batch = pyglet.graphics.Batch()


def init():
    board = []
    board_file = open("board.txt", "r")
    for row in range(14):
        x_counter = 25
        for square in board_file.readline():
            if square == 'g':
                entity_list.append(Grass(x=x_counter, y=675-50*row, batch=entity_batch))
                #board[row].append()
            elif square == 'b':
                entity_list.append(Bricks(x=x_counter, y=675-50*row, batch=entity_batch))
            x_counter+=50
    
    #player
    player = Pacman(x=400, y=200, batch=entity_batch)
    pacman_window.push_handlers(player.key_handler)
    entity_list.append(player)

@pacman_window.event
def on_draw():
    pacman_window.clear()
    entity_batch.draw()

def update(dt):
    for entity in entity_list:
        entity.update(dt)

if __name__ == '__main__':
    init()

    pyglet.clock.schedule_interval(update, 1/120.0)

    pyglet.app.run()
