from constants import *
from game.scripting.action import Action


class DrawItemAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        item = cast.get_first_actor(ITEM_GROUP)
        body = item.get_body()

        if item.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, RED)
            
        image = item.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)