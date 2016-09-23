from os.path import join, isfile

from pyffs.settings import MATRIX_FILE_NAMING, GENERATED_DIR

from .utils import read_matrix_from_file


def _load_matrix(tolerance):
    filename = join(GENERATED_DIR, MATRIX_FILE_NAMING % tolerance)
    if not isfile(filename):
        raise Exception("Transitions matrices have not been generated")

    with open(filename, 'r') as file:
        return read_matrix_from_file(file)


class Manager:
    def __init__(self):
        self._matrices = {}

    def get_for_tolerance(self, tolerance):
        if tolerance not in self._matrices:
            self._matrices[tolerance] = _load_matrix(tolerance)

        return self._matrices[tolerance]


transition_matrix_manager = Manager()
