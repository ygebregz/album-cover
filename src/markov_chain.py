"""
Markov Chain

Generates transition matrix and provides functionalut
to get next state

"""
from typing import List
import random


class MarkovChain:

    def __init__(self, order: int, noise: int) -> None:
        self.transition_matrix = {}
        self.order = order
        self.noise = noise

    def populate_transition_matrix(self, rgb_data: List[tuple]):
        pass

    def get_next_state(self, curr_state):
        pass
