import click

from stores.nvidia import NvidiaBuyer


@click.group()
def main():
    pass


@click.command()
@click.option(
    "--gpu"
)
@click.option(
    "--locale"
)
@click.option("--test", is_flag=True)
@click.option("--headless", is_flag=True)
def nvidia(gpu, locale, test, headless):
    nv = NvidiaBuyer(gpu, locale, test, headless)
    nv.run_items()


main.add_command(nvidia)
