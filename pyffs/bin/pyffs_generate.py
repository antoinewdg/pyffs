import click

from pyffs.automaton_management import generate_automaton_to_file


@click.command()
@click.argument('tolerance', type=int)
def main(tolerance):
    generate_automaton_to_file(tolerance)


if __name__ == "__main__":
    main()
