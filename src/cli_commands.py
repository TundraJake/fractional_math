import click
from ..src import frac_tests

@click.command()
@click.option('--run_tests', 
              help='Run all tests, ensuring this version of python (3.8.4) works.')
def run_all_tests():
    """Simple program that greets NAME for a total of COUNT times."""
    