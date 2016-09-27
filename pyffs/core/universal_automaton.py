import csv
from collections import namedtuple

UniversalAutomaton = namedtuple("UniversalAutomaton", [
    'bit_vectors', 'matrix', 'max_i_minus_e'
])

State = namedtuple("State", ['id', 'min_boundary'])


def state_from_string(s):
    id_, min_boundary = [int(v) for v in s.split(',')]
    return State(id_, min_boundary)


def write_to_file(automaton: UniversalAutomaton, file):
    writer = csv.writer(file, delimiter=';')

    n_states = len(automaton.max_i_minus_e)
    n_bit_vectors = len(automaton.bit_vectors)
    writer.writerow([n_states, n_bit_vectors])

    bv_strings = [''.join(str(b) for b in bv) for bv in automaton.bit_vectors]
    writer.writerow(bv_strings)
    writer.writerow(automaton.max_i_minus_e)

    for i in range(n_states):
        row = []
        for bv_id, bv in enumerate(automaton.bit_vectors):
            s = automaton.matrix[i][bv_id]
            row.append("%s,%s" % (s.id, s.min_boundary))
        writer.writerow(row)


def _bit_vector_for_string(s):
    if s == '':
        return ()
    return tuple(int(b) for b in list(s))


def read_from_file(file):
    reader = csv.reader(file, delimiter=';')

    n_states, n_bit_vectors = (int(n) for n in next(reader))

    bit_vectors = [_bit_vector_for_string(s) for s in next(reader)]
    max_i_minus_e = [int(v) for v in next(reader)]
    matrix = [[] for _ in range(n_states)]

    for id_, line in enumerate(reader):
        for b_index, s in enumerate(line):
            matrix[id_].append(state_from_string(s))

    return UniversalAutomaton(bit_vectors, matrix, max_i_minus_e)
