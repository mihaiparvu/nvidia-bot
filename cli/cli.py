import click

from cli.utils import QuestionaryOption
from stores.nvidia import NvidiaBuyer, GPU_DISPLAY_NAMES, ACCEPTED_LOCALES


@click.group()
def main():
    pass


@click.command()
@click.option(
    "--gpu",
    type=click.Choice(GPU_DISPLAY_NAMES, case_sensitive=False),
    prompt="What GPU are you after?",
    cls=QuestionaryOption,
)
@click.option(
    "--locale",
    type=click.Choice(ACCEPTED_LOCALES, case_sensitive=False),
    prompt="What locale shall we use?",
    cls=QuestionaryOption,
)
def nvidia(gpu, locale):
    nv = NvidiaBuyer(gpu, locale)
    nv.run_items()


main.add_command(nvidia)
