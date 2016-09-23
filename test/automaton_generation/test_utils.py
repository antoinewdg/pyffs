from pyffs.automaton_generation.utils import generate_all_bit_vectors_under_n


def test_generate_all_bit_vectors_under_0():
    generated = generate_all_bit_vectors_under_n(0)
    expected = [()]
    assert expected == generated


def test_generate_all_bit_vectors_under_1():
    generated = generate_all_bit_vectors_under_n(1)
    expected = [(), (0,), (1,)]
    assert expected == generated


def test_generate_all_bit_vectors_under_3():
    generated = generate_all_bit_vectors_under_n(3)
    expected = [
        (),
        (0,),
        (1,),
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    ]
    assert expected == generated
