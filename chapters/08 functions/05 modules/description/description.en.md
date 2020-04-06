Creating a module is very simple. You just create a Python file, with
extension `.py`, and place functions in it. You can then import this
Python file in another Python program (you just use the name of the file
without the extension `.py`; the file should be either in the same
folder as the program, or in a standard Python modules location), and
access its functions just as you access functions from regular Python
modules, i.e., you either import specific functions from the module, or
you import the module as a whole, and call its functions by using the
`<module>.<function>()` syntax.

### `main()`

When examining other people’s Python programs, in particular those that
contain functions that you might want to import, you often see a
construct like shown below:

```python
def main():
    # code...
    
if __name__ == '__main__':
    main()
```

The function `main()` contains the core of the program, and may call
other functions.

There is no need to understand this exactly, but what happens here is
the following: the Python file that contains the code can run as a
program, or the functions that it contains can be imported into other
programs. The construction shown here ensures that the program only
executes `main()` (which is the core program) if the program is run as a
separate program, rather than being loaded as a module. If, instead, the
program is loaded as a module into another program, only its functions
can be accessed, and the code for `main()` is ignored.

If the Python file that contains such a construct is predominantly used
as a module, the `main()` function usually contains some code that tests
the functions in the module. This is useful during development time.

The use of a program `main()` for the main functionality has an extra
use, though. Since it is a function, if you want to leave the program
for some reason in the middle of processing, you do not need to use the
`exit()` function from the `sys` module. You can simple `return` from
the `main()` function. This avoids the ugly error message that some
editors give on using the `exit()` function.
