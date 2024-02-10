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


MAP_START = 'S'
MAP_GOAL = 'A'
MAP_WALL = 'O'


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

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

    def get_pos(self):
        return self.player.current_row(), self.player.current_col()

    def map_to_string(self):
        player_row, player_col = self.get_pos()
        map_str = ""
        for index, lane in enumerate(self.lanes):
            if isinstance(lane, SafeZone):
                if index == MAP_ROW - 1:
                    map_str += "A" * MAP_COL  # 'A' représente l'arrivée
                else:
                    map_str += "S" * MAP_COL  # 'S' représente une la SafeZone de départ
            elif isinstance(lane, Grass):
                lane_str = ["."] * MAP_COL  # '.' représente un espace vide
                for obstacle in lane.obstacles:
                    col = int(obstacle.center_x / SPRITE_SIZE)  # Calculer la colonne de l'obstacle
                    lane_str[col] = "O"  # 'O' représente un obstacle
                map_str += "".join(lane_str)
            elif isinstance(lane, Road):
                lane_str = ["."] * MAP_COL  # '.' représente un espace vide
                for car in lane.cars:
                    col = int(car.center_x / SPRITE_SIZE)  # Calculer la colonne de la voiture
                    lane_str[col] = "C"  # 'C' représente une voiture
                map_str += "".join(lane_str)
            map_str += "\n"  # Nouvelle ligne à la fin de chaque lane

        # Remplacement de l'élément correspondant à la position du joueur par une autre lettre
        map_str = map_str[:player_row * (MAP_COL + 1) + player_col] + "P" + map_str[player_row * (
                    MAP_COL + 1) + player_col + 1:]

        return map_str

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

    def get_radar(self, state):
        row, col = state[0], state[1]
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                     (row - 2, col), (row + 2, col), (row, col - 2), (row, col + 2)]
        radar = []
        for n in neighbors:
            if n in self.map:
                radar.append(self.map[n])
            else:
                radar.append(MAP_WALL)
        delta_row = sign(self.goal[0] - row) + 1
        delta_col = sign(self.goal[1] - col) + 1
        radar_goal = [0] * 9

        position = delta_row * 3 + delta_col
        radar_goal[position] = 1

        return tuple(radar + radar_goal)

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
        return self.get_radar(self.get_pos())

    def on_key_press(self, key, modifiers):
        self.player.move(key, self.lanes)

    def draw_debug_grid(self):
        for i in range(0, MAP_COL):
            arcade.draw_line(i * SPRITE_SIZE, 0, i * SPRITE_SIZE, MAP_ROW * SPRITE_SIZE, arcade.color.WHITE, 1)
        for i in range(0, MAP_ROW):
            arcade.draw_line(0, i * SPRITE_SIZE, MAP_COL * SPRITE_SIZE, i * SPRITE_SIZE, arcade.color.WHITE, 1)
