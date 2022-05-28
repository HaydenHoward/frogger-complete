from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideItemAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        item = cast.get_first_actor(ITEM_GROUP)
        frog = cast.get_first_actor(FROG_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        over_sound = Sound(OVER_SOUND)
        
        item_body = item.get_body()
        frog_body = frog.get_body()

        if self._physics_service.has_collided(frog_body, item_body):
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            points = item.get_points()
            stats.add_points(points)
            callback.on_next(GAME_OVER)
            self._audio_service.play_sound(over_sound)
            # cast.clear_actors(ITEM_GROUP)
            # cast.remove_actor(ITEM_GROUP, item)