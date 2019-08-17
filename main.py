#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet
from pyglet.window import key

#Set resource location
pyglet.resource.path = ['./Pictures']
pyglet.resource.reindex()

#Create game window
pacman_window = pyglet.window.Window()

#entity list
entity_list = None

#Images
player_image = pyglet.resource.image('player.jpg')

@pacman_window.event
def on_key_press(symbol, modifiers):
    pass
    #if symbol == key.W:
        
    #if symbol == key.S:
        

@pacman_window.event
def on_draw():
    pacman_window.clear

if __name__ == '__main__':
    pyglet.app.run()
