from functools import wraps
from typing import Optional

import typer
from typing_extensions import Annotated

from . import decode, encode

app = typer.Typer(
    name='Caesar Cipher',
    no_args_is_help=True,
)
__version__ = '0.1.1'


def version(value: bool):
    if value:
        print(app.info.name, __version__)
        raise typer.Exit()


@app.callback()
def callback(
    version: Annotated[
        Optional[bool],
        typer.Option(
            '--version', callback=version, help='Show the CLI app version.'
        ),
    ] = None
) -> None:  # pragma: no cover
    ...


def on_stdout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


app.command(no_args_is_help=True)(on_stdout(encode))
app.command(no_args_is_help=True)(on_stdout(decode))
