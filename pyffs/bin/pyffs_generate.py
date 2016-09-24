import sys
from os.path import dirname, join

import click

from pyffs.automaton_generation import generate_transition_matrix
from pyffs.transition_matrix import save_matrix_to_file
from pyffs.settings import GENERATED_DIR, MATRIX_FILE_NAMING


@click.command()
@click.argument('tolerance', type=int)
def main(tolerance):
    matrix, bit_vectors, n_states = generate_transition_matrix(tolerance)

    filename = join(GENERATED_DIR, MATRIX_FILE_NAMING % tolerance)
    with open(filename, 'w+') as file:
        save_matrix_to_file(matrix, file, bit_vectors, n_states)


if __name__ == "__main__":
    main()
