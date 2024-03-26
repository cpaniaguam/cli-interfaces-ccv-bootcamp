# Empower Your Code: Building an Easy-to-Use Command Line Interface from Scratch - Carlos Paniagua

## Motivation
Scientific computing often involves complex data processing tasks that require automation and reproducibility. Command-line interface (CLI) tools offer a powerful solution for streamlining such tasks, allowing researchers to efficiently manage and execute their code across different environments.

### Use Case
Imagine you have a large dataset generated from experiments stored in various formats. You need to preprocess this data, perform statistical analysis, and generate visualizations—all while ensuring the process is scalable and reproducible. A CLI tool can automate this pipeline, enabling you to effortlessly execute and manage your code on a computing cluster or even one-off computations. By transitioning from code entry points, such as Jupyter notebooks, to a CLI tool, you gain greater control, scalability, and reproducibility.

## Running your code - Entry Points

An *entry point* refers to the specific location within a program where the execution begins. It's the starting point from which the program's instructions are executed and control is transferred to the code defined at that location.

For command-line applications or scripts, the entry point is typically the main function or block of code responsible for handling command-line arguments, initializing the program, and executing its core functionality.

In Python, entry points can vary depending on how the program is designed and structured:

1. Python Interpreter: When executing a Python script or module directly from the command line, the entry point is typically the top-level code within the script or module.
    ```python
    # script.py
    from time import sleep

    print('hello from script')
    print('This script does some serious work')
    print('Doing some work...')
    sleep(2)
    print('Work done!')
    ```
    Now from a Python session we can run `script.py`.
    ```python
    >>> import script
    ```

    Alternatively, the script can be executed more conveniently from the terminal.

    ```shell
    $ python script.py 
    hello from script
    This script does some serious work
    Doing some work...
    Work done!
    $
    ```

    Often external data is needed. We could provide this data by hand using, for example, the `input` function.

    ```python
    # script-with-arg.py

    from time import sleep

    print('hello from script')
    print('This script does some serious work')

    t = input('How much work are we doing? ')

    print('Doing some work...')
    sleep(int(t))

    print('Work done!')
    ```

There are two potential issues with this approach:

<ol type="a">
  <li>Error prone:  What if, by accident, bad input is provided?</li>
  <li>Scalability: What if the input data was in a file with thousands of values to process? What if, in turn, thousands of such files needed to be processed?</li>
</ol>

Enter CLI applications!

## CLI Applications
For CLI tools, the entry point is often a designated function (traditionally `main`) or block of code responsible for parsing command-line arguments and triggering the appropriate actions based on those arguments.