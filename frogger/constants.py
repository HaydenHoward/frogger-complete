from game.casting.color import Color

# General Game Constants

# Game
GAME_NAME = "Frogger"
FRAME_RATE = 60

# Screen
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# Field 
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# Font
FONT_FILE = "frogger/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 60

# Sound
BOUNCE_SOUND = "frogger/assets/sounds/boing.wav"
WELCOME_SOUND = "frogger/assets/sounds/start.wav"
OVER_SOUND = "frogger/assets/sounds/over.wav"

# Text
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# Colors
BLACK = Color(0, 0, 0)
GREY = Color (211, 211, 211)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

# Keys
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# Scenes
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# Levels 
# LEVEL_FILE = "frogger/assets/data/level-001.txt"
LEVEL_FILE = "frogger/assets/data/level-002.txt"

BASE_LEVELS = 5

# Scripting Constants

# Phases
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# Casting Constants

# Stats
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# Hud
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"

# Frog
FROG_GROUP = "frog"
FROG_WIDTH = 40
FROG_HEIGHT = 40
FROG_VELOCITY = 5
FROG_RATE = 6
FROG_IMAGES = [f"frogger/assets/images/{n:03}.png" for n in range(1, 4)]

# Tile
TILE_GROUP = "tile"
SAFE_TILE_GROUP ="safe_tile"
TILE_IMAGE = {
    # "b": [f"frogger/assets.images/{i:03}.png" for i in range(4, 6)],
    # "g": [f"frogger/assets.images/{i:03}.png" for i in range(6, 8)]
    "b" : ["frogger/assets/images/004.png"],
    "g" : ["frogger/assets/images/006.png"]
    }
TILE_HEIGHT = 40
TILE_WIDTH = 80
TILE_RATE = 4
TILE_DELAY = 0.5

# Dialog
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"


