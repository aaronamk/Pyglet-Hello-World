#Import statements
import pyglet

import util

class Entity(pyglet.sprite.Sprite):
    """A sprite with physical properties such as speed. Adapted from Pyglet example
    """

    def __init__(self, *args, **kwargs):
        super(Entity, self).__init__(*args, **kwargs)

        # Speed
        self.speed_x, self.speed_y = 0.0, 0.0

        # Flag to remove this object from the game_object list
        self.dead = False

        # List of new objects to go in the entity5 list
        self.new_objects = []

        # Tell the game handler about any event handlers
        # Only applies to things with keyboard/mouse input
        self.event_handlers = []

    def update(self, dt):
        """This method should be called every frame.
        """

        # Update position according to speed and time
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        # Wrap around the screen if necessary
        self.check_bounds()

    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior.
        """
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 800 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object):
        """Determine if this object collides with another.
        """

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.image.width * 0.5 * self.scale \
                             + other_object.image.width * 0.5 * other_object.scale

        # Get distance using position tuples
        actual_distance = util.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)