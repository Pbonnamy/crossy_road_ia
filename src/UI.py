import arcade
import arcade.gui
from arcade.gui import UIBoxLayout

from settings import SPRITE_SIZE


class UI:
    def __init__(self, window):
        self.window = window
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.setup()

    def draw(self):
        self.ui_manager.draw()

    def setup(self):
        self.ui_manager.enable()

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

    def create_btn(self, text, on_click):
        btn = arcade.gui.UIFlatButton(
            text=text,
            width=SPRITE_SIZE / 2 * 1.5,
            height=SPRITE_SIZE / 2 * 1.5,
        )

        btn.on_click = on_click

        return btn

    def faster(self, _):
        self.window.rate *= 2
        self.window.set_update_rate(1 / self.window.rate)

    def slower(self, _):
        self.window.rate /= 2
        self.window.set_update_rate(1 / self.window.rate)
