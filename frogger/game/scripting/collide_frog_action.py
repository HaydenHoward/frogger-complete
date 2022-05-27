from constants import *
from game.casting.sound import Sound
from game.casting.point import Point
from game.scripting.action import Action


class CollideFrogAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        tiles = cast.get_first_actor(TILE_GROUP)
        
        frog_body = frog.get_body()
        frog_velocity = frog_body.get_velocity()
        frog_position = frog_body.get_position()
        frog_x = frog_position.get_x()
        frog_y = frog_position.get_y()

        tiles_body = tiles.get_body()
        tiles_position = tiles_body.get_position()
        tiles_x = tiles_position.get_x()
        tiles_y = tiles_position.get_y()


        if self._physics_service.has_collided(frog_body, tiles_body):
            # frog_position = Point(frog_x, frog_y)
            # frog.stop_moving()
            sound = Sound(BOUNCE_SOUND)
            # self._audio_service.play_sound(sound)    
            # frog_body.set_position(frog_position)