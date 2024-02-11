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
        self.lanes = []
        self.generate_map()
        self.player = Player(self.lanes)
        self.debug_mode = debug_mode
        self.win_count = 0
        self.loss_count = 0

    def generate_map(self):
        for i in range(0, MAP_ROW):
            if i == 0 or i == MAP_ROW - 1:
                lane = SafeZone(i, "start" if i == 0 else "end")
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

        self.draw_counters()

    def draw_counters(self):
        arcade.draw_text('Wins: ' + str(self.win_count), 5, MAP_ROW * SPRITE_SIZE - 20, arcade.color.BLACK, 14, bold=True)
        arcade.draw_text('Losses: ' + str(self.loss_count), 5, MAP_ROW * SPRITE_SIZE - 40, arcade.color.BLACK, 14, bold=True)

    def on_update(self, delta_time):
        player_row = self.player.current_row()

        if player_row == MAP_ROW - 1:
            self.win_count += 1
            self.player.reset_position()

        for lane in self.lanes:
            lane.update()

            if lane.index == player_row and isinstance(lane, Road):
                if lane.hit_by_car(self.player):
                    self.loss_count += 1
                    self.player.reset_position()

    def on_key_press(self, key, modifiers):
        self.player.move(key, self.lanes)

    def draw_debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
