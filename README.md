# Iterative Exponentiation

## Assigned: Tuesday, September 20, 2022

## Due: Tuesday, September 27, 2022

## Project Goals

This engineering effort invites you to combine what you learned about the basics of Python programming to implement a program that can use a `for` loop and/or a `while` loop to perform a series of exponentiations (i.e., raising a value to some defined power).

The function that you will implement will repeatedly perform an exponentiation and then save the result of the computation in the list. Ultimately, the output of the program should confirm that it is possible to use either a `for` loop or a `while` loop to produce the same program output.

As you learn more about how to translate mathematical equations into Python functions, you will implement and test a complete Python program while using tools such as the VS Code text editor, a terminal window, and the Poetry package manager.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in the course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Expected Output

This project invites you to implement a program called `iterator`. The program has two flags called `--forloop` and `--whileloop` that control the type of iteration construct with which the program performs iterative exponentiation. To best understand the program's behavior it is nice to observe how it operates when given different command-line arguments. For instance, the command `poetry run iterator --forloop --whileloop --minimum 0 --maximum 2` produces the following output. 

```
Calculating the powers of 2 from 0 to 2 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? Yes

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2

  Here is the output with the while loop.

   2**0 = 1
   2**1 = 2

Wow, all of that iteration was exhausting! 😂
```
Can you see the pattern? Please note that the use of both the flags `--forloop` and `--whileloop` means that the program will iteratively compute the powers of two with both a `for` and `while` loop.

It is important to note that the Python program can also produce the output of the powers of two using a single type of iteration construct. For instance, the command `poetry run iterator --forloop --minimum 0 --maximum 5` produces the following output demonstrating that the program only ran a `for` loop. As in the previous output example, this output shows that the program uses the `**` operator to raise `2` to the power of a number such as `0`, `1`, and `2`. Both of these output examples also show that the program should contain several lines of diagnostic output that make it clear how it interpreted the command-line arguments. This output should be made before performing iterative exponentiation.

```
Calculating the powers of 2 from 0 to 5 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16

Wow, all of that iteration was exhausting! 😂
```

While all of the prior examples show that the `iterator` works when you use `0` as the value for the `--minimum`, it is also important to point out that it should work when you increase the value for this parameter. For instance, when you run `poetry run iterator --forloop --minimum 2 --maximum 10` it should produce the following output. 
```
Calculating the powers of 2 from 2 to 10 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**2 = 4
   2**3 = 8
   2**4 = 16
   2**5 = 32
   2**6 = 64
   2**7 = 128
   2**8 = 256
   2**9 = 512

Wow, all of that iteration was exhausting! 😂
```

Note that this output shows that the first exponentiation that the `iterator` performs is `2**2 = 4` instead of starting with `2**0 = 1` as was the case in the previous runs.


```
Remember, if you want to run `iterator` you must use your terminal to go into the GitHub repository containing this project and then go into the `iterator` directory that contains the project's source code. Finally, remember that before running the program you must run `poetry install` to add the dependencies. If you run into errors when using a `poetry run` command you can often resolve them by deleting the `.venv` directry and the `poetry.lock` file and then trying `poetry install` again.
```

## Adding Functionality

If you study the file `iterator/iterator/main.py` you will see that it has many `TODO` markers that designate the parts of the program that you need to implement before `iterator` will produce the correct output. If you run the program before adding all of the source code required by the `TODO` markers then `iterator` will neither produce the correct output or pass the test suite. Ultimately, you are invited to add the required functionality to the functions that have the following signatures.

- Functions in the `display` module:

  - `def convert_bool_to_answer(argument: bool)`
  - `def display_list(values: List, indent="")`

- Functions in the `iterate` module:

  - `def calculate_powers_of_two_for_loop(minimum: int, maximum: int)`
  - `def calculate_powers_of_two_while_loop(minimum: int, maximum: int)`

It is important to note that you should not change the signature of these functions in your own implementation unless you receive prior approval from the course instructor.

When you are finished implementing both of the iterative approaches, please take time to evaluate each of them, comparing and contrasting their syntactic structure. Which one do you think is easier to understand? Why? Can you develop any good rules of thumb that suggest when it is better to use one type of loop over the other loop type?

Finally, the following source code segment shows how the `main` module should implement the Python source code that calls the `calculate_powers_of_two_for_loop` and `calculate_powers_of_two_while_loop` functions. Lines `1` and `7` of this source code segment ensure that the correct function in the `iterate` module is called. Next, lines `2` and `3` and `8` and `9` produce the correct labels that will appear in the console output. Finally, lines `4` and `10` call the correct iteration function depending on the command-line arguments specified by the person running the program. Once either the `calculate_powers_of_two_for_loop` or `calculate_powers_of_two_while_loop` function returns a list of values, the `display` function will show the contents of that list with the amount of indentation specified in the string constant.

```python
if forloop is True:
    typer.echo("  Here is the output with the for loop.")
    typer.echo("")
    forloop_list = iterate.calculate_powers_of_two_for_loop(minimum, maximum)
    display.display_list(forloop_list, "   ")
    typer.echo("")
if whileloop is True:
    typer.echo("  Here is the output with the while loop.")
    typer.echo("")
    whileloop_list = iterate.calculate_powers_of_two_while_loop(minimum, maximum)
    display.display_list(whileloop_list, "   ")
    typer.echo("")
````

## Running Checks

As you continue to add and confirm the correctness of the funtionality of the `iterator`, you also study the source code in the `pyproject.toml` file. This file contains the specification of several tasks that will help you to easily run checks on your Python source code. Now, you can run commands like `poetry run task lint` to automatically run all of the linters designed to check the Python source code in your program and its test suite.

You can also use the command `poetry run task black` to confirm that your source code adheres to the industry-standard format defined by the `black` tool. If it does not adhere to the standard then you can run the command `poetry run black iterator tests` and it will automatically reformat the source code. By following a [tutorial](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0), you can also configure your VS Code text editor to use the `black` tool to automatically reformat you source code every time you save a file.

```toml
[tool.taskipy.tasks]
black = { cmd = "black iterator tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 iterator tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy iterator", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle iterator tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint iterator tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
````

Along with running tasks like `poetry run task lint`, you run `gatorgrade --config config/gatorgrade.yml` command to check your work. If `gatorgrade --config config/gatorgrade.yml` shows that all checks pass, you will know that you made progress towards correctly implementing and writing about `iterator`. If your program has all of the anticipated functionality, you can run the command `poetry run task test` and see that the test suite passes correctly if you have the correct implementation of the function(s) that it tests.

### Note

Do not forget that when you commit source code or technical writing to your GitHub repository for this project, it will trigger the run of a GitHub Actions workflow. If you are a student at Allegheny College, then running this workflow consumes build minutes for the organization of the course!

As such, we ask that you only commit to your repository once you have made substantive changes to your project and you are ready to confirm its correctness. Before you commit to your repository, you can still run checks on your own computer by either using Poetry or Docker and GatorGrader.

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and used, and answer all of the other questions about your experiences in completing this project.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.