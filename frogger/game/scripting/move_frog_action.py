from turtle import pos
from torch import poisson
from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveFrogAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        body = frog.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - FROG_WIDTH):
            position = Point(SCREEN_WIDTH - FROG_WIDTH, position.get_y())

        if y < 0:
            position = Point(position.get_x(), 0)
        elif y > (SCREEN_HEIGHT - FROG_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - FROG_HEIGHT)
            
        body.set_position(position)