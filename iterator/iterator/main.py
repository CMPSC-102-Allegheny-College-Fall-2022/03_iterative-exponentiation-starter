"""Define the command-line interface for the iterator program."""

import typer

from iterator import display
from iterator import iterate

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(
    forloop: bool = typer.Option(False, "--forloop"),
    whileloop: bool = typer.Option(False, "--whileloop"),
    minimum: int = typer.Option(1, min=0, max=100),
    maximum: int = typer.Option(5, min=0, max=100),
):
    """Calculate the powers of 2 from 0 to 20 using iteration constructs."""
    # display the debugging output for the program's command-line arguments
    typer.echo(
        f"Calculating the powers of 2 from {minimum} to {maximum} with iteration:"
    )
    typer.echo("")
    typer.echo(f"  Should I use a for loop? {display.convert_bool_to_answer(forloop)}")
    typer.echo(
        f"  Should I use a while loop? {display.convert_bool_to_answer(whileloop)}"
    )
    typer.echo("")
    # compute the powers of 2 using a function in the iterate module that uses a for loop
    if forloop is True:
        typer.echo("  Here is the output with the for loop.")
        typer.echo("")
        forloop_list = iterate.calculate_powers_of_two_for_loop(minimum, maximum)
        display.display_list(forloop_list, "   ")
        typer.echo("")
    # compute the powers of 2 using a function in the iterate module that uses a while loop
    if whileloop is True:
        typer.echo("  Here is the output with the while loop.")
        typer.echo("")
        whileloop_list = iterate.calculate_powers_of_two_while_loop(minimum, maximum)
        display.display_list(whileloop_list, "   ")
        typer.echo("")
    # display a final message and some extra spacing
    typer.echo("Wow, all of that iteration was exhausting! 😂")
    typer.echo("")
