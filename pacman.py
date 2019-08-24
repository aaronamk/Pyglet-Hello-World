#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet
from pyglet.window import Window, key

from entity import Entity
import util
from util import Direction

class Pacman(Entity):
    """Pacman Entity controlled by user.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, pyglet.resource.image('player.jpg'), **kwargs)

        self.image.width = 48
        self.image.height = 48
        util.center_image(self.image)
        
        self.speed = 100
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.desired_direction = Direction.West

    def update(self, dt):
        """This method should be called every frame.
        """
        super(Pacman, self).update(dt)

        if self.key_handler[key.W]:
            self.turn(Direction.North)
        if self.key_handler[key.S]:
            self.turn(Direction.South)
        if self.key_handler[key.D]:
            self.turn(Direction.East)
        if self.key_handler[key.A]:
            self.turn(Direction.West)
        
        self.check_bounds()

    def turn(self, d):
        self.speed_x = d.value[0] * self.speed
        self.speed_y = d.value[1] * self.speed

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0