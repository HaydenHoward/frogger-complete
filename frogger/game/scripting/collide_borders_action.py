from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        body = frog.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            frog.stop_moving()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - FROG_WIDTH):
            frog.stop_moving()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            frog.stop_moving()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - FROG_WIDTH):
            frog.stop_moving()
            self._audio_service.play_sound(bounce_sound)