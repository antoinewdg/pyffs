class State:
    def __init__(self, id_, min_boundary):
        self.id = id_
        self.min_boundary = min_boundary

    @staticmethod
    def from_string(s):
        id_, min_boundary = [int(v) for v in s.split(',')]
        return State(id_, min_boundary)

    def __repr__(self):
        return "State(%s,%s)" % (self.id, self.min_boundary)

    def __eq__(self, other):
        return (self.id, self.min_boundary) == \
               (other.id, other.min_boundary)
