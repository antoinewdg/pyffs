from os.path import dirname, join

from .parametrized_state import ParametrizedState
from .utils import generate_all_bit_vectors_under_n
from pyffs import core
from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING


def generate_universal_automaton(tolerance):
    bit_vectors = generate_all_bit_vectors_under_n(2 * tolerance + 1)
    states = ParametrizedState.generate_all(tolerance)
    states_core = [core.ParametrizedState(*s.position_set) for s in states]

    states_ids = {s: i for i, s in enumerate(states)}
    matrix = [[-1 for __ in range(len(bit_vectors))] for _ in range(len(states))]

    for i, s in enumerate(states):
        for b_id, b in enumerate(bit_vectors):
            min_boundary, new_state = s.transition(b, tolerance)
            matrix[i][b_id] = core.State(states_ids[new_state], min_boundary)

    max_i_minus_e = [0 for _ in range(len(states))]
    for i, state in enumerate(states):
        if len(state) > 0:
            max_i_minus_e[i] = max((p.i - p.e) for p in state)

    return core.UniversalAutomaton(states_core, bit_vectors, matrix, max_i_minus_e)
