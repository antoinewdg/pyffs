import tempfile
import atexit
import shutil
from os.path import dirname, join
from os import environ

GENERATED_DIR = join(dirname(__file__), 'generated')
MATRIX_FILE_NAMING = 'universal_automaton_%s.csv'
_temp_dir_generated = False

if environ.get('PYFFS_SETTINGS_MODE', 'release') == 'test':
    GENERATED_DIR = tempfile.mkdtemp()
    _temp_dir_generated = True


@atexit.register
def destroy_temp_dir():
    if _temp_dir_generated:
        shutil.rmtree(GENERATED_DIR)
