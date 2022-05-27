from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.rectangle import Rectangle

class Frog(Actor):
    "A shape that will move as the player"

    def __init__(self, body, animation, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """The frog goes to the left."""
        velocity = Point(-FROG_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """The frog goes to the right."""
        velocity = Point(FROG_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def move_up(self):
        """The frog goes up."""
        velocity = Point(0, -FROG_VELOCITY)
        self._body.set_velocity(velocity)
    
    def move_down(self):
        """The frog goes down."""
        velocity = Point(0, FROG_VELOCITY)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the frog from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def no_move(self):
        """Stops the frog from moving"""
        # velocity = self._body.get_velocity()
        # vx = velocity.get_x()
        # vy = velocity.get_y()
        # velocity = Point(0, 0)
        # self.
        # FROG_VELOCITY = 0
        # position = self._body.get_position()
        # new_position = position.equals(position)
        # self._body.set_position(new_position)
        # self._body.set_velocity(velocity)