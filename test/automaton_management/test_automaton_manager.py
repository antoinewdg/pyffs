from time import time

import pytest

from pyffs.automaton_management import generate_automaton_to_file
from pyffs.automaton_management.automaton_manager import Manager
from test.utils import clean_generated_dir


class TestManager:
    def test_memoization_works(self):
        # The file need to be generated beforehand
        clean_generated_dir()
        generate_automaton_to_file(2)

        manager = Manager()
        t0 = time()
        manager.get_for_tolerance(2)
        first_time = time() - t0

        t0 = time()
        manager.get_for_tolerance(2)
        second_time = time() - t0

        assert first_time / second_time > 100
        clean_generated_dir()

    def test_exception_when_file_not_generated(self):
        clean_generated_dir()
        manager = Manager()

        with pytest.raises(Exception):
            manager.get_for_tolerance(2)
