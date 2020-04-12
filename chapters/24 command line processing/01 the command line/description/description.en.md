Chapter
<a href="#ch:operatingsystem" data-reference-type="ref" data-reference="ch:operatingsystem">16</a>
explained how you can get access to your computer's "command prompt". If
you do not remember, please go refresh your memory. The chapter also
explained that you can start Python programs directly from the command
prompt with the command:

```console?lang=bash&prompt=$
$ python <programname>.py
```

This works as long as your system knows how to find Python and the
program resides in the current directory. If the program is not in the
current directory, it will still work as long as you specify the
complete path to the program in the command.

### Batch processing

Suppose you have written a program that asks a user for a filename and
maybe for a few extra parameters, then processes the file with the
indicated name using the parameters. I then ask you to run that program
on all the files in a specific directory. The directory contains over
10,000 files. What will you do?

You might adapt the program so that instead of asking for the name of
file and processing that file, it processes all files in a directory,
using parameters that are not asked of the user. If the parameters that
you have to use differ per file, there has to be a way to know what they
are (perhaps you can derive them from the file name), so it should be
possible to calculate them. This solves your problem. But then I ask you
to run your program on a bunch of different directories. What will you
do?

You can adapt your program so that it contains a list of all the
directories that you need to process, then work through them one by one.
And every time that I ask you to add an extra directory, just change the
program. Regardless what I ask you, you can always adapt your program to
encompass my requests. Though you might get a bit annoyed that I am
asking you to change the program again and again and again.

There is a different way of handling such requests, and that is through
batch processing. All command lines support the running of so-called
"batch files," which contain a list of commands that you give to the
operating system. Under Windows such files have the extension `.bat`,
while under Mac and Linux they can have any name. However, you can
install different command shells which use different conventions –
potentially you could even use a Python shell and use Python itself to
write batch files.

The batch file can contain commands that use a close derivative of your
first program, that processes just one file, and call it for every file
that you want to process. The problem is, of course, that the program
requires user input, and you are not prepared to type inputs every time
the batch file calls the program. The solution is to change the program
in such a way that it processes command line arguments.

### Command line arguments

On the command line, you can start a Python program with a list of
arguments:

```console?lang=bash&prompt=$
$ python <programname>.py <argument_1> <argument_2> … <argument_n>
```

The arguments are separated from each other by spaces and can be
anything, though if you have an argument that contains spaces, you
should enclose it in double quotes. This, of course, immediately raises
the question what you should do if an argument contains a double quote,
and unfortunately the answer is "that depends on the command shell that
you are using." Most commonly, you either precede the double quote with
a backslash, or you write a double double quote.

Of course, just writing the arguments will not let your program process
them automatically. You have to extend your program with code that
processes command line arguments, which means you have to be able to
access those command line parameters directly.

### `sys.argv`

You get access to the command line arguments that your program was
supplied with via a pre-defined list that is available when you import
the `sys` module. The list is called `sys.argv`. It is a list of
strings, each string being one of the command line arguments that was
supplied to the program.

`sys.argv` always contains at least one element, namely the complete
name of the Python file that you are running, including the directories
and (under Windows) the drive letter of the place where the program file
resides. To know how many arguments were supplied (including the
filename), you can, of course, use the `len()` function.

When you work from an editor, in general you cannot supply command-line
arguments to your Python programs. So if you want to experiment with
this, you actually have to test your programs on the command line. That
is a bit of a hassle, especially during development time. However, I can
tell you how to set up your programs in such a way that handling command
line arguments is optional.

## Flexible command line processing

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
<a href="#ch:conditions" data-reference-type="ref" data-reference="ch:conditions">7</a>.
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
