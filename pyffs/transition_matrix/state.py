from collections import namedtuple

State = namedtuple("State", ['id', 'min_boundary'])


def state_from_string(s):
    id_, min_boundary = [int(v) for v in s.split(',')]
    return State(id_, min_boundary)
