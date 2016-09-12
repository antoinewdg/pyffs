import csv


class State:
    def __init__(self, id, min_boundary):
        self.id = id
        self.min_boundary = min_boundary

    def __repr__(self):
        return "State(%s,%s)" % (self.id, self.min_boundary)

    def __eq__(self, other):
        return (self.id, self.min_boundary) == \
               (other.id, other.min_boundary)


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
