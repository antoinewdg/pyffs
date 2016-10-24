import tempfile
from time import time

import pytest

from pyffs.automaton_management import generate_automaton_to_file
from pyffs.automaton_management.automaton_manager import Manager


class TestManager:
    def test_memoization_works(self):
        manager = Manager()
        t0 = time()
        manager.get_for_tolerance(2)
        first_time = time() - t0

        t0 = time()
        manager.get_for_tolerance(2)
        second_time = time() - t0

        assert first_time / second_time > 100

    def test_exception_when_file_not_generated(self):
        temp_dir = tempfile.TemporaryDirectory()
        manager = Manager(temp_dir.name)

        with pytest.raises(Exception):
            manager.get_for_tolerance(2)

        generate_automaton_to_file(2, temp_dir.name)
        manager.get_for_tolerance(2)
