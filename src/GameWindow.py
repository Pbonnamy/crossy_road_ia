import arcade

from src.Player import Player
from src.Lane import Lane
from settings import SPRITE_SIZE, MAP_COL, MAP_ROW


class GameWindow(arcade.Window):
    def __init__(self, debug_mode):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road')
        self.player = Player(MAP_COL * SPRITE_SIZE / 2, SPRITE_SIZE / 2)
        self.lanes = []
        self.generate_map()
        self.debug_mode = debug_mode

    def generate_map(self):
        for i in range(0, MAP_ROW):
            lane_type = 'road'
            if i < 1 or i > MAP_ROW - 2:
                lane_type = 'grass'

            road = Lane(lane_type, i)
            self.lanes.append(road)

    def on_draw(self):
        arcade.start_render()

        for road in self.lanes:
            road.draw()

        self.player.draw()

        if self.debug_mode:
            self.debug_grid()

    def update(self, delta_time):
        for lane in self.lanes:
            lane.update()

    def on_key_press(self, key, modifiers):
        self.player.move(key)

    def debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
