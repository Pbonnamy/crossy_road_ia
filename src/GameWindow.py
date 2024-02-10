# GameWindow.py
import arcade
import random

from src.Grass import Grass
from src.Player import Player
from settings import SPRITE_SIZE, MAP_COL, MAP_ROW
from src.QlearningAgent import QLearningAgent
from src.Road import Road
from src.SafeZone import SafeZone
from arcade.key import UP, LEFT, RIGHT, DOWN

# Le reste du code reste inchangé


ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'
ACTIONS = [LEFT, RIGHT, UP, DOWN, ACTION_IDLE]
REWARD_ROAD = -1
REWARD_GOAL = 100
REWARD_WALL = -100


class GameWindow(arcade.Window):
    def __init__(self, debug_mode):
        super().__init__(MAP_COL * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, 'Crossy Road')
        self.player = Player()
        self.agent = QLearningAgent(self.player)
        self.lanes = []
        self.debug_mode = debug_mode
        self.win_count = 0
        self.loss_count = 0
        self.generate_map()

    def calculate_reward(self):
        player_row = self.player.current_row()
        if player_row == MAP_ROW - 1:
            return REWARD_GOAL
        for lane in self.lanes:
            if lane.index == player_row and isinstance(lane, Road):
                if lane.hit_by_car(self.player):
                    return REWARD_WALL
        return REWARD_ROAD

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

        self.draw_counters()

    def draw_counters(self):
        arcade.draw_text('Wins: ' + str(self.win_count), 5, MAP_ROW * SPRITE_SIZE - 20, arcade.color.BLACK, 14,
                         bold=True)
        arcade.draw_text('Losses: ' + str(self.loss_count), 5, MAP_ROW * SPRITE_SIZE - 40, arcade.color.BLACK, 14,
                         bold=True)

    def on_update(self, delta_time):
        print(self.map_to_string())
        state = (self.player.current_row(), self.player.current_col())
        action = self.agent.choose_action(ACTIONS)
        self.player.move(action, self.lanes)
        reward = self.calculate_reward()
        next_state = (self.player.current_row(), self.player.current_col())
        # Passer action, reward et next_state à la méthode update de QLearningAgent
        self.agent.update(state, action, reward, next_state, self.lanes)

        self.agent.update_player(action, self.lanes)

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
