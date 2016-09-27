from io import StringIO
from pyffs.core.universal_automaton import (write_to_file, State, UniversalAutomaton,
                                            read_from_file)


def test_write_to_file():
    file = StringIO()
    matrix = [
        [State(0, 0), State(0, 0), State(0, 0)],
        [State(0, 0), State(0, 0), State(1, 1)],
    ]
    bit_vectors = [(), (0,), (1,)]
    states_i_e = [0, 0]

    automaton = UniversalAutomaton(bit_vectors, matrix, states_i_e)

    write_to_file(automaton, file)
    assert file.getvalue() == "2;3\r\n;0;1\r\n0;0\r\n0,0;0,0;0,0\r\n0,0;0,0;1,1\r\n"


def test_read_from_file():
    file = StringIO("2;3\r\n;0;1\r\n0;0\r\n0,0;0,0;0,0\r\n0,0;0,0;1,1\r\n")
    automaton = read_from_file(file)
    expected = [
        [State(0, 0), State(0, 0), State(0, 0)],
        [State(0, 0), State(0, 0), State(1, 1)],
    ]

    assert automaton.matrix == expected
    assert automaton.bit_vectors == [(), (0,), (1,)]
    assert automaton.max_i_minus_e == [0, 0]
