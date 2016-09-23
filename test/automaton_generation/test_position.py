from pyffs.automaton_generation.position import Position


class TestPosition:
    def test_transition_with_high_tolerance(self):
        p = Position(0, 0)

        expected = [Position(1, 0)]
        assert p.transition((1, 0), 3) == expected
        assert p.transition((1, 1, 1, 0, 1), 3) == expected
        assert p.transition((1, 0, 0, 0, 0), 3) == expected

        expected = [Position(0, 1), Position(1, 1)]
        assert p.transition((0,), 3) == expected
        assert p.transition((0, 0, 0), 3) == expected

        expected = [Position(0, 1)]
        assert p.transition((), 3) == expected

        expected = [Position(0, 1), Position(1, 1), Position(4, 3)]
        assert p.transition((0, 0, 0, 1,), 3) == expected
        assert p.transition((0, 0, 0, 1, 1, 1,), 3) == expected
        assert p.transition((0, 0, 0, 1, 0, 0), 3) == expected

    def test_transition_remove_results_above_tolerance(self):
        p = Position(0, 1)
        assert p.transition((1, 0), 1) == [Position(1, 1)]
        assert p.transition((0, 0), 1) == []
        assert p.transition((), 1) == []

    def test_subsumes(self):
        p = Position(0, 0)

        assert p.subsumes(p)
        assert p.subsumes(Position(0, 1))
        assert p.subsumes(Position(1, 1))
        assert p.subsumes(Position(-1, 1))
        assert p.subsumes(Position(88, 88))

        assert not p.subsumes(Position(3, 2))
        assert not p.subsumes(Position(1, 0))

    def test_is_subsumed_by(self):
        p = Position(0, 1)

        assert p.is_subsumed_by(p)
        assert p.is_subsumed_by(Position(0, 0))
        assert p.is_subsumed_by(Position(1, 0))
        assert p.is_subsumed_by(Position(-1, 0))

        assert not p.is_subsumed_by(Position(2, 0))
        assert not p.is_subsumed_by(Position(-1, 1))
