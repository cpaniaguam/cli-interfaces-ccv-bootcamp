# Empower Your Code: Building an Easy-to-Use Command Line Interface from Scratch - Carlos Paniagua

## Motivation
Scientific computing often involves complex data processing tasks that require automation and reproducibility. Command-line interface (CLI) tools offer a powerful solution for streamlining such tasks, allowing researchers to efficiently manage and execute their code across different environments.

### Use Case
Imagine you have a large dataset generated from experiments stored in various formats. You need to preprocess this data, perform statistical analysis, and generate visualizations—all while ensuring the process is scalable and reproducible. A CLI tool can automate this pipeline, enabling you to effortlessly execute and manage your code on a computing cluster or even one-off computations. By transitioning from code entry points, such as Jupyter notebooks or regular scripts, to a CLI tool, you gain greater control and scalability.

## Running your code - Entry Points

An *entry point* refers to the specific location within a program where the execution begins. It's the starting point from which the program's instructions are executed and control is transferred to the code defined at that location.


In the Python ecosystem, entry points can vary depending on how the program is designed and structured:

1. **Python Interpreter**
   When executing a Python script or module directly from the command line, the entry point is typically the top-level code within the script or module.
      ```python
      # _0_motivation/_0_script.py
      """
      This script does some serious work
      """

      # Entry point of the script at the top of the file
      from time import sleep

      print("Hello from", __name__) # look at this line for a moment. What's peculiar about it?
      print(__doc__) # How about this one?

      t = input("How much work are we doing? ")
      amount_of_work = int(t)

      print("Doing some work...")

      for _ in range(amount_of_work):
         sleep(0.5)
         print(".", end="", flush=True)
      print("\nWork done!")
      ```

      Now from a Python session we can run the code in the `_0_motivation/_0_script.py` file.

      ```python
      $ python -q
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
      $ python _0_motivation/_0_script.py
      Hello from __main__

      This script does some serious work

      How much work are we doing? 2
      Doing some work...
      ..
      Work done!
      ```

      **Exercise**
         - What happens if `lots!` is passed as input?

         - What's the deal with the `__name__` and `__doc__` variables?


2. **Jupyter Notebooks**
   Everybody (well, [almost](https://youtu.be/7jiPeIFXb6U?si=oB8s_jFoEH7jPs7O) everybody) loves Jupyter Notebooks for their versatility when exploring data, building visualizations, prototyping, and showcasing results. However, their structure may not be optimal for batch processing tasks where the same code needs to be applied across multiple datasets or inputs efficiently. Additionally, every cell in the notebook can serve as a potential entry point for code execution. While this flexibility allows for interactive exploration and experimentation, it can also lead to challenges in code organization and execution flow control.

As you probably have realized, there are several potential issues with these approaches:

   <ol type="a">
   <li>Error prone:  What if, by accident, bad or no input is provided?</li>
   <li>Scalability: What if the input data was in a file with thousands of values to process? What if, in turn, thousands of such files needed to be processed?</li>
   <li>Flexibility: What if each data set required its own set of input metadata?</li>
   <li>No documentation for users: Prior knowledge of the behavior of the script/notebook is needed to use it correctly</li>
   </ol>


Enter CLI applications!

## CLI Applications
For CLI tools, the entry point is often a designated function (traditionally `main`) or block of code in a module (file) responsible for parsing command-line arguments and triggering the appropriate actions based on those arguments. In `_0_motivation/_1_script-with-custom-entry-point.py` we refactor our original script into a main function with a custom entry point.


   ```python
   # _0_motivation/_1_script-with-custom-entry-point.py

   from time import sleep

   def main():
      print("hello from script")
      print("This script does some serious work")

      t = input("How much work are we doing? ")
      amount_of_work = int(t)

      print("Doing some work...")

      for _ in range(amount_of_work):
         sleep(0.5)
         print(".", end="", flush=True)
      print("\nWork done!")


   if __name__ == "__main__":
      # This is the entry point of the script
      main()
   ```

### `sys.argv`

In the world of Python CLIs, `sys.argv` is the gateway to interacting with your Python scripts through the terminal. This is a Python list that contains the command-line arguments passed to the script. Let's explore how `sys.argv` works in Python. Consider the following simple script

```python
# _1_sysarv/_1_explore-sysarv.py

import sys

print(f'{sys.argv=}')

```

Now run this command from your terminal:
```bash
python _1_sysarv/_1_explore-sysarv.py
```
```bash
python _1_sysarv/_1_explore-sysarv.py foo --bar 1 123 a,b,c, path/to/a/file
```
You will see the following output:
```
sys.argv=['_1_sysarv/_1_explore-sysarv.py']
```
```
sys.argv=['_1_sysarv/_1_explore-sysarv.py', 'foo', 'bar', '1', '123', 'a,b,c,', 'path/to/a/file']
```
It seems like Python collected the string of characters following the command executable and split it at the spaces. We can now use these metadata in our program and make it more flexible and extensible.


**Exercise**

   Consider the `_1_sysarv/_2_script.py` script, which is a refactored version of `_0_motivation/_0_script.py`.

   ```python
   # _1_sysarv/_2_script.py
   """
   This script does some serious work
   """

   import sys
   from time import sleep

   def do_work(t):
      sleep(t)

   def main():
      # ISSUE: args are positional, need prior knowledge of the script for correct use
      script, bound, filepath = sys.argv # ISSUE: What if there are not enough or extra arguments?
      print(__doc__)
      print(f'{script=}, {bound=}, {filepath=}')


      # Read the data from file
      with open(filepath, 'r') as file:
         data = [int(line.rstrip('\n')) for line in file]

      print(f'Hello from {script}')
      print('We are going to do a lot of work now...')

      for t in data:
         # Small jobs only please
         if t < int(bound): # ISSUE: What if bound cannot be cast to int?
               print(f'Doing some work for {t} seconds...')
               do_work(t)

      print('Work done!')


   if __name__ == '__main__':
      main() # this is the code's entry point when the script is run from the command line
   ```

   Now run the script with the following command arguments and see what happens:
   ```bash
      python _1_sysarv/_2_script.py
   ```
   ```bash
      python _1_sysarv/_2_script.py 2
   ```
   ```bash
      python _1_sysarv/_2_script.py inputdata.dat
   ```
   ```bash
      python _1_sysarv/_2_script.py 2 inputdata.dat
   ```
   ```bash
      python _1_sysarv/_2_script.py inputdata.dat 2
   ```
   ```bash
      python _1_sysarv/_2_script.py 2 inputdata.dat foo
   ```

While `sys.argv` is a good starting point, it has limitations, especially when dealing with complex inputs or user interactions. Imagine passing multiple file paths, flags, or configuration options through the command line. Handling these inputs robustly and intuitively can quickly become unwieldy. Enter `argparse`!

### `argparse`

To overcome the limitations of manually parsing `sys.argv`, Python provides the `argparse` module, a powerful tool for parsing command-line arguments in a structured and user-friendly manner. In `_2_argparse/_1_script.py` there is a refactored version of `_1_sysarv/_2_script.py` using `argparse`.

 **Exercise**
   1. Keeping in mind the issues `_1_sysarv/_2_script.py` has, run `_2_argparse/_1_script.py` with the following command arguments and see what happens:
   ```bash
      python _2_argparse/_1_script.py --help
   ```
   ```bash
      python _2_argparse/_1_script.py -h
   ```
   ```bash
      python _2_argparse/_1_script.py
   ```
   2. Run the script with the following arguments and observe what happens:
   ```bash
      python _2_argparse/_1_script.py -b 1
   ```
   ```bash
      python _2_argparse/_1_script.py -f inputdata.dat
   ```
   ```bash
      python _2_argparse/_1_script.py --bound 2 --file otherinputdata.dat
   ```
   ```bash
      python _2_argparse/_1_script.py -b foo
   ```
   ```bash
      python _2_argparse/_1_script.py --foo bar
   ```

As you can see, `argparse` handled all the bookkeeping for us, including adding documentation, enforcing correct usage, error reporting, default values, and correct argument parsing. This streamlined approach to command-line argument handling greatly simplifies script development and enhances user experience.

We will now look into some of the most useful and frequently used features of `argparse` below.

### Creating Commands and Options

We can add further flexibility to our CLIs by creating custom commands.

Consider the `_2_argparse/funcs.py` module; it contains various functions that compute numerical descriptors for numerical vectors/arrays. In the `_2_argparse/_2_commands.py` file there is a CLI that leverages all of these functions using *positional* and *optional* (also referred as keyword or named) arguments.

Positional arguments are mandatory and their order matters. They are identified by their position in the command line input, rather than by a specific keyword or option string. On the other hand, arguments that are prefixed with one or two `-` are optional (unless specified with `required=True`), and they can be specified in any order.

#### Exercise
1. Run the following commands and see what happens:
```bash
python _2_argparse/_2_commands.py -h
```
```bash
python _2_argparse/_2_commands.py mean 1 2 3
```
```bash
python _2_argparse/_2_commands.py mean --nums 1 2 3
```
```bash
python _2_argparse/_2_commands.py l2 --nums 1 2 3
```
```bash
python _2_argparse/_2_commands.py l2 --nums 1 2 foo
```
```bash
python _2_argparse/_2_commands.py median --nums 1 2 3
```
```bash
python _2_argparse/_2_commands.py --foo 1 2 3
```bash
python _2_argparse/_2_commands.py mean  --numbers 1 2 3 > result.txt
```
```bash
python _2_argparse/_2_commands.py 1st --help
```
Play time! Choose one of the following activities to do right now.

   2. What happens if `nargs` is set to `1` instead of `"+"` or deleted?
   4. Add a new command to the CLI (e.g. mode, median, variance, standard deviation, etc.)
   5. Make the stat command an option instead of a positional argument
   3. Modify the program to accept a list of numbers from a data file

### Subparsers

In `_2_argparse/_2_commands.py` all commands shared the argument `nums`. Often, however, it's useful for commands to have different sets of arguments, different sets of options, or their particular documentation. In `_2_argparse/_3_subparser-commands.py` we refactor `_2_argparse/_2_commands.py` to add two new commands, `lp` and `kth`, which compute the _l-p_ norm and the _kth-order_ statistic of a numeric array, respectively. Note how the common arguments have been defined in the `parent_parser` object which is passed to each `subparser` (one per set of commands) object under the the `parent` argument. Look at the help page for the script with

```bash
python _2_argparse/_3_subparser-commands.py --help
usage: _3_subparser-commands.py [-h] {mean,kth,lp} ...

Compute statistics on a list of numbers

options:
  -h, --help     show this help message and exit

commands:
  {mean,kth,lp}
    mean         compute the arithmetic mean of a list of numbers
    kth          compute the kth ordered statistic of a list of numbers
    lp           compute the lp norm of a list of numbers

Example: python _3_subparser-commands.py lp -p 2 -n 1 2 3 4 5
```

#### Exercise
1. Run the following commands and see what happens. `cd` into the `_2_argparse` directory first.
```bash
python _3_subparser-commands.py mean --help
```
```bash
python _3_subparser-commands.py lp --help
```
```bash
python _3_subparser-commands.py kth --help
```
```bash
python _3_subparser-commands.py mean --nums 1 2 3
```
```bash
python _3_subparser-commands.py lp --nums 1 2 3
```
```bash
python _3_subparser-commands.py lp -p=2 --nums 1 2 3
```
```bash
python _3_subparser-commands.py kth -k 3 --nums 1 2 3
```
2. Name some of the advantages of using commands in your CLIs (modularity, encapsulation, documentation, readability, consistency, extensibility, etc.)
3. Add a new parameter-free command to the CLI (e.g. `geomean`, `max`, etc.)
4. How would you add a feature to the CLI so that the program accepts a list of numbers from a data file
5. How would you make adding a new command to the CLI easier.

### Switches
Also known as flags or options, switches are used to toggle specific features, settings, or configurations within a CLI. They typically take the form of boolean flags where their presence or absence determines whether certain behavior is enabled or not. A common switch used in many CLIs is `-v` to allow more detailed output feedback during a program's runtime. In `_2_argparse/_4_flags.py` a `--verbose` option was added to the parent parser. The `action="store_true"` setting sets the value of `args.verbose` to `True` when invoked in the command line.

#### Exercise


1. Again from the `_2_argparse` directory, run the following commands and see what happens.
   ```bash
   python _4_flags.py kth -k 3 --nums 1 2 3
   ```
   ```bash
   python _4_flags.py kth -k 3 --nums 1 2 3 --verbose
   ```


1. Add a log switch to the CLI that will display the input arguments to stdout
2. Add a quiet switch to the CLI that will suppress all output to stdout
3. How would you handle the case where the user provides two or three of the log, verbose, and quiet switches?

## Higher-level Frameworks

`argparse`, as we have seen, is a robust framework for building command-line interfaces (CLIs) with extensive functionality and flexibility. However,  there are other higher-level frameworks for building CLIs within the Python ecosystem. One of them is `Typer`, which presents a compelling evolution in CLI development, offering a more streamlined and perhaps more *Pythonic* approach.

Leveraging Python's type annotations, Typer eliminates much of the boilerplate associated with argument parsing, automatically inferring types and generating CLI interfaces from function signatures. This simplifies the development process, allowing developers to focus more on application logic rather than parsing intricacies. Typer can also seamlessly integrate with Python's async capabilities, making it an ideal choice for building modern CLI applications.

In this brief section, we explore a few of the [many capabilities of `typer`](https://typer.tiangolo.com/features/). Consider the `_3_higher-level-frameworks/typerapp.py` script. After creating a `typer.Typer` instance, `app`, we add commands to it  using the `command` *decorator*.

### Exercise

   1. `From the `_3_higher_level_frameworks` directory, run the following commands and see what happens.
      ```bash
      python typerapp.py
      ```
      ```bash
      python typerapp.py -h
      ```
      ```bash
      python typerapp.py --help
      ```
      ```bash
      python typerapp.py mean --help
      ```
      ```bash
      python typerapp.py kth --help
      ```
      ```bash
      python typerapp.py kth
      ```
   2. Under this new framework, how do you think new subcommands or flags can be defined?
   3. Consider going over the tutorial at https://typer.tiangolo.com/tutorial/

