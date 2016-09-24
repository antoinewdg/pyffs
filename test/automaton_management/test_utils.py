from os.path import join, isfile

from pyffs.settings import GENERATED_DIR
from pyffs.automaton_management.utils import generate_automaton_to_file
from test.utils import clean_generated_dir


def test_generate_automaton_to_file():
    path = join(GENERATED_DIR, "universal_automaton_0.csv")
    assert not isfile(path)
    generate_automaton_to_file(0)
    assert isfile(path)
    clean_generated_dir()
