import arcade
import arcade.gui
import random

from arcade.gui import UIBoxLayout

from src.Grass import Grass
from src.Player import Player
from settings import SPRITE_SIZE, MAP_COL, MAP_ROW, ROAD_PROBABILITY, ACTIONS, BASE_WINDOW_RATE
from src.Road import Road
from src.SafeZone import SafeZone
from src.UI import UI


class GameWindow(arcade.Window):
    def __init__(self, debug_mode):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road')
        self.lanes = []
        self.generate_map()
        self.player = Player(self.lanes)
        self.debug_mode = debug_mode
        self.win_count = 0
        self.loss_count = 0
        self.rate = BASE_WINDOW_RATE
        self.ui = UI(self)

    def generate_map(self):
        for i in range(0, MAP_ROW):
            if i == 0 or i == MAP_ROW - 1:
                lane = SafeZone(i, "start" if i == 0 else "end")
            else:
                rand = random.randint(0, 10)
                if rand < ROAD_PROBABILITY:
                    lane = Road(i)
                else:
                    lane = Grass(i)

            self.lanes.append(lane)

    def on_draw(self):
        arcade.start_render()

        for lane in self.lanes:
            lane.draw()

        self.player.draw()

        if self.debug_mode:
            self.draw_debug_grid()
            self.player.agent.draw_state()

        self.draw_counters()
        self.ui.draw()

    def draw_counters(self):
        self.draw_text('Wins: ' + str(self.win_count), 5, MAP_ROW * SPRITE_SIZE - 20)
        self.draw_text('Losses: ' + str(self.loss_count), 5, MAP_ROW * SPRITE_SIZE - 40)
        winrate = round(self.win_count / (self.win_count + self.loss_count) * 100, 2) if self.win_count + self.loss_count > 0 else 0
        self.draw_text('Winrate: ' + str(winrate) + '%', MAP_COL / 3 * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE - 20)
        self.draw_text('Iterations: ' + str(self.win_count + self.loss_count), MAP_COL / 3 * SPRITE_SIZE,MAP_ROW * SPRITE_SIZE - 40)
        self.draw_text('Q-Table Size: ' + str(len(self.player.agent.qtable) * len(ACTIONS)), MAP_COL / 3 * SPRITE_SIZE * 2, MAP_ROW * SPRITE_SIZE - 20)
        self.draw_text('Score: ' + str(self.player.agent.score), MAP_COL / 3 * SPRITE_SIZE * 2, MAP_ROW * SPRITE_SIZE - 40)
        self.draw_text('Speed: ' + str(self.rate), MAP_COL/8 * SPRITE_SIZE, 20)

    def draw_text(self, text, x, y):
        arcade.draw_text(text, x, y, arcade.color.BLACK, 14, bold=True)

    def on_update(self, delta_time):

        for lane in self.lanes:
            lane.update()

        player_row = self.player.current_row()

        if player_row != MAP_ROW - 1:
            self.player.agent.update()
        else:
            self.player.agent.history.append(self.player.agent.score)
            self.win_count += 1
            self.player.reset_position()

        player_row = self.player.current_row()

        for lane in self.lanes:
            if lane.index == player_row and isinstance(lane, Road):
                if lane.hit_by_car(self.player):
                    self.player.agent.history.append(self.player.agent.score)
                    self.loss_count += 1
                    self.player.reset_position()

    def on_key_press(self, key, modifiers):
        self.player.move(key, self.lanes)

    def draw_debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
