import csv
from turtle import position
from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.image import Image
from game.casting.text import Text 
from game.casting.point import Point
from game.casting.frog import Frog
from game.casting.label import Label
from game.casting.stats import Stats
from game.casting.sound import Sound
from game.casting.tiles import Tiles
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.control_frog_action import ControlFrogAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_frog_action import CollideFrogAction
from game.scripting.collide_tiles_action import CollideTileAction
from game.scripting.draw_frog_action import DrawFrogAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_tiles_action import DrawTilesAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_frog_action import MoveFrogAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.time_change_scene_action import TimedChangeSceneAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    
    CHECK_OVER_ACTION = CheckOverAction()
    CONTROL_FROG_ACTION = ControlFrogAction(KEYBOARD_SERVICE)
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_FROG_ACTION = CollideFrogAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TILE_ACTION = CollideTileAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    DRAW_FROG_ACTION = DrawFrogAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_TILE_ACTION = DrawTilesAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_FROG_ACTION = MoveFrogAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)





    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    # Scene methods

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_tiles(cast)
        self._add_frog(cast)
        self._add_dialog(cast, ENTER_TO_START)
        

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_tiles(cast)
        self._add_frog(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))

        
    
    def _prepare_try_again(self, cast, script):
        self._add_frog(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_FROG_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)
    
    def _prepare_game_over(self, cast, script):
        self._add_frog(cast)
        self._add_tiles(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)
        
        
    # Casting methods
    def _add_frog(self, cast):
        cast.clear_actors(FROG_GROUP)
        x = CENTER_X - FROG_WIDTH / 2
        y = SCREEN_HEIGHT - FROG_HEIGHT
        position = Point(x, y)
        size = Point(FROG_WIDTH, FROG_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(FROG_IMAGES, FROG_RATE)
        frog = Frog(body, animation)
        cast.add_actor(FROG_GROUP, frog)

    def _add_tiles(self, cast):
        cast.clear_actors(TILE_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            
            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * TILE_WIDTH
                    y = FIELD_TOP + r * TILE_HEIGHT
                    color = column[0]
                    frames = int(column[1])

                    position = Point(x, y)
                    size = Point(TILE_WIDTH, TILE_HEIGHT)
                    velocity = Point(0, 0)
                    images = TILE_IMAGE[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, TILE_RATE, TILE_DELAY)

                    tile = Tiles(body, animation)
                    cast.add_actor(TILE_GROUP, tile)
    
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_LARGE, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        # position = Point(50, 300)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)
    
    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)
    
    

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
        script.add_action(OUTPUT, self.DRAW_TILE_ACTION)
        script.add_action(OUTPUT, self.DRAW_FROG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
        
   
    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_FROG_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_FROG_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TILE_ACTION)
        script.add_action(UPDATE, self.MOVE_FROG_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
       