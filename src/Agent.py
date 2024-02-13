import pickle
from os.path import exists

import arcade

from settings import SPRITE_SIZE, MAP_ROW, MAP_COL, WALL, ACTIONS, ACTION_UP, UP_ARROW, ACTION_DOWN, DOWN_ARROW, \
    ACTION_LEFT, LEFT_ARROW, ACTION_RIGHT, RIGHT_ARROW, IDLE, QTABLE_FILE, LEARNING_RATE, DISCOUNT_FACTOR


def arg_max(table):
    return max(table, key=table.get)


class Agent:
    def __init__(self, player, lanes):
        self.qtable = {}
        self.load_qtable()
        self.learning_rate = LEARNING_RATE
        self.discount_factor = DISCOUNT_FACTOR
        self.player = player
        self.lanes = lanes
        self.score = 0
        self.history = []
        self.state = self.get_state()
        self.add_state(self.state)

    def reset(self):
        self.history = []
        self.qtable = {}
        self.state = self.get_state()
        self.add_state(self.state)

    def best_action(self):
        return arg_max(self.qtable[self.state])

    def get_key(self, action):
        if action == ACTION_UP:
            return UP_ARROW
        elif action == ACTION_DOWN:
            return DOWN_ARROW
        elif action == ACTION_LEFT:
            return LEFT_ARROW
        elif action == ACTION_RIGHT:
            return RIGHT_ARROW
        else:
            return IDLE

    def update(self):
        action = self.best_action()
        reward = self.player.move(self.get_key(action))
        self.score += reward
        new_state = self.get_state()
        self.add_state(new_state)

        max_q = max(self.qtable[new_state].values())
        delta = self.learning_rate * (reward + self.discount_factor * max_q - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state

    def get_neighbors(self):
        row = self.player.current_row() * SPRITE_SIZE
        col = self.player.current_col() * SPRITE_SIZE
        return [
            (row + SPRITE_SIZE * 2, col - SPRITE_SIZE),
            (row + SPRITE_SIZE * 2, col),
            (row + SPRITE_SIZE * 2, col + SPRITE_SIZE),
            (row + SPRITE_SIZE * 3, col - SPRITE_SIZE),
            (row + SPRITE_SIZE * 3, col),
            (row + SPRITE_SIZE * 3, col + SPRITE_SIZE),
            (row + SPRITE_SIZE, col - SPRITE_SIZE),
            (row + SPRITE_SIZE, col),
            (row + SPRITE_SIZE, col + SPRITE_SIZE),
            (row, col - SPRITE_SIZE),
            (row, col - SPRITE_SIZE * 2),
            (row, col + SPRITE_SIZE),
            (row, col + SPRITE_SIZE * 2),
            (row - SPRITE_SIZE, col - SPRITE_SIZE),
            (row - SPRITE_SIZE, col - SPRITE_SIZE * 2),
            (row - SPRITE_SIZE, col),
            (row - SPRITE_SIZE, col + SPRITE_SIZE),
            (row - SPRITE_SIZE, col + SPRITE_SIZE * 2)
        ]

    def get_state(self):
        neighbors = self.get_neighbors()

        state = []

        for neighbor in neighbors:
            if (
                    neighbor[0] < 0
                    or neighbor[1] < 0
                    or neighbor[0] >= SPRITE_SIZE * MAP_ROW
                    or neighbor[1] >= SPRITE_SIZE * MAP_COL
            ):
                state.append(WALL)
            else:
                target_row = int(neighbor[0] / SPRITE_SIZE)
                target_col = int(neighbor[1] / SPRITE_SIZE)
                for lane in self.lanes:
                    if lane.index == target_row:
                        state.append(lane.get_state(target_col))
                        break

        return tuple(state)

    def save_qtable(self):
        with open(QTABLE_FILE, 'wb') as file:
            pickle.dump(self.qtable, file)

    def load_qtable(self):
        if exists(QTABLE_FILE):
            with open(QTABLE_FILE, 'rb') as file:
                self.qtable = pickle.load(file)

    def draw_state(self):
        neighbors = self.get_neighbors()
        current_state = self.get_state()
        for i in range(0, len(neighbors)):
            arcade.draw_rectangle_outline(
                neighbors[i][1] + SPRITE_SIZE / 2,
                neighbors[i][0] + SPRITE_SIZE / 2,
                SPRITE_SIZE,
                SPRITE_SIZE,
                arcade.color.RED
            )

            arcade.draw_text(
                current_state[i],
                neighbors[i][1] + SPRITE_SIZE / 2,
                neighbors[i][0] + SPRITE_SIZE / 2,
                arcade.color.RED,
                14,
                anchor_x='center',
                anchor_y='center'
            )

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in ACTIONS:
                self.qtable[state][action] = 0.0
