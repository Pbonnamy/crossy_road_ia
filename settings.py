# Sprite sizes
SPRITE_SCALING = 0.4
SPRITE_SIZE = int(128 * SPRITE_SCALING)
CAR_WIDTH = int(256 * SPRITE_SCALING)

# Allow debug information
DEBUG_MODE = False

# Possible actions
ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE]

# Lane types
SAFE_ZONE_START = 'SZS'
SAFE_ZONE_END = 'SZE'
ROAD_RIGHT = 'RR'
ROAD_LEFT = 'RL'
GRASS = 'G'

# Map dimensions
MAP_COL = 17  # Odd number only
MAP_ROW = 15

# Levels
LEVEL1 = [
    SAFE_ZONE_START,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    GRASS,
    SAFE_ZONE_END
]

LEVEL2 = [
    SAFE_ZONE_START,
    GRASS,
    GRASS,
    GRASS,
    ROAD_RIGHT,
    GRASS,
    GRASS,
    ROAD_LEFT,
    GRASS,
    GRASS,
    GRASS,
    ROAD_RIGHT,
    GRASS,
    GRASS,
    SAFE_ZONE_END
]

LEVEL3 = [
    SAFE_ZONE_START,
    GRASS,
    ROAD_RIGHT,
    GRASS,
    ROAD_RIGHT,
    GRASS,
    GRASS,
    ROAD_LEFT,
    GRASS,
    ROAD_LEFT,
    GRASS,
    ROAD_RIGHT,
    GRASS,
    GRASS,
    SAFE_ZONE_END
]

# Q-Learning settings
LEARNING_RATE = 0.7
DISCOUNT_FACTOR = 0.7

# Rewards
REWARD_WALL = -(MAP_ROW * MAP_COL / 2)
REWARD_CAR = -(MAP_ROW * MAP_COL)
REWARD_DEFAULT = -1
REWARD_GOAL = MAP_ROW * MAP_COL

# Speed of the game
BASE_WINDOW_RATE = 60

# Lane settings
NUMBER_OF_OBSTACLES = [2, 3, 4]
CAR_SPEEDS = [2, 2.5, 3]
CAR_SPACINGS = [4, 5]

# State symbols
WALL = 'W'
CAR_RIGHT = 'CR'
CAR_LEFT = 'CL'
GOAL = 'G'
EMPTY = ' '

# Q-Table filename
QTABLE_FILE = 'agent.qtable'

# Key bindings
Z_KEY, S_KEY, Q_KEY, D_KEY = 122, 115, 113, 100
UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW = 65362, 65364, 65361, 65363
IDLE = -1
NOISE_KEY = 110

UP_KEYS = [Z_KEY, UP_ARROW]
DOWN_KEYS = [S_KEY, DOWN_ARROW]
LEFT_KEYS = [Q_KEY, LEFT_ARROW]
RIGHT_KEYS = [D_KEY, RIGHT_ARROW]
