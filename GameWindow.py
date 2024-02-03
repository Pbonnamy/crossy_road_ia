import arcade

from Player import Player
from Road import Road

SPRITE_SCALING = 0.4
SPRITE_SIZE = int(128 * SPRITE_SCALING)

MAP_COL = 17
MAP_ROW = 16

DEBUG_MODE = True


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy road')
        self.player = Player(SPRITE_SCALING, SPRITE_SIZE, MAP_COL * SPRITE_SIZE / 2, SPRITE_SIZE / 2)
        self.roads = []
        self.generate_map()

    def generate_map(self):
        for i in range(0, MAP_ROW):
            road_type = 'road'
            if i < 2 or i > MAP_ROW - 2:
                road_type = 'grass'

            road = Road(road_type, i, SPRITE_SIZE, MAP_COL * SPRITE_SIZE)
            self.roads.append(road)

    def on_draw(self):
        arcade.start_render()

        for road in self.roads:
            road.draw()

        self.player.draw()

        if DEBUG_MODE:
            self.debug_grid()

    def debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)

    def on_key_press(self, key, modifiers):
        self.player.move(key, MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE)
