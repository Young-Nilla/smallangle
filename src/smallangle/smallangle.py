import click
import numpy as np
from numpy import pi
import pandas as pd


# Create a Click group to organize related commands
@click.group()
def smallangle():
    pass

# Define the 'sin' command
@smallangle.command("sin")
@click.option(
    "-n",
    "--number",
    default=5, # Default value for the number of points
    help="The number of points to calculate within the range [0, 2π].",
    show_default=True, # show default in help
    type = int # Ensure the input is an interger
)
def sin(number):
    """
    This command generates 'number' within the range [0, 2π]
    and calculates their sine values. The result are displayed as a table.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

# Define the 'tan' command
@smallangle.command("tan")
@click.option(
    "-n",
    "--number",
    default=5, # Default value for the number of points
    help="The number of points to calculate within the range [0, 2π].",
    show_default=True,  # show default in help
    type = int # Ensure the input is an interger
)
def tan(number):
    """
    This command generates 'number' within the range [0, 2π]
    and calculates their tangent values. The result are displayed as a table.
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

# Entry point for the script
if __name__ == "__main__":
    smallangle()