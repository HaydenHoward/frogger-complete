from constants import *
from game.casting.sound import Sound
from game.casting.point import Point
from game.scripting.action import Action



class CollideTileAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        tiles = cast.get_actors(TILE_GROUP)
        frog_body = frog.get_body()
        frog_velocity = frog_body.get_velocity()
        frog_position = frog_body.get_position()
        frog_x = frog_position.get_x()
        frog_y = frog_position.get_y()

        # stats = cast.get_first_actor(STATS_GROUP)
        
        for tile in tiles:
            tile_body = tile.get_body()
            tile_position = tile_body.get_position()
            tile_x = tile_position.get_x()
            tile_y = tile_position.get_y()
            
            if self._physics_service.has_collided(frog_body, tile_body):
                if frog_x < tile_x:
                    frog_position = Point(0, frog_position.get_y())
                elif frog_x > (SCREEN_WIDTH - TILE_WIDTH):
                    frog_position = Point((SCREEN_WIDTH - TILE_WIDTH), frog_position.get_y())

                if frog_y < tile_y:
                    frog_position = Point(frog_position.get_x(), 0)
                elif frog_y > (SCREEN_HEIGHT - TILE_HEIGHT):
                    frog_position = Point(frog_position.get_x(), (SCREEN_HEIGHT - TILE_HEIGHT))


                # frog.stop_moving()
                sound = Sound(BOUNCE_SOUND)
                # self._audio_service.play_sound(sound)
            frog_body.set_position(frog_position)
                # points = brick.get_points()
                # stats.add_points(points)
                # cast.remove_actor(BRICK_GROUP, brick)