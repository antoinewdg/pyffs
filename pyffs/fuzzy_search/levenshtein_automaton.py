from collections import namedtuple

from pyffs.core import State
from pyffs.automaton_management import manager


class LevenshteinAutomaton:
    def __init__(self, tolerance, query_word, alphabet):
        self._automaton = manager.get_for_tolerance(tolerance)
        self._word = query_word
        self.tolerance = tolerance
        self._bit_vectors_ids = {b: i for i, b in enumerate(self._automaton.bit_vectors)}

        self._precomputed_bit_vectors = [{} for _ in range(len(query_word) + 1)]
        for i in range(len(self._word) + 1):
            for symbol in alphabet:
                self._precomputed_bit_vectors[i][symbol] = self._compute_bit_vector_id(symbol, i)

        self._i_minus_e_threshold = len(self._word) - self.tolerance

    def _compute_bit_vector_id(self, symbol, i):
        bit_list = []
        for c in self._word[i:min(i + 2 * self.tolerance + 1, len(self._word))]:
            bit_list.append(int(c == symbol))
        return self._bit_vectors_ids[tuple(bit_list)]

    def transition(self, state: State, symbol):
        bit_vector = self._precomputed_bit_vectors[state.min_boundary][symbol]
        new_state = self._automaton.matrix[state.id][bit_vector]
        return State(new_state.id, new_state.min_boundary + state.min_boundary)

    def is_final(self, state: State):
        i_minus_e = self._automaton.max_i_minus_e[state.id]
        return i_minus_e + state.min_boundary >= self._i_minus_e_threshold

    def get_error(self, state: State):
        i_minus_e = self._automaton.max_i_minus_e[state.id]
        return len(self._word) - (i_minus_e + state.min_boundary)

    @staticmethod
    def is_empty_state(state: State):
        return state.id == -1

    @staticmethod
    def get_initial_state():
        return State(id=0, min_boundary=0)
