from os.path import join, isfile

from pyffs.automaton_generation import generate_universal_automaton
from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING
from pyffs.core.universal_automaton import write_to_file


def generate_automaton_to_file(tolerance, generated_dir=GENERATED_DIR, overwrite=True):
    automaton = generate_universal_automaton(tolerance)

    filename = join(generated_dir, MATRIX_FILE_NAMING % tolerance)

    if not overwrite and isfile(filename):
        return

    with open(filename, 'w') as file:
        write_to_file(automaton, file)
