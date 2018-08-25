from pathlib import Path

from pyffs.automaton_generation import generate_universal_automaton
from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING
from pyffs.core.universal_automaton import write_to_file


def generate_automaton_to_file(tolerance, overwrite_existing=False):
    generated_dir = Path(GENERATED_DIR)
    filename = generated_dir / (MATRIX_FILE_NAMING % tolerance)
    if not filename.exists() or overwrite_existing:
        generated_dir.mkdir(parents=True, exist_ok=True)
        with open(str(filename), 'w+') as file:
            automaton = generate_universal_automaton(tolerance)
            write_to_file(automaton, file)
