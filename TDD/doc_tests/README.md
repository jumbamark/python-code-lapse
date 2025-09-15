## doctest
- The `doctest` module searches for pieces of text that look like interactive Python sessions and then executes those sessions to verify that they work exactly as shown
- Common ways to use doctest:
    * To check that a module's docstrings are up-to-date by verifying that all interactive examples still work as documented
    * To perform regression testing by verifying that interactive examples from a test file or a test object work as expected
    * To write tutorial documentation for a package, liberally illustrated with input-output examples

### Checking Examples in Docstrings
- The simplest way to start a doctest is to end each module M with:
    ```python
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
    ```
- `doctest` will examine docstrings in module M
- Running the module as a script will cause the examples in the docstrings to get executed and verified. Nothing is display unless an example fails.
- You can force cerbose mode by passing `verbose=True` to testmod(), or prohibit it by passing `verbose=False`. In either of these cases `sys.argv` is not examined by `testmod()` (so passing `-v` or not will have no effect)
- Command line shortcut for running `testmod()` - `python -m doctest -v M.py`
- It imports `M.py` as a standalone module and runs `testmode()` on it

### Checking Examples in a Text File
- Another simple applicaton of doctest is testing interactive examples in a text file
- This can be done with the `testfile()` function
    ```python
    import doctest
    doctest.testfile("example.txt")
    ```
- This script will execute and verify any interactive Python examples contained in the file `example.txt`. The file content is treated as if it were a single giant docstring.
- As with `testmod()`, `testfile()` won't display anything unless an example fails.
- By default `testfile()` looks for files in the calling module's directory
- `testfile()`'s verbosity can also be set with the `-v` command-line switch or the optional keyword argument verbose
- Commandline shortcut - `python -m doctest -v add.txt`
- Because the file name does not end with `.py` `doctest` infers that it must be run with `testfile()` not `testmod()`

## How It Works
- which docstrings it looks at
- how it finds interactive examples
- what execution context it uses
- how it handles exceptions and how option flags can be used to control its behaviour

### Which Docstrings Are Examined?
- The module docstring and all functions, classes and method docstrings are searched
- Objects imported into the module are not searched
-If `M.__test__` exists and "is true" it must be a dict and each entry maps a (string) name to a function object, class object or string

### How are Docstring Examples Recognized?
- `doctest` doesn't do an exact emulation of any specific Python shell
- Any expected output must immediately follow the final ">>> " or "... " line containing the code
- Fine print:
    * Expected output cannot contain an all-whitespace line, such a line is taken to signal the end of expected output. If expected output does contain a blank line, put `<BLANKLINE>` in your doctest example each place a blank line is expected
    * All hard tab characters are expanded to spaces, using 8-column tab stops.
    * output to stdout is captured but not ouput to stderr (exception tracebacks are captured via a different means)
    * If you continue a line via backslasing in an interactive session you should use a raw docstring which will preserve your backslashes exactly as you type them,alternatively you can double each backslash in the doctest version (and not use a raw string
    ```python
    def f(x):
        r```Backslashes in a raw docstring: m\n```
        print(f.__doc__)
    ```

    ```python
    def f(x):
        ```Backslashes in a raw docstring: m\\n```
    ```
    * starting column doesn't matter

### What's the execution context?
- Each time `doctest` finds a docstring to test, it uses a shallow copy of M's globals so that running tests doesn't change the module's real globals.
- Examples cannot see names defined in other docstrings

### Exceptions
- provided that the traceback is the only output produced by the example: just paste in the traceback. Since tracebacks contain details that are likely to change rapidly (i.e exact file paths and line numbers), this is one case where doctests works hard to be flexible in what it accepts

### Option Flags
- A number of option flags control various aspects of doctest behaviour
- symbolic names for the flags are supplied as module constants, the names can also be used in doctest directives and may be passed to the doctest CLI via the `-o` option

### Directives
- Doctest directives may be used to modify the option flags for an individual example
- Doctest directives are special Python comments following an example's source code:
    __directive__             ::=   "#" "doctest:" directive_options
    __directive_options__     ::=   directive_option (", " directive_option)\*
    __directive_option__      ::=   on_or_off directive_option_name
    __on_or_off__             ::=   "+"\| "-"
    __directive_option_name__ ::= "DONT_ACCEPT_BLANKLINE" \| "NORMALIZE_WHITESPACE" \| ...

- Whitespace is not allowed between the `+` or `-` and the directive option name
- The directive option name can be any of the option flag names
- An example's doctest directives modify doctest's behaviour for that single example
- Use `+` to enable the named behaviour or `-` to disable it
- This test passes but its bound to fail without the directive;
    ```python
    >>> print(list(range(10))) # doctest: +NORMALIZE_WHITESPACE
    [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    ```
- It fails without the directive both because the actual output doesn't have two blanks before the single-digit list elements and because the actual output is on a single line
- This test also passes and requires a directive to do so:
    ```python
    >>> print(list(range(20))) # doctest: +ELLIPSIS
    [0, 1, ..., 18, 19]
    ```
- Multiple directives;
    ```python
    >>> print(list(range(20))) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    [0,   1,   ...,   18,   19]
    ```
- If multiple directive comments are used for a single example then they are combined:
    ```python
    >>> print(list(range(20))) # doctest: +ELLIPSIS
    ...                        # doctest: +NORMALIZE_WHITESPACE
    [0,    1, ...,    18,   19]
    ```
- You can add `...` lines to your example containing only directives, can be useful when an example is too long for a directive to comfortably fit on the same line:
    ```python
    >>> print(list(range(5)) + list(range(10, 20)) + list(range(30, 40)))
    ... # doctest: +ELLIPSIS
    [0, ..., 4, 10, ..., 19, 30, ..., 39]
    ```
- Since all options are displayed by default, directives only apply to examples they appear in


### Warnings
- `doctest` is serious about requiring exact matches in expected output. If even a single character doesn't match, the test fails
