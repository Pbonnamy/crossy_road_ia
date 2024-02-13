import arcade
import arcade.gui
from arcade.gui import UIBoxLayout

from settings import SPRITE_SIZE, MAP_COL


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
            x=0,
            y=SPRITE_SIZE / 2 * 1.5 + 10,
            vertical=False
        )

        faster_speed_btn = self.create_btn("+", self.faster)

        padding = arcade.gui.UIPadding(
            padding=(5, 5, 5, 5),
            child=faster_speed_btn
        )

        slower_speed_btn = self.create_btn("-", self.slower)

        layout.add(padding)
        layout.add(slower_speed_btn)

        self.ui_manager.add(
            layout
        )

    def add_game_state_buttons(self):
        width = SPRITE_SIZE * 1.5
        layout = UIBoxLayout(
            x=MAP_COL * SPRITE_SIZE - width * 2 - 10,
            y=SPRITE_SIZE / 2 * 1.5 + 10,
            vertical=False
        )

        reset_btn = self.create_btn("Reset", self.reset, width=width)
        new_map_btn = self.create_btn("New", self.new_map, width=width)

        padding = arcade.gui.UIPadding(
            padding=(5, 5, 5, 5),
            child=reset_btn
        )

        layout.add(new_map_btn)
        layout.add(padding)

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

    def reset(self, _):
        self.window.reset()

    def new_map(self, _):
        self.window.new_map()
        self.window.player.reset_position()
        self.window.player.agent.history = []
        self.window.win_count = 0
        self.window.loss_count = 0
