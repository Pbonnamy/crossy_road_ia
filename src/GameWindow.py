import arcade
import random

from src.Grass import Grass
from src.Player import Player
from settings import SPRITE_SIZE, MAP_COL, MAP_ROW
from src.Road import Road
from src.SafeZone import SafeZone


class GameWindow(arcade.Window):
    def __init__(self, debug_mode):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road')
        self.player = Player()
        self.lanes = []
        self.generate_map()
        self.debug_mode = debug_mode

    def generate_map(self):
        for i in range(0, MAP_ROW):
            if i == 0 or i == MAP_ROW - 1:
                lane = SafeZone(i)
            else:
                rand = random.randint(0, 10)
                if rand < 3:
                    lane = Grass(i)
                else:
                    lane = Road(i)

            self.lanes.append(lane)

    def on_draw(self):
        arcade.start_render()

        for lane in self.lanes:
            lane.draw()

        self.player.draw()

        if self.debug_mode:
            self.draw_debug_grid()

    def on_update(self, delta_time):
        for lane in self.lanes:
            lane.update()
            player_row = self.player.current_row()
            if lane.index == player_row and isinstance(lane, Road):
                lane.check_collision(self.player)

    def on_key_press(self, key, modifiers):
        self.player.move(key)

    def draw_debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
