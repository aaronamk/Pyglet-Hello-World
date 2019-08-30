#Import statements
import pyglet
from pyglet.window import Window

from entity import Entity
import util

class Board():
    """The map
    """
    def __init__(self, file, entity_list, batch):
        board_file = open(file, "r")
        for row in range(14):
            x_counter = 25
            for square in board_file.readline():
                if square == 'g':
                    entity_list.append(Grass(x=x_counter, y=675-50*row, batch=batch))
                    x_counter+=50
                elif square == 'b':
                    entity_list.append(Bricks(x=x_counter, y=675-50*row, batch=batch))
                    x_counter+=50

    def get_tile_type(self, ):
        pass

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