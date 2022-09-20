# Iterative Exponentiation

TODO: Make sure that you completely delete all of the TODO markers and sentences
inside of this document. After you are finished writing all of the answer in
your reflection it should have a professional format and be ready for
publication on your own web site.

## Add Your Name Here

## Program Output

### What is the output from running the `iterator` program?

TODO: Use a fenced code block to provide the output for your this command for running the `iterator`.

- `poetry run iterator --whileloop --forloop --minimum 2 --maximum 10`

TODO: Use a fenced code block to provide the output for your this command for running the `iterator`.

- `poetry run iterator --forloop --minimum 0 --maximum 5`

TODO: Use a fenced code block to provide the output for your this command for running the `iterator`.

- `poetry run iterator --whileloop --minimum 2 --maximum 10`

### What is the output from running the test suite for the `iterator` program?

TODO: Use a fenced code block to provide the output from running the test suite

## Source Code and Configuration Files

### Describe in detail how the provided source code works

#### How does the following source code segment define the command-line interface for `iterator`?

TODO: Write at least one paragraph to explain the source code

```
def main(
    forloop: bool = typer.Option(False, "--forloop"),
    whileloop: bool = typer.Option(False, "--whileloop"),
    minimum: int = typer.Option(1, min=0, max=100),
    maximum: int = typer.Option(5, min=0, max=100),
):
```

#### What is the purpose of the following function in the context of the `iterator` program?

```
def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "Yes"
    return "No"
```

## Professional Reflection

### What do you find most challenging about implementing and testing Python programs? Why?

TODO: Provide a one-paragraph response that answers this question in your own words.

### In your view, what does it mean to be an ethical Python programmer?

TODO: Provide a one-paragraph response that answers this question in your own words.

### After completing this assignment, what is one experience for which you are grateful?

TODO: Provide a one-paragraph response that answers this question in your own words.
