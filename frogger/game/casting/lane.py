from game.casting.actor import Actor
from game.casting.rectangle import Rectangle

class Lane(Rectangle):
    "A row of rectangles that player can go on"

    def __init__(self, body, size):
        """construct a new tile
        
        Args:
            size()
        """