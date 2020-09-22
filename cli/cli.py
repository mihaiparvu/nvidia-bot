import click

from stores.nvidia import NvidiaBuyer, GPU_DISPLAY_NAMES, ACCEPTED_LOCALES


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
def nvidia(gpu, locale):
    nv = NvidiaBuyer(gpu, locale)
    nv.run_items()


main.add_command(nvidia)
