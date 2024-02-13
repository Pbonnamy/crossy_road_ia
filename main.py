import arcade
import matplotlib.pyplot as plt

from settings import DEBUG_MODE
from src.GameWindow import GameWindow
from src.MenuWindow import MenuWindow

if __name__ == '__main__':
    menu = MenuWindow()
    menu.run()

