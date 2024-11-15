import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass

@cmd_group.command("sin")
@click.option(
    "-n",
    "--number",
    default=1,
    help=".",
    show_default=True,  # show default in help
    type = int
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command("tan")
@click.option(
    "-n",
    "--number",
    default=1,
    help=".",
    show_default=True,  # show default in help
    type = int
)
def tan(number):
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    sin(10)