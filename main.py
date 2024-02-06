import arcade

from settings import DEBUG_MODE
from src.GameWindow import GameWindow
from src.Radar import Radar, Agent

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE]

REWARD_ROAD = -1
REWARD_GOAL = 100
REWARD_WALL = -100

AGENT_FILE = 'agent.qtable'

if __name__ == '__main__':
    window = GameWindow(DEBUG_MODE)
    arcade.run()
