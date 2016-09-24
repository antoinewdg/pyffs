from collections import namedtuple

Position = namedtuple("Position", ['i', 'e'])


class ParametrizedState:
    def __init__(self, *args):
        self.positions = args

    def __eq__(self, other):
        return self.positions == other.positions

    def __iter__(self):
        for x in self.positions:
            yield x

    def __len__(self):
        return len(self.positions)
