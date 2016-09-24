from pyffs.automaton_generation.parametrized_state import ParametrizedState, PositionSet, Position


class TestParametrizedState:
    def test_from_position_set(self):
        position_set = PositionSet(Position(1, 1), Position(2, 1))
        expected = ParametrizedState(Position(0, 1), Position(1, 1))

        param, result = ParametrizedState.from_position_set(position_set)
        assert param == 1
        assert result == expected

        position_set = PositionSet(Position(1, 1), Position(2, 1), Position(0, 1))
        expected = ParametrizedState(Position(1, 1), Position(2, 1), Position(0, 1))

        param, result = ParametrizedState.from_position_set(position_set)
        assert param == 0
        assert result == expected

    def test_transition(self):
        state = ParametrizedState(Position(0, 1), Position(1, 1))
        expected = ParametrizedState(Position(0, 2), Position(1, 2), Position(2, 2))

        param, actual = state.transition((0, 0, 0), 2)
        assert param == 0
        assert actual == expected

        param, actual = state.transition((0, 0, 0), 1)
        expected = ParametrizedState()
        assert param == 0
        assert actual == expected

        param, actual = state.transition((0, 1, 0), 2)
        expected = ParametrizedState(Position(2, 1), Position(0, 2))

        assert param == 0
        assert actual == expected

        param, actual = state.transition((1, 0, 0), 2)
        expected = ParametrizedState(Position(0, 1))
        assert param == 1
        assert actual == expected

    def test_generate_all_tolerance_1(self):
        generated = ParametrizedState.generate_all(1)
        expected = [
            ParametrizedState(),
            ParametrizedState(Position(0, 0)),
            ParametrizedState(Position(0, 1)),
            ParametrizedState(Position(0, 1), Position(1, 1)),
            ParametrizedState(Position(0, 1), Position(2, 1)),
            ParametrizedState(Position(0, 1), Position(1, 1), Position(2, 1)),
        ]

        assert generated == expected

    def test_generate_all_tolerance_2(self):
        generated = ParametrizedState.generate_all(2)
        expected = [
            ParametrizedState(),
            ParametrizedState(Position(0, 0)),
            ParametrizedState(Position(0, 1)),
            ParametrizedState(Position(0, 2)),
            ParametrizedState(Position(0, 1), Position(1, 1)),
            ParametrizedState(Position(0, 1), Position(2, 1)),
            ParametrizedState(Position(0, 1), Position(2, 2)),
            ParametrizedState(Position(0, 1), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(2, 1)),
            ParametrizedState(Position(0, 2), Position(3, 1)),
            ParametrizedState(Position(0, 2), Position(1, 2)),
            ParametrizedState(Position(0, 2), Position(2, 2)),
            ParametrizedState(Position(0, 2), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(4, 2)),
            ParametrizedState(Position(0, 1), Position(1, 1), Position(2, 1)),
            ParametrizedState(Position(0, 1), Position(1, 1), Position(3, 2)),
            ParametrizedState(Position(0, 1), Position(2, 2), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(2, 1), Position(3, 1)),
            ParametrizedState(Position(0, 2), Position(2, 1), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(3, 1), Position(1, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(2, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(2, 2), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(2, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(3, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(2, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(3, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(2, 2), Position(3, 2), Position(4, 2)),
            ParametrizedState(Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2), Position(4, 2)),
        ]

        assert generated == expected

    def test_generate_all_tolerance_3(self):
        generated = ParametrizedState.generate_all(3)
        assert len(generated) == 197

    def test_generate_all_tolerance_4(self):
        generated = ParametrizedState.generate_all(4)
        assert len(generated) == 1354
