"""
Markov Chain

Generates transition matrix and provides functionalut
to get next state

"""
from typing import List
import numpy as np
from collections import defaultdict, Counter
import random


class MarkovChain:

    def __init__(self, tempo: int) -> None:
        self.transition_matrix = defaultdict(Counter)
        self.order = 10
        self.noise = self.calc_noise_amount(tempo)

    def calc_noise_amount(self, tempo: int):
        min_noise, max_noise = 0.2, 0.8
        min_tempo, max_tempo = 80, 150  # for my range of music
        normalized_tempo = (tempo - min_tempo) / (max_tempo - min_tempo)
        noise_level = min_noise + (max_noise - min_noise) * normalized_tempo
        return noise_level

    def apply_noise(self, pixel: tuple):
        pixel_list = list(pixel)
        for i in range(len(pixel_list)):
            if np.random.rand() < self.noise * 0.5:
                pixel_list[i] = (pixel_list[i] + 1) % 256
        return tuple(pixel_list)

    def get_key(self, pixel_data: List[tuple], index: int):
        key = []
        for pixel in pixel_data[index:index+self.order]:
            for rgb_data in pixel:
                key.append(rgb_data)
        return tuple(key)

    def normalize(self, value_dict: dict):
        total = sum(value_dict.values())
        for key, value in value_dict.items():
            value_dict[key] = value / total
        return value_dict

    def populate_transition_matrix(self, rgb_data: List[tuple]):
        for i in range(len(rgb_data)):
            rgb_data[i] = self.apply_noise(rgb_data[i])
        rgb_data.extend(rgb_data[0:self.order])

        for index in range(len(rgb_data) - self.order):
            key = self.get_key(rgb_data, index)
            self.transition_matrix[key][rgb_data[index+self.order]] += 1

        for key, value in self.transition_matrix.items():
            self.transition_matrix[key] = self.normalize(value)

    def get_next_state(self, curr_state):
        probabilities = list(self.transition_matrix[curr_state].values())
        possible_states = list(self.transition_matrix[curr_state].keys())
        state_map = {i: state for i, state in enumerate(possible_states)}
        next_state_index = np.random.choice(
            list(state_map.keys()), p=probabilities)
        next_state = state_map[next_state_index]
        curr_state = list(curr_state)[3:self.order*3]
        curr_state.extend(list(next_state))
        return tuple(curr_state)

    def generate_image_data(self, image_size: List):
        new_image_pixels = []
        curr_state = random.choice(list(self.transition_matrix.keys()))
        for _ in range(image_size[0] * image_size[1]):
            curr_state = self.get_next_state(curr_state)
            new_image_pixels.append(
                curr_state[-self.order*3:-self.order][:3])
        return new_image_pixels
