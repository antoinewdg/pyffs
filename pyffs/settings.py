import tempfile
from os.path import dirname, join
from os import environ

GENERATED_DIR = join(dirname(__file__), 'generated')
MATRIX_FILE_NAMING = 'universal_automaton_%s.csv'

if environ.get('PYFFS_SETTINGS_MODE', 'release') == 'test':
    temp_dir = tempfile.TemporaryDirectory()
    GENERATED_DIR = temp_dir.name
