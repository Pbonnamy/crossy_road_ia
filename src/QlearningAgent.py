import numpy as np

from settings import MAP_ROW, MAP_COL
from arcade.key import UP, LEFT, RIGHT, DOWN

from src.Road import Road

ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, ACTION_IDLE = 'U', 'D', 'L', 'R', 'I'

ACTIONS = [LEFT, RIGHT, UP, DOWN, ACTION_IDLE]


class QLearningAgent:
    def __init__(self, player, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.player = player
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros((MAP_ROW, MAP_COL, len(ACTIONS)))

    def choose_action(self, actions):
        print("je choois une action")
        row, col = self.player.current_row(), self.player.current_col()
        q_values = self.q_table[row, col, :]
        print("action q_values", actions[np.argmax(q_values)])
        return actions[np.argmax(q_values)]

    def update(self, state, action, reward, next_state, lanes):
        penalty = 50
        if self.detect_nearby_cars(lanes, detection_distance=10):
            adjust_reward = reward - penalty
            print("Voiture(s) => mise à jour de la récompense de l'agent")
        else:
            adjust_reward = reward
            print("Aucune voiture, récompense normal")
        row, col = state
        next_row, next_col = next_state
        current_q = self.q_table[row, col, ACTIONS.index(action)]
        max_future_q = np.max(self.q_table[next_row, next_col, :])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (
                adjust_reward + self.discount_factor * max_future_q)
        self.q_table[row, col, ACTIONS.index(action)] = new_q

        self.player.move(action, lanes)

    def reset(self):
        self.q_table = np.zeros((MAP_ROW, MAP_COL, len(ACTIONS)))

    def detect_nearby_cars(self, lanes, detection_distance=50):
        """
        Détecte si une voiture est à côté de l'agent.

        :param lanes: Liste des voies sur la route.
        :param detection_distance: Distance à partir de laquelle une voiture est considérée comme étant à proximité.
        :return: Booléen indiquant la présence d'une voiture à proximité.
        """
        # Obtenir la position actuelle de l'agent
        agent_x, agent_y = self.player.sprite.center_x, self.player.sprite.center_y

        # Itérer à travers chaque voie pour vérifier la présence de voitures
        for lane in lanes:
            if isinstance(lane, Road):  # Assurer que la 'lane' est bien une voie de circulation
                for car in lane.cars:
                    # Calculer la distance entre l'agent et la voiture
                    distance = ((agent_x - car.center_x) ** 2 + (agent_y - car.center_y) ** 2) ** 0.5

                    # Si une voiture est à l'intérieur du seuil de détection, renvoyer True
                    print(f'Distance: {distance}, Detection distance: {detection_distance}')
                    if distance < detection_distance:
                        return True
        # Si aucune voiture n'est détectée à proximité, renvoyer False
        return False

    def update_player(self, action, lanes):
        self.player.move(action, lanes)

