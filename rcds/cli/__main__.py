import click

from .deploy import deploy, test


@click.group()
def cli():
    pass


cli.add_command(deploy)
cli.add_command(test)

if __name__ == "__main__":
    cli()
