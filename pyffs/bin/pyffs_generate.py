import click

from pyffs.automaton_management import generate_automaton_to_file


@click.command()
@click.argument('tolerances', type=int, nargs=-1)
def main(tolerances):
    for tolerance in tolerances:
        generate_automaton_to_file(tolerance)


if __name__ == "__main__":
    main()
