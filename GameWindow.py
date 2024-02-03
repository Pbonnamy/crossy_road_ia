import arcade

from Road import Road

SPRITE_SCALING = 0.3
SPRITE_SIZE = int(128 * SPRITE_SCALING)

MAP_COL = 16
MAP_ROW = 16


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy road')
        self.roads = []
        for i in range(MAP_ROW):
            self.roads.append(Road(i, SPRITE_SIZE, MAP_COL * SPRITE_SIZE))

    def on_draw(self):
        arcade.start_render()
        for road in self.roads:
            road.draw()
