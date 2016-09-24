from collections import namedtuple

from pyffs.transition_matrix import transition_matrix_manager, State


class LevenshteinAutomaton:
    def __init__(self, tolerance, query_word, alphabet):
        self._matrix, _, self._states_i_e = transition_matrix_manager.get_for_tolerance(tolerance)
        self._word = query_word
        self.tolerance = tolerance

        self._precomputed_bit_vectors = [{} for _ in range(len(query_word) + 1)]
        for i in range(len(self._word) + 1):
            for symbol in alphabet:
                self._precomputed_bit_vectors[i][symbol] = self._compute_bit_vector(symbol, i)

    def _compute_bit_vector(self, symbol, i):
        bit_list = []
        for c in self._word[i:min(i + 2 * self.tolerance + 1, len(self._word))]:
            bit_list.append(int(c == symbol))

        return tuple(bit_list)

    def transition(self, state: State, symbol):
        new_state = self._matrix[state.id][self._precomputed_bit_vectors[state.min_boundary][symbol]]
        return State(new_state.id, new_state.min_boundary + state.min_boundary)

    def is_final(self, state: State):
        return self._states_i_e[state.id] + state.min_boundary >= len(self._word) - self.tolerance - 1

    @staticmethod
    def is_empty_state(state: State):
        return state.id == 0

    @staticmethod
    def get_initial_state():
        return State(id=1, min_boundary=0)
