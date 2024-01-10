import arcade

WINDOW_WITH = 600
WINDOW_HEIGHT = 800


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WITH, WINDOW_HEIGHT, 'Crossy Road')

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)

if __name__ == '__main__':
    window = GameWindow()
    arcade.run()