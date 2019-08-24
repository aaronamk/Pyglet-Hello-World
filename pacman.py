#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet
from pyglet.window import Window, key

from entity import Entity
import util

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

    def update(self, dt):
        """This method should be called every frame.
        """
        super(Pacman, self).update(dt)

        if self.key_handler[key.W]:
            self.move_up()
        if self.key_handler[key.S]:
            self.move_down()
        if self.key_handler[key.D]:
            self.move_right()
        if self.key_handler[key.A]:
            self.move_left()
        
        self.check_bounds()

    def move_up(self):
        self.speed_x = 0
        self.speed_y = self.speed

    def move_down(self):
        self.speed_x = 0
        self.speed_y = -self.speed

    def move_right(self):
        self.speed_x = self.speed
        self.speed_y = 0

    def move_left(self):
        self.speed_x = -self.speed
        self.speed_y = 0

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0