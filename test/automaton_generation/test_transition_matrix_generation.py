from pyffs.transition_matrix import State
from pyffs.automaton_generation import generate_transition_matrix


def test_generate_transition_matrix_0():
    expected = [
        {(): State(0, 0), (1,): State(0, 0), (0,): State(0, 0)},
        {(): State(0, 0), (1,): State(1, 1), (0,): State(0, 0)}
    ]

    actual, bit_vectors, states_i_e = generate_transition_matrix(0)

    assert actual == expected
    assert bit_vectors == [(), (0,), (1,)]
    assert states_i_e == [0, 0]


def test_generate_transition_matrix_1():
    expected = [
        {
            (0, 1): State(0, 0),
            (0, 1, 1): State(0, 0),
            (0, 0): State(0, 0),
            (1,): State(0, 0),
            (0,): State(0, 0),
            (1, 0, 0): State(0, 0),
            (1, 1, 0): State(0, 0),
            (0, 0, 1): State(0, 0),
            (1, 1): State(0, 0),
            (1, 1, 1): State(0, 0),
            (): State(0, 0),
            (0, 1, 0): State(0, 0),
            (1, 0, 1): State(0, 0),
            (1, 0): State(0, 0),
            (0, 0, 0): State(0, 0)
        }, {
            (0, 1): State(5, 0),
            (0, 1, 1): State(5, 0),
            (0, 0): State(3, 0),
            (1,): State(1, 1),
            (0,): State(3, 0),
            (1, 0, 0): State(1, 1),
            (1, 1, 0): State(1, 1),
            (0, 0, 1): State(3, 0),
            (1, 1): State(1, 1),
            (1, 1, 1): State(1, 1),
            (): State(2, 0),
            (0, 1, 0): State(5, 0),
            (1, 0, 1): State(1, 1),
            (1, 0): State(1, 1),
            (0, 0, 0): State(3, 0)
        }, {
            (0, 1): State(0, 0),
            (0, 1, 1): State(0, 0),
            (0, 0): State(0, 0),
            (1,): State(2, 1),
            (0,): State(0, 0),
            (1, 0, 0): State(2, 1),
            (1, 1, 0): State(2, 1),
            (0, 0, 1): State(0, 0),
            (1, 1): State(2, 1),
            (1, 1, 1): State(2, 1),
            (): State(0, 0),
            (0, 1, 0): State(0, 0),
            (1, 0, 1): State(2, 1),
            (1, 0): State(2, 1),
            (0, 0, 0): State(0, 0)
        }, {
            (0, 1): State(2, 2),
            (0, 1, 1): State(2, 2),
            (0, 0): State(0, 0),
            (1,): State(2, 1),
            (0,): State(0, 0),
            (1, 0, 0): State(2, 1),
            (1, 1, 0): State(3, 1),
            (0, 0, 1): State(0, 0),
            (1, 1): State(3, 1),
            (1, 1, 1): State(3, 1),
            (): State(0, 0),
            (0, 1, 0): State(2, 2),
            (1, 0, 1): State(2, 1),
            (1, 0): State(2, 1),
            (0, 0, 0): State(0, 0)
        }, {
            (0, 1): State(0, 0),
            (0, 1, 1): State(2, 3),
            (0, 0): State(0, 0),
            (1,): State(2, 1),
            (0,): State(0, 0),
            (1, 0, 0): State(2, 1),
            (1, 1, 0): State(2, 1),
            (0, 0, 1): State(2, 3),
            (1, 1): State(2, 1),
            (1, 1, 1): State(4, 1),
            (): State(0, 0),
            (0, 1, 0): State(0, 0),
            (1, 0, 1): State(4, 1),
            (1, 0): State(2, 1),
            (0, 0, 0): State(0, 0)
        }, {
            (0, 1): State(2, 2),
            (0, 1, 1): State(3, 2),
            (0, 0): State(0, 0),
            (1,): State(2, 1),
            (0,): State(0, 0),
            (1, 0, 0): State(2, 1),
            (1, 1, 0): State(3, 1),
            (0, 0, 1): State(2, 3),
            (1, 1): State(3, 1),
            (1, 1, 1): State(5, 1),
            (): State(0, 0),
            (0, 1, 0): State(2, 2),
            (1, 0, 1): State(4, 1),
            (1, 0): State(2, 1),
            (0, 0, 0): State(0, 0)
        }
    ]

    actual, bit_vectors, states_i_e = generate_transition_matrix(1)

    assert actual == expected
    assert states_i_e == [0, 0, -1, 0, 1, 1]
