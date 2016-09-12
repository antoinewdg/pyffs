class Position:
    def __init__(self, i, e):
        self.i = i
        self.e = e

    def transition(self, bit_vector, tolerance):
        if bit_vector == ():
            result = [Position(self.i, self.e + 1)]
        elif bit_vector[0] == 1:
            result = [Position(self.i + 1, self.e)]
        else:
            result = [Position(self.i, self.e + 1), Position(self.i + 1, self.e + 1)]
            for k, b in enumerate(bit_vector[1:]):
                if b == 1:
                    result.append(Position(self.i + k + 2, self.e + k + 1))
                    break

        return [p for p in result if p.e <= tolerance]

    def subsumes(self, p):
        return self.e <= p.e and abs(self.i - p.i) <= p.e - self.e

    def is_subsumed_by(self, p):
        return p.subsumes(self)

    def __str__(self):
        return "(%s,%s)" % (self.i, self.e)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return other.i == self.i and other.e == self.e

    def __hash__(self):
        return hash((self.i, self.e))
