import arcade
from settings import DEBUG_MODE
from src.GameWindow import GameWindow

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'

REWARD_ROAD = -1
REWARD_GOAL = 100
REWARD_WALL = -100

if __name__ == '__main__':
    window = GameWindow(DEBUG_MODE)
    arcade.run()
