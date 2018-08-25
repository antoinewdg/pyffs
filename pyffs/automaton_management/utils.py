from pathlib import Path
from os.path import join

from pyffs.automaton_generation import generate_universal_automaton
from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING
from pyffs.core.universal_automaton import write_to_file


def generate_automaton_to_file(tolerance):
    automaton = generate_universal_automaton(tolerance)

    Path(GENERATED_DIR).mkdir(parents=True, exist_ok=True)
    filename = join(GENERATED_DIR, MATRIX_FILE_NAMING % tolerance)
    with open(filename, 'w+') as file:
        write_to_file(automaton, file)
