When you are working with a mouse-driven user interface (UI), which is
standard for Windows and Mac OS, and is used by many Linux users too,
you are actually interacting with a visual representation of the system,
specifically, of the file system. Programs and documents are represented
by "icons," which have a name. They are grouped by "folders," which are
actually "directories" of the file system. You can create new folders,
delete documents, rename programs, change security settings, etcetera.
All these actions you can also execute by directly typing commands, in
an environment that is often called the "command prompt" or "command
shell."

Most Linux users are familiar with a command shell, but for many Windows
and Mac users this is not something that they are aware of. Both Windows
and Mac actually have a program that allows you to work in the command
shell. On Windows, you find the "command prompt" as one of the
"accessories" or "system tools." On Macs, this is called the "Terminal."
If you start that program, you get confronted by a window with a black
background and a blinking prompt. Here you can type commands that the
system will execute for you.

The commands that you can give depend on the system that you are using.
This book is not meant to teach you how to use it, but I want to tell
you at least that you can run Python programs directly from the command
prompt by typing the command:

```console?lang=bash&prompt=$
$ python <programname>.py
```

As long as Python can be found on your system, and the program is
actually found in the current working directory (i.e., the place in the
computer's file system where you currently are), or you have specified
the complete path for the program, then it will run the program. This
can actually be quite handy if you have written a program that processes
files and you want to process many files in a "batch." Again, this goes
a bit too far for this book, but you might get to a point in your career
where this is extremely useful.

The commands that you can give are things like "change the current
working directory," "make a new directory," "remove an empty directory,"
"list all the files in the directory," "delete a file," etcetera. Again,
it depends on the operating system what exactly the commands are that
you need to give to achieve these things.

On your system, find the command shell and run the program. On Windows,
type "dir" to see the files in the current directory. On Macs and Linux,
this command is usually "ls." After doing this, you can close the
command shell again.
