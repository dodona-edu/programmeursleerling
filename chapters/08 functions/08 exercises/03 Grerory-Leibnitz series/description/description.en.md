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
$ python <programname>.py <argument_1> <argument_2> ... <argument_n>
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
