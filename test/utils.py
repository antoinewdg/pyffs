import os
from os.path import join, dirname

from pyffs.settings import GENERATED_DIR


def clean_generated_dir():
    for file in os.listdir(GENERATED_DIR):
        path = os.path.join(GENERATED_DIR, file)
        if os.path.isfile(path):
            os.unlink(path)


def get_asset_file(name):
    return join(dirname(__file__), "assets", name)
