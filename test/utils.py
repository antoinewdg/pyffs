from os.path import join, dirname


def get_asset_file(name):
    return join(dirname(__file__), "assets", name)
