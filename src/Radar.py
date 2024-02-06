import matplotlib.pyplot as plt
from random import *
import pickle
from os.path import exists


def arg_max(table):
    return max(table, key=table.get)


# RADAR ?
class Agent:
    def __init__(self, env, actions, learning_rate=1, discount_factor=0.9):
        self.position = None
        self.env = env
        self.reset()
        self.qtable = {}
        self.add_state(self.state)

        self.actions = actions

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.history = []
        self.noise = 0

    def reset(self):
        self.position = self.env.start
        self.score = 0
        self.iteration = 0
        self.state = self.env.get_radar(self.position)

    def best_action(self):
        if random() < self.noise:
            return choice(self.actions)
        else:
            return arg_max(self.qtable[self.state])

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in self.actions:
                self.qtable[state][action] = 0.0

    def do(self):
        action = self.best_action()
        new_state, position, reward = self.env.do(self.position, action)
        self.score += reward
        self.iteration += 1
        self.position = position

        # Q-learning
        self.add_state(new_state)
        maxQ = max(self.qtable[new_state].values())
        delta = self.learning_rate * (reward + self.discount_factor * maxQ \
                                      - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state

        if self.position == self.env.goal:
            self.history.append(self.score)
            self.noise *= 1 - 1E-1

        return action, reward

    def load(self, filename):
        if exists(filename):
            with open(filename, 'rb') as file:
                self.qtable = pickle.load(file)
            self.reset()

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.qtable, file)


class Radar:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.radar = None

    def set_radar(self, radar):
        self.radar = radar

    def get_radar(self):
        return self.radar
