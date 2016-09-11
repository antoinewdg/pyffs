from pyffs.automaton_generation import ParametrizedState, PositionSet, Position


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
