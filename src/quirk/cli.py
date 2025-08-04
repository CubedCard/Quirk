import typer

from .quirk import quirk 


app = typer.Typer()
app.command()(quirk)


if __name__ == "__main__":
    app()
