from io import StringIO

from pyffs.transition_matrix import (State, save_matrix_to_file,
                                     read_matrix_from_file)


def test_save_matrix_to_file():
    file = StringIO()
    matrix = [
        {(): State(0, 0), (1,): State(0, 0), (0,): State(0, 0)},
        {(): State(0, 0), (1,): State(1, 1), (0,): State(0, 0)}
    ]
    bit_vectors = [(), (0,), (1,)]
    states_i_e = [0, 0]

    save_matrix_to_file(matrix, file, bit_vectors, states_i_e)
    assert file.getvalue() == "0;0\r\n;0;1\r\n0,0;0,0;0,0\r\n0,0;0,0;1,1\r\n"


def test_matrix_from_file():
    file = StringIO("0;0\r\n;0;1\r\n0,0;0,0;0,0\r\n0,0;0,0;1,1\r\n")
    matrix, bit_vectors, states_i_e = read_matrix_from_file(file)
    expected = [
        {(): State(0, 0), (1,): State(0, 0), (0,): State(0, 0)},
        {(): State(0, 0), (1,): State(1, 1), (0,): State(0, 0)}
    ]

    assert matrix == expected
    assert bit_vectors == [(), (0,), (1,)]
    assert states_i_e == [0, 0]
