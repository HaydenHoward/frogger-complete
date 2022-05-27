from raylib import PollInputEvents
from game.casting.actor import Actor
from game.casting.rectangle import Rectangle

class Tiles(Actor):
    "A row of rectangles that player can go on"

    def __init__(self, body, animation, debug = False):
        """construct a new tile
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
