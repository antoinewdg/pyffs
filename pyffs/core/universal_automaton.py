import csv
from collections import namedtuple
from os.path import join

from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING

from . import ParametrizedState, Position

UniversalAutomaton = namedtuple("UniversalAutomaton", [
    'states', 'bit_vectors', 'matrix', 'max_i_minus_e'
])

State = namedtuple("State", ['id', 'min_boundary'])


def state_from_string(s):
    id_, min_boundary = [int(v) for v in s.split(',')]
    return State(id_, min_boundary)


def write_to_file(automaton: UniversalAutomaton, file):
    writer = csv.writer(file, delimiter=';')
    states_str = [_parametrized_to_str(s) for s in automaton.states]
    writer.writerow(states_str)
    bv_strings = [''.join(str(b) for b in bv) for bv in automaton.bit_vectors]
    writer.writerow(bv_strings)
    writer.writerow(automaton.max_i_minus_e)

    for i in range(len(automaton.states)):
        row = []
        for bv_id, bv in enumerate(automaton.bit_vectors):
            s = automaton.matrix[i][bv_id]
            row.append("%s,%s" % (s.id, s.min_boundary))
        writer.writerow(row)


def _bit_vector_for_string(s):
    if s == '':
        return ()
    return tuple(int(b) for b in list(s))


def _parametrized_to_str(state):
    return ','.join(('%s-%s' % (p.i, p.e) for p in state))


def _parametrized_from_str(s):
    if s == '':
        return ParametrizedState()

    positions = []
    for pos_str in s.split(','):
        sp = pos_str.split('-')
        positions.append(Position(int(sp[0]), int(sp[1])))
    return ParametrizedState(*positions)


def read_from_file(file):
    reader = csv.reader(file, delimiter=';')

    states = [_parametrized_from_str(s) for s in next(reader)]

    bit_vectors = [_bit_vector_for_string(s) for s in next(reader)]
    max_i_minus_e = [int(v) for v in next(reader)]
    matrix = [[] for _ in range(len(states))]

    for id_, line in enumerate(reader):
        for b_index, s in enumerate(line):
            matrix[id_].append(state_from_string(s))

    return UniversalAutomaton(states, bit_vectors, matrix, max_i_minus_e)


