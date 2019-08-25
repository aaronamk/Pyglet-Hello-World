#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet
from pyglet.window import Window

from entity import Entity
import util

class Grass(Entity):
    """No go zones
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pyglet.resource.image('grass.jpg'), **kwargs)

        self.image.width = 50
        self.image.height = 50
        util.center_image(self.image)

class Bricks(Entity):
    """Paths to walk on.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pyglet.resource.image('bricks.jpg'), **kwargs)

        self.image.width = 50
        self.image.height = 50
        util.center_image(self.image)