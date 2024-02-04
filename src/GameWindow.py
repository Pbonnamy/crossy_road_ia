import arcade

from src.Grass import Grass
from src.Player import Player
from settings import SPRITE_SIZE, MAP_COL, MAP_ROW
from src.Road import Road


class GameWindow(arcade.Window):
    def __init__(self, debug_mode):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road')
        self.player = Player(MAP_COL * SPRITE_SIZE / 2, SPRITE_SIZE / 2)
        self.lanes = []
        self.generate_map()
        self.debug_mode = debug_mode

    def generate_map(self):
        for i in range(0, MAP_ROW):
            if i < 1 or i > MAP_ROW - 2:
                lane = Grass(i)
            else:
                lane = Road(i)

            self.lanes.append(lane)

    def on_draw(self):
        arcade.start_render()

        for road in self.lanes:
            road.draw()

        self.player.draw()

        if self.debug_mode:
            self.debug_grid()

    def on_update(self, delta_time):
        for lane in self.lanes:
            lane.update()

    def on_key_press(self, key, modifiers):
        self.player.move(key)

    def debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
