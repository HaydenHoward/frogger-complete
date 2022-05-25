
from constants import *
from game.casting.text import Text 
from game.casting.point import Point
from game.casting.frog import Frog
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.time_change_scene_action import TimedChangeSceneAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)




    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        # elif scene == NEXT_LEVEL:
        #     self._prepare_next_level(cast, script)
        # elif scene == TRY_AGAIN:
        #     self._prepare_try_again(cast, script)
        # elif scene == IN_PLAY:
        #     self._prepare_in_play(cast, script)
        # elif scene == GAME_OVER:    
        #     self._prepare_game_over(cast, script)

    # Scene methods

    def _prepare_new_game(self, cast, script):
        self._add_frog(cast)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    # Casting methods
    def _add_frog(self, cast):
        cast.clear_actors(FROG_GROUP)
        x = CENTER_X - FROG_WIDTH / 2
        y = SCREEN_HEIGHT - FROG_HEIGHT
        position = Point(x, y)
        size = Point(FROG_WIDTH, FROG_HEIGHT)
        velocity = Point(0, 0)
        image = Text.set_value(self, FROG_IMAGE)
        frog = Frog(image, position, size, velocity)
        cast.add_actor(FROG_GROUP, frog)

    # Scripting methods

    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
   
    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
       