from constants import *
from game.scripting.action import Action


class ControlFrogAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            frog.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            frog.move_right() 
        elif self._keyboard_service.is_key_down(UP):
            frog.move_up()
        elif self._keyboard_service.is_key_down(DOWN):
            frog.move_down()
        else: 
            frog.stop_moving()        