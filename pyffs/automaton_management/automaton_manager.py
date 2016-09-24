from os.path import join, isfile

from pyffs.settings import MATRIX_FILE_NAMING, GENERATED_DIR
from pyffs.core.universal_automaton import read_from_file


def _load(tolerance):
    filename = join(GENERATED_DIR, MATRIX_FILE_NAMING % tolerance)
    if not isfile(filename):
        raise Exception("Transitions matrices have not been generated")

    with open(filename, 'r') as file:
        return read_from_file(file)


class Manager:
    def __init__(self):
        self._memoized = {}

    def get_for_tolerance(self, tolerance):
        if tolerance not in self._memoized:
            self._memoized[tolerance] = _load(tolerance)

        return self._memoized[tolerance]


manager = Manager()
