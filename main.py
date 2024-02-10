import arcade
from matplotlib import pyplot as plt

from settings import DEBUG_MODE
from src.GameWindow import GameWindow
from src.Player import Player
from src.QlearningAgent import QLearningAgent

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'

AGENT_FILE = 'agent.qtable'

REWARD_ROAD = -1
REWARD_GOAL = 100
REWARD_WALL = -100

if __name__ == '__main__':
    player = Player()
    agent = QLearningAgent(player)
    agent.load(AGENT_FILE)
    window = GameWindow(DEBUG_MODE, agent, player)
    window.run()

    agent.save(AGENT_FILE)
    print(agent.history)
    plt.plot(agent.history)
    plt.show()
