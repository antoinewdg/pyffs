from os.path import join, isfile

from pyffs.settings import MATRIX_FILE_NAMING, GENERATED_DIR
from pyffs.core.universal_automaton import read_from_file


class Manager:
    def __init__(self, generated_dir=GENERATED_DIR):
        self._memoized = {}
        self.generated_dir = generated_dir

    def get_for_tolerance(self, tolerance):
        if tolerance not in self._memoized:
            self._memoized[tolerance] = self._load(tolerance)

        return self._memoized[tolerance]

    def _load(self, tolerance):
        filename = join(self.generated_dir, MATRIX_FILE_NAMING % tolerance)
        if not isfile(filename):
            raise Exception("Transitions matrices have not been generated")

        with open(filename, 'r') as file:
            return read_from_file(file)


manager = Manager()
