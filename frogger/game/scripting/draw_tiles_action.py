from constants import *
from game.scripting.action import Action


class DrawTilesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        tiles = cast.get_actors(TILE_GROUP)
        tiles_2 = cast.get_actors(SAFE_TILE_GROUP)
        
        for tile in tiles:
            body = tile.get_body()

            if tile.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, RED)
                
            animation = tile.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
        
        for tile in tiles_2:
            body = tile.get_body()

            if tile.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, RED)
                
            animation = tile.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)