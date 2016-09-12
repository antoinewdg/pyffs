from .position_set import PositionSet, reduced_union
from .position import Position


def _get_next_candidates(tolerance, current):
    base = current[0]
    back = current[-1]
    result = []

    i0 = base.i + base.e
    e0 = 0
    if back != base:
        e0 = back.e + 1
        for j in range(back.i + 1, i0 + back.e + 1):
            result.append(Position(j, back.e))

    for f in range(e0, tolerance + 1):
        for j in range(i0 - f, i0 + f + 1):
            result.append(Position(j, f))

    return result


class ParametrizedState:
    def __init__(self, *args):
        self.position_set = PositionSet(*args)

    @staticmethod
    def from_position_set(position_set):
        param = position_set.min_boundary
        new_positions = [Position(p.i - param, p.e) for p in position_set]
        return param, ParametrizedState(*new_positions)

    def transition(self, bit_vector, tolerance):
        if len(self.position_set) == 0:
            return 0, ParametrizedState()

        transitions = [PositionSet(*p.transition(bit_vector[p.i:], tolerance))
                       for p in self.position_set]

        reduced = reduced_union(*transitions)
        return self.from_position_set(reduced)

    @staticmethod
    def generate_all(tolerance):
        newly_generated = [[Position(0, e)] for e in range(tolerance + 1)]
        result = []

        while newly_generated:
            result.extend(newly_generated)
            old = newly_generated
            newly_generated = []
            for positions in old:
                candidates = _get_next_candidates(tolerance, positions)
                for c in candidates:
                    is_valid = not any((p.subsumes(c) or c.subsumes(p) for p in positions))
                    if is_valid:
                        new_positions = positions + [c]
                        newly_generated.append(new_positions)

        return [ParametrizedState()] + [ParametrizedState(*r) for r in result]

    def __eq__(self, other):
        return self.position_set == other.position_set

    def __repr__(self):
        return repr(self.position_set)

    def __hash__(self):
        return hash(self.position_set.positions)

    def __iter__(self):
        for x in self.position_set.positions:
            yield x

    def __len__(self):
        return len(self.position_set.positions)
