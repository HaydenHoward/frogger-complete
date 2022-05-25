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

# Font
FONT_FILE = "frogger/assets/fonts/HydrophiliaLiquid.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# Sound
# Text
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# Colors
BLACK = Color(0,0,0)
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

# Frog
FROG_GROUP = "frog"
FROG_WIDTH = 50
FROG_HEIGHT = 50
FROG_VELOCITY = 3
FROG_IMAGE = "8"