import arcade

from settings import DEBUG_MODE
from src.GameWindow import GameWindow

if __name__ == '__main__':
    window = GameWindow(DEBUG_MODE)
    arcade.run()
