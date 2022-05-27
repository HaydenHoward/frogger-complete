from matplotlib import animation
from constants import *
from game.scripting.action import Action

class DrawFrogAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        body = frog.get_body()

        if frog.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, RED)
            
        animation = frog.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)