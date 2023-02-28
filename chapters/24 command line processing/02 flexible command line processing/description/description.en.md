When I code Python programs, I prefer working from an editor. There are
a few editors that support supplying command line arguments to a program
when testing it, but most do not. So I want to develop my programs in
such a way that I can build them as if they process command line
arguments, but that I can test them directly from an editor, and only
need to test whether or not they actually process command line
parameters correctly once. I do that as follows:

For every parameter that can be controlled via the command line, I
create a global variable. I fill these global variables with default
values. In the rest of the program, I use these variables as if they are
constants. Only at the very start of the main program I check for the
existence of command line arguments, and if I find those, I overwrite
the variables with values that are supplied on the command line.

The advantage of this approach is that I can develop my program without
using command line arguments. If I want to use different values for the
command line arguments for testing, I simply use different values for
the variables in which I will store the command line arguments. I can
even set up the program in such a way that it will either fill a
variable via a command line argument, or will ask the user for the value
if it was not supplied on the command line.

Typically, such code looks as follows:

```python
import sys

# 3 variables for holding the command line parameters
inputfile = "input.txt"
outputfile = "output.txt"
shift = 3

# Processing the command line parameters
# (works with 0, 1, 2, or 3 parameters)
if len( sys.argv ) > 1:
    inputfile = sys.argv[1]
if len( sys.argv ) > 2:
    outputfile = sys.argv[2]
if len( sys.argv ) > 3:
    try:
        shift = int( sys.argv[3] )
    except TypeError:
        print( sys.argv[3], "is not an integer." )
        sys.exit(1)
```

In this code, three command line arguments are supported: the first two
are strings, and the third is an integer. The third one is immediately
converted from a string (which a command line argument always is) to an
integer, and the program is aborted if this conversion fails. I could
have built in more checks for demonstration, but I assume that at this
point in your programming career that does not pose any problems to you.

All three arguments have a default value: the first string has default
value `"input.txt"`, the second string has default value `"output.txt"`,
and the integer has as default value 3. You are not expected to supply
all three arguments on the command line: if you supply zero, all three
default values will be used; if you supply one, the first string will be
overwritten with the command line argument, while the other two
variables will retain their default value; etcetera.

### `sys.exit()`

In the example code above the program is aborted using `sys.exit()` if
an argument is not meeting the requirements set to it. `sys.exit()` was
introduced in Chapter
7.
However, I did not explain at that time that `sys.exit()` can get a
numerical argument, which you see above. The use of this argument is
that it will be returned to the batch file that is running the program,
and the batch file can respond to it if it was designed to. The
numerical argument is supposed to be an error code. Typically, zero is
given as argument if everything was processed correctly (a program that
ends normally will also return zero), and otherwise another number is
used. As some systems are limited to the values zero to 255 as program
return values, it is convention to limit the `sys.exit()` argument to
that range of values too.

### `argparse`

If you want module support for command line processing, Python supplies
a standard module `argparse` for that. Frankly, I do not see much use
for such a module, as command line processing is too simple to spend
much time on. However, some Python programs, in particular those that
are meant to enhance the system, support a large and complex variety of
command line arguments, and may benefit from such a module. It is up to
you to study it if you think it may help you.
