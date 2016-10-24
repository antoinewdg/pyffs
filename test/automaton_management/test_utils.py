import tempfile
from os.path import join, isfile

from pyffs.automaton_management.utils import generate_automaton_to_file


def test_generate_automaton_to_file():
    tmp_dir = tempfile.TemporaryDirectory()
    path = join(tmp_dir.name, "universal_automaton_0.csv")
    assert not isfile(path)
    generate_automaton_to_file(0, tmp_dir.name)
    assert isfile(path)
