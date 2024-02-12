import matplotlib.pyplot as plt

from settings import DEBUG_MODE
from src.GameWindow import GameWindow

if __name__ == '__main__':
    window = GameWindow(DEBUG_MODE)
    window.run()

    plt.plot(window.player.agent.history)
    plt.show()
