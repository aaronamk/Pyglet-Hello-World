#Tell main where Pyglet is
import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/Pyglet/pyglet")

#Import statements
import pyglet, math
from enum import Enum

class Direction(Enum):
    North = [0,1, 270]
    East = [1,0, 0]
    South = [0,-1, 90]
    West = [-1,0, 180]

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2