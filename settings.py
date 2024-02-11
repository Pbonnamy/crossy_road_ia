SPRITE_SCALING = 0.4
SPRITE_SIZE = int(128 * SPRITE_SCALING)

CAR_WIDTH = int(256 * SPRITE_SCALING)

MAP_COL = 17  # Odd number only
MAP_ROW = 15

DEBUG_MODE = True

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE]

REWARD_WALL = -25
REWARD_CAR = -50
REWARD_DEFAULT = -1
REWARD_GOAL = 100

WALL = 'W'
CAR = 'C'
GOAL = 'G'
EMPTY = ' '

Z_KEY, S_KEY, Q_KEY, D_KEY = 122, 115, 113, 100
UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW = 65362, 65364, 65361, 65363
IDLE = -1

UP_KEYS = [Z_KEY, UP_ARROW]
DOWN_KEYS = [S_KEY, DOWN_ARROW]
LEFT_KEYS = [Q_KEY, LEFT_ARROW]
RIGHT_KEYS = [D_KEY, RIGHT_ARROW]
