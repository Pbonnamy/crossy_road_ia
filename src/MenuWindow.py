import arcade
from arcade.gui import UIFlatButton

from settings import MAP_COL, SPRITE_SIZE, MAP_ROW, DEBUG_MODE
from src.GameWindow import GameWindow


current_window = None # type: GameWindow

class MenuWindow(arcade.Window):
    def __init__(self):
        global current_window
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road Menu')
        self.v_box = arcade.gui.UIBoxLayout()
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        arcade.set_background_color(arcade.color.ANDROID_GREEN)
        self.v_box = arcade.gui.UIBoxLayout()

        play_button = PlayButton(text='Play')
        self.v_box.add(play_button.with_space_around(bottom=20))
        learn_button = LearnButton(text='Learn')
        self.v_box.add(learn_button)

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        current_window = self

    def on_draw(self):
        arcade.start_render()
        self.ui_manager.draw()


class PlayButton(UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        global current_window
        current_window.close()
        current_window = GameWindow(debug_mode=False, learning_mode=False)
        current_window.run()


class LearnButton(UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        global current_window
        current_window.close()
        current_window = GameWindow(debug_mode=DEBUG_MODE, learning_mode=True)
        current_window.run()
