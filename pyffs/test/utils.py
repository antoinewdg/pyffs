import os

from pyffs.settings import GENERATED_DIR


def clean_generated_dir():
    for file in os.listdir(GENERATED_DIR):
        path = os.path.join(GENERATED_DIR, file)
        if os.path.isfile(path):
            os.unlink(path)
