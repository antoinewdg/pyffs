from .parametrized_state import ParametrizedState
from .utils import generate_all_bit_vectors_under_n
from pyffs.transition_matrix import State


def generate_transition_matrix(tolerance):
    bit_vectors = generate_all_bit_vectors_under_n(2 * tolerance + 1)
    states = ParametrizedState.generate_all(tolerance)

    states_ids = {s: i for i, s in enumerate(states)}
    matrix = [{} for _ in range(len(states))]

    for i, s in enumerate(states):
        for b in bit_vectors:
            min_boundary, new_state = s.transition(b, tolerance)
            matrix[i][b] = State(states_ids[new_state], min_boundary)

    states_max_i_e = [0 for _ in range(len(states))]
    for i, state in enumerate(states):
        if len(state) > 0:
            states_max_i_e[i] = max((p.i - p.e) for p in state)

    return matrix, bit_vectors, states_max_i_e
