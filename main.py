import matplotlib.pyplot as plt

from settings import DEBUG_MODE
from src.GameWindow import GameWindow

if __name__ == '__main__':
    window = GameWindow(DEBUG_MODE)
    window.run()

    window.player.agent.save_qtable()

    plt.plot(window.player.agent.history)
    plt.show()
