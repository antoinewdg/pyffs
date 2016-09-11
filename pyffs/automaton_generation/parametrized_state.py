from .position_set import PositionSet, reduced_union
from .position import Position


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

        print()
        print(self)
        print(bit_vector)
        print(transitions)

        reduced = reduced_union(*transitions)

        print(reduced)
        return self.from_position_set(reduced)

    def __eq__(self, other):
        return self.position_set == other.position_set

    def __repr__(self):
        return repr(self.position_set)
