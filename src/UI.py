import arcade
import arcade.gui
import matplotlib.pyplot as plt
from arcade.gui import UIBoxLayout
from settings import SPRITE_SIZE, MAP_COL, LEVEL1, LEVEL2, LEVEL3


class UI:
    def __init__(self, window):
        self.window = window
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.add_speed_buttons()
        self.add_game_state_buttons()

    def draw(self):
        self.ui_manager.draw()

    def add_speed_buttons(self):
        layout = UIBoxLayout(
            x=5,
            y=SPRITE_SIZE * 1.5,
            vertical=False
        )

        faster_speed_btn = self.create_btn("+", self.faster)
        slower_speed_btn = self.create_btn("-", self.slower)
        space = arcade.gui.UISpace(width=5)

        layout.add(faster_speed_btn)
        layout.add(space)
        layout.add(slower_speed_btn)

        self.ui_manager.add(
            layout
        )

    def add_game_state_buttons(self):
        width = SPRITE_SIZE * 1.5
        layout = UIBoxLayout(
            x=MAP_COL * SPRITE_SIZE - (width + SPRITE_SIZE / 2 * 1.5 * 3 + 20),
            y=SPRITE_SIZE * 1.5,
            vertical=False,
        )

        plot_btn = self.create_btn("Plot", self.plot, width=width)
        first_level_btn = self.create_btn("1", self.launch_first_level)
        second_level_btn = self.create_btn("2", self.launch_second_level)
        third_level_btn = self.create_btn("3", self.launch_third_level)

        space = arcade.gui.UISpace(width=5)

        layout.add(first_level_btn)
        layout.add(space)
        layout.add(second_level_btn)
        layout.add(space)
        layout.add(third_level_btn)
        layout.add(space)
        layout.add(plot_btn)

        self.ui_manager.add(
            layout
        )

    def create_btn(self, text, on_click, width=SPRITE_SIZE / 2 * 1.5, height=SPRITE_SIZE / 2 * 1.5):
        btn = arcade.gui.UIFlatButton(
            text=text,
            width=width,
            height=height
        )

        btn.on_click = on_click

        return btn

    def faster(self, _):
        self.window.rate *= 2
        self.window.set_update_rate(1 / self.window.rate)

    def slower(self, _):
        self.window.rate /= 2
        self.window.set_update_rate(1 / self.window.rate)

    def plot(self, _):
        plt.plot(self.window.player.agent.history)
        plt.show()

    def new_map(self, level):
        plt.plot(self.window.player.agent.history)
        plt.show()
        self.window.new_map(level)
        self.window.player.reset_position()
        self.window.player.agent.noise = 0
        self.window.player.agent.history = []
        self.window.win_count = 0
        self.window.loss_count = 0

    def launch_first_level(self, _):
        self.new_map(LEVEL1)

    def launch_second_level(self, _):
        self.new_map(LEVEL2)

    def launch_third_level(self, _):
        self.new_map(LEVEL3)
