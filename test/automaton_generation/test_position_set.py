from pyffs.automaton_generation.position_set import PositionSet, reduced_union
from pyffs.automaton_generation.position import Position


class TestPositionsSet:
    def test_construction(self):
        s = PositionSet(Position(1, 1), Position(0, 3), Position(2, 0))
        expected = (Position(2, 0), Position(1, 1), Position(0, 3))

        assert s.positions == expected
        assert s.min_boundary == 0

    def test_reduced_union_keeps_positions_sorted(self):
        a = PositionSet(Position(0, 0), Position(3, 1))
        b = PositionSet(Position(1, 0))
        expected = PositionSet(Position(0, 0), Position(1, 0), Position(3, 1))

        assert reduced_union(a, b) == expected

    def test_reduced_union_removes_subsumed_position(self):
        a = PositionSet(Position(0, 0), Position(3, 1))
        b = PositionSet(Position(1, 0))
        c = PositionSet(Position(1, 1))
        expected = PositionSet(Position(0, 0), Position(1, 0), Position(3, 1))

        assert reduced_union(a, b, c) == expected

    def test_reduced_unions_removes_duplicates(self):
        a = PositionSet(Position(0, 1), Position(1, 1))
        b = PositionSet(Position(1, 1), Position(2, 1))
        expected = PositionSet(Position(0, 1), Position(1, 1), Position(2, 1))

        assert reduced_union(a, b) == expected
