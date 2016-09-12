import csv

from .state import State


def save_matrix_to_file(matrix, file, bit_vectors, states_i_e):
    writer = csv.writer(file, delimiter=';')
    writer.writerow(states_i_e)
    bv_strings = [''.join(str(b) for b in bv) for bv in bit_vectors]
    writer.writerow(bv_strings)

    for i in range(len(states_i_e)):
        row = []
        for bv in bit_vectors:
            s = matrix[i][bv]
            row.append("%s,%s" % (s.id, s.min_boundary))
        writer.writerow(row)


def _bit_vector_for_string(s):
    if s == '':
        return ()
    return tuple(int(b) for b in list(s))


def read_matrix_from_file(file):
    reader = csv.reader(file, delimiter=';')

    states_i_e = [int(v) for v in next(reader)]
    bit_vectors = [_bit_vector_for_string(s) for s in next(reader)]
    matrix = [{} for _ in range(len(states_i_e))]

    for id_, line in enumerate(reader):
        for b_index, s in enumerate(line):
            matrix[id_][bit_vectors[b_index]] = State.from_string(s)

    return matrix, bit_vectors, states_i_e
