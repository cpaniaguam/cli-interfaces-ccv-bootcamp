# Empower Your Code: Building an Easy-to-Use Command Line Interface from Scratch - Carlos Paniagua

## Motivation
Scientific computing often involves complex data processing tasks that require automation and reproducibility. Command-line interface (CLI) tools offer a powerful solution for streamlining such tasks, allowing researchers to efficiently manage and execute their code across different environments.

### Use Case
Imagine you have a large dataset generated from experiments stored in various formats. You need to preprocess this data, perform statistical analysis, and generate visualizations—all while ensuring the process is scalable and reproducible. A CLI tool can automate this pipeline, enabling you to effortlessly execute and manage your code on a computing cluster or even one-off computations. By transitioning from code entry points, such as Jupyter notebooks or regular scripts, to a CLI tool, you gain greater control, scalability, and reproducibility.

## Running your code - Entry Points

An *entry point* refers to the specific location within a program where the execution begins. It's the starting point from which the program's instructions are executed and control is transferred to the code defined at that location.


In Python, entry points can vary depending on how the program is designed and structured:

1. **Python Interpreter**: When executing a Python script or module directly from the command line, the entry point is typically the top-level code within the script or module.
    ```python
   # _0_motivation/_0_script.py
   # Entry point of the script at the top of the file
   from time import sleep

   print("Hello from", __name__) # look at this line for a moment. What's peculiar about it?
   print("This script does some serious work")

   t = input("How much work are we doing? ")
   amount_of_work = int(t)

   print("Doing some work...")

   for _ in range(amount_of_work):
      sleep(0.5)
      print(".", end="", flush=True)
   print("\nWork done!")
    ```

   Now from a Python session we can run the code in `_0_motivation/_0_script.py` file.

   ```python
   $ python
   >>> import _0_motivation._0_script
   Hello from _0_motivation._0_script
   This script does some serious work
   How much work are we doing? 2
   Doing some work...
   ..
   Work done!
   >>>
   ```

   Alternatively, the script can be executed more conveniently from the terminal.

   ```shell
   $ python _0_motivation._0_script.py
   Hello from __main__
   This script does some serious work
   How much work are we doing? 2
   Doing some work...
   ..
   Work done!
   ```

> [!Exercise]
> 1. What happens if no input is provided
> 2. What happens if `lots!` is passed as input?


   There are two potential issues with this approach:

   <ol type="a">
   <li>Error prone:  What if, by accident, bad input is provided?</li>
   <li>Scalability: What if the input data was in a file with thousands of values to process? What if, in turn, thousands of such files needed to be processed?</li>
   <li>No documentation for users: Prior knowledge of the behavior of the script is needed to use it correctly</li>
   </ol>

2. **Jupyter Notebooks**: Everybody (well, [almost](https://youtu.be/7jiPeIFXb6U?si=oB8s_jFoEH7jPs7O) everybody) loves Jupyter Notebooks for their versatility when exploring data, building visualizations, prototyping, and showcasing results. However, their structure may not be optimal for batch processing tasks where the same code needs to be applied across multiple datasets or inputs efficiently. Additionally, every cell in the notebook can serve as a potential entry point for code execution. While this flexibility allows for interactive exploration and experimentation, it can also lead to challenges in code organization and execution flow control.

Enter CLI applications!

## CLI Applications
For CLI tools, the entry point is often a designated function (traditionally `main`) or block of code responsible for parsing command-line arguments and triggering the appropriate actions based on those arguments.

### `sys.argv`

In the world of command-line interfaces (CLIs) in Python, `sys.argv` is the gateway to interacting with your Python scripts through the terminal. It's a list in Python that contains the command-line arguments passed to the script. Let's explore how `sys.argv` works in Python. Consider the following script

```python
# 01sysarv/01explore-sysarv.py

import sys

print(f'{sys.argv=}')
```

Run the command from your terminal
```bash
python 01sysarv/01explore-sysarv.py foo bar 1 123 a,b,c, path/to/a/file
```
You will see the following output:
```
sys.argv=['01sysarv/01explore-sysarv.py', 'foo', 'bar', '1', '123', 'a,b,c,', 'path/to/a/file']
```
It seems like Python collected the string of characters following the command and split it at the spaces. We can now use these metadata in our program and make it more flexible and extensible.

While `sys.argv` is a good starting point, it has limitations, especially when dealing with complex inputs or user interactions. Imagine passing multiple file paths, flags, or configuration options through the command line. Handling these inputs robustly and intuitively can quickly become unwieldy.

```python
# 00motivation/04script-small-only.py

import sys
from time import sleep

def main():
    # ISSUE: args are positional, need prior knowledge of the script
    script, bound, filepath = sys.argv[0], sys.argv[1], sys.argv[2]
    print(f'{script=}, {bound=}, {filepath=}')
    with open(filepath, 'r') as file:
        data = [int(line.rstrip('\n')) for line in file]

    print(f'Hello from {script}')
    print('We are going to do a lot of work now...')

    for t in data:
        # Small jobs only please
        if t < int(bound): # ISSUE: What if bound cannot be cast to int?
            print(f'Doing some work for {t} seconds...')
            sleep(t)

    print('Work done!')


if __name__ == '__main__':
    main() # this is the code's entry point when the script is run as a script from the command line

```


### `argparse`

To overcome the limitations of manually parsing `sys.argv`, Python provides the `argparse` module, a powerful tool for parsing command-line arguments in a structured and user-friendly manner. In `02argparse/00script-small-only-argparse.py` there is a refactored version of `00motivation/04script-small-only.py` using `argparse`.

#### Exercise
1. Run the script with the following command arguments and see what happens:
```bash
   python 02argparse/00script-small-only-argparse.py
```
```bash
   python 02argparse/00script-small-only-argparse.py --help
```
```bash
   python 02argparse/00script-small-only-argparse.py -h
```
2. Run the script with the following arguments and observe what happens:
```bash
   python 02argparse/00script-small-only-argparse.py -b 1
```
```bash
   python 02argparse/00script-small-only-argparse.py -f inputdata.dat
```
```bash
   python 02argparse/00script-small-only-argparse.py --bound 2 --file otherinputdata.dat
```
```bash
   python 02argparse/00script-small-only-argparse.py -b foo
```
```bash
   python 02argparse/00script-small-only-argparse.py -foo bar
```

As you can see, `argparse` handled all the bookkeeping for us, including adding documentation, enforcing correct usage, error reporting, default values, and argument parsing. This streamlined approach to command-line argument handling greatly simplifies script development and enhances user experience.

We will now look into some of the most useful and frequently used features of argparse below.

### Creating Commands

We can add further flexibility to our CLIs by creating custom commands within it. Consider the `02argparse/funcs.py` module; it contains a number of functions that compute numerical descriptors for numerical vectors/arrays. In the `02argparse/01commands.py` file there is a CLI that leverages all of these functions.

#### Exercise
1. Run the following commands and see what happens:
```bash
python 02argparse/01commands.py -h
```
```bash
python 02argparse/01commands.py mean 1 2 3
```
```bash
python 02argparse/01commands.py mean --nums 1 2 3
```
```bash
python 02argparse/01commands.py l2 --nums 1 2 3
```
```bash
python 02argparse/01commands.py median --nums 1 2 3
```
2. Modify the program to accept a list of numbers from a data file
3. Add a new command to the CLI (e.g. mode, median, variance, standard deviation, etc.)
4. Make the stat command an option instead of a positional argument

### Subparsers

In `02argparse/01commands.py` all commands shared the argument `nums`. Often, however, commands have different sets of arguments. In `02argparse/02subparser-commands.py` we refactor `02argparse/01commands.py` to add two new commands, `lp` and `nth`, which compute the _l-p_ norm and the _nth-ordered_ statistic of a numeric array, respectively. Note how the common arguments have been defined in the `parent_parser` object which is passed to each `subparser` (one per set of commands) object under the the `parent` argument. Look at the help page for the script with

```bash
python 02argparse/02subparser-commands.py --help
usage: 02subparser-commands.py [-h] {stat,lp,nth} ...

Compute statistics

options:
  -h, --help     show this help message and exit

commands:
  {stat,lp,nth}
    stat         Calculate: mean, geomean, max, min
    lp           Calculate the Lp norm
    nth          Calculate the nth ordered statistic
```

#### Exercise
1. Run the following commands and see what happens. `cd` into the `02argparse` directory first.
```bash
python 02subparser-commands.py stat --help
```
```bash
python 02subparser-commands.py lp --help
```
```bash
python 02subparser-commands.py nth --help
```
```bash
python 02subparser-commands.py stat mean --nums 1 2 3
```
```bash
python 02subparser-commands.py lp --nums 1 2 3
```
```bash
python 02subparser-commands.py lp -p 3 --nums 1 2 3
```
```bash
python 02argparse/02subparser-commands.py nth -n 3 --nums 1 2 3
```
2. Name some of the advantages of using commands in your CLIs (modularity, encapsulation, documentation, readability, consistency, extensibility, etc.)
3. Add a new command with argument to the CLI (e.g. `topn`, `bottomn`, etc.)
4. Modify the program to accept a list of numbers from a data file
5. Make the `stat` command an option instead of a positional argument

### Switches
Also known as flags or options, switches are used to toggle specific features, settings, or configurations within a CLI. They typically take the form of boolean flags where their presence or absence determines whether certain behavior is enabled or not. A common switch used in many CLIs is `-v` to allow more detailed output feedback during a program's runtime. In `02argparse/03flags.py` a `--verbose` option was added. The `action="store_true"` setting sets the value of `args.verbose` to `True` when invoked in the command line.

#### Exercise

1. Add a log switch to the CLI that will display the input arguments to stdout
2. Add a quiet switch to the CLI that will suppress all output to stdout
3. How would you handle the case where the user provides two or three of the log, verbose, and quiet switches?
