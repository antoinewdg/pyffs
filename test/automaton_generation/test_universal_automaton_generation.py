from pyffs.core import State, ParametrizedState, Position
from pyffs.automaton_generation import generate_universal_automaton


def test_generate_automaton_0():
    expected = [
        {(): State(0, 0), (1,): State(0, 0), (0,): State(0, 0)},
        {(): State(0, 0), (1,): State(1, 1), (0,): State(0, 0)}
    ]

    automaton = generate_universal_automaton(0)
    states = [ParametrizedState(), ParametrizedState(Position(0, 0))]

    assert automaton.states == states
    assert automaton.matrix == expected
    assert automaton.bit_vectors == [(), (0,), (1,)]
    assert automaton.max_i_minus_e == [0, 0]


def test_generate_automaton_1():
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

    automaton = generate_universal_automaton(1)

    assert automaton.matrix == expected
    assert automaton.max_i_minus_e == [0, 0, -1, 0, 1, 1]
