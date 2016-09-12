def _key_position_error_first(p):
    return p.e, p.i


class PositionSet:
    def __init__(self, *args):
        self.positions = tuple(sorted(args, key=_key_position_error_first))
        self.min_boundary = 0
        if args:
            self.min_boundary = min(args, key=lambda p: p.i).i

    def __getitem__(self, item):
        return self.positions[item]

    def __len__(self):
        return len(self.positions)

    def __str__(self):
        return str(self.positions)

    def __repr__(self):
        return repr(self.positions)

    def __eq__(self, other):
        return self.positions == other.positions


def _get_minimum_position_set_index(position_sets, indexes):
    r = [i for i in range(0, len(indexes)) if indexes[i] < len(position_sets[i])]

    if not r:
        return -1
    return min(list(r), key=lambda i: _key_position_error_first(position_sets[i][indexes[i]]))


def reduced_union(*args):
    position_sets = args
    indexes = [0 for _ in range(len(position_sets))]
    result = []

    while True:
        i = _get_minimum_position_set_index(position_sets, indexes)
        if i < 0:
            break

        candidate = position_sets[i][indexes[i]]
        if not any((candidate.is_subsumed_by(p) for p in result)):
            result.append(candidate)
        indexes[i] += 1

    return PositionSet(*result)
