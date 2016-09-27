from os.path import dirname, join

from pyffs import core

from .parametrized_state import ParametrizedState
from .utils import generate_all_bit_vectors_under_n


def generate_universal_automaton(tolerance):
    bit_vectors = generate_all_bit_vectors_under_n(2 * tolerance + 1)
    states = ParametrizedState.generate_all(tolerance)
    empty_state, valid_states = states[0], states[1:]

    states_ids = {s: i for i, s in enumerate(valid_states)}
    states_ids[empty_state] = -1
    matrix = [[-1 for __ in range(len(bit_vectors))] for _ in range(len(valid_states))]

    for i, s in enumerate(valid_states):
        for b_id, b in enumerate(bit_vectors):
            min_boundary, new_state = s.transition(b, tolerance)
            matrix[i][b_id] = core.State(states_ids[new_state], min_boundary)

    max_i_minus_e = [0 for _ in range(len(valid_states))]
    for i, state in enumerate(valid_states):
        if len(state) > 0:
            max_i_minus_e[i] = max((p.i - p.e) for p in state)

    return core.UniversalAutomaton(bit_vectors, matrix, max_i_minus_e)
