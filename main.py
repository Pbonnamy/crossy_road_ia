import arcade

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE]

REWARD_ROAD = -1
REWARD_GOAL = 100
REWARD_WALL = -100

MAP_COL = 8
MAP_ROW = 12
MAP_SIZE = 50

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(MAP_COL*MAP_SIZE, MAP_ROW*MAP_SIZE, 'Crossy road')

    def on_draw(self):
        arcade.start_render()
        for row in range(MAP_ROW):
            if row % 2 == 0:
                arcade.draw_rectangle_filled(MAP_COL*MAP_SIZE/2, MAP_SIZE/2 + row*MAP_SIZE, MAP_COL*MAP_SIZE, MAP_SIZE, GRASS_COLOR_1)
            else:
                arcade.draw_rectangle_filled(MAP_COL*MAP_SIZE/2, MAP_SIZE/2 + row*MAP_SIZE, MAP_COL*MAP_SIZE, MAP_SIZE, GRASS_COLOR_2)

if __name__ == '__main__':
    window = GameWindow()
    arcade.run()