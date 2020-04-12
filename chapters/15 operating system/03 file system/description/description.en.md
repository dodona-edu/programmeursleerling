A computer's file system consists of a tree-like structured organization
of directories and files.

There is one "root" directory, which is the main access point for all
other directories. The root directory is identified by a slash (`/`) or
backslash (`\`), depending on the operating system. Under Windows it is a
backslash, under Mac OS and Linux it is a forward slash. However,
Windows now also supports the forward slash. I recommend using the
forward slash in most cases, as in strings the backslash indicates a
special symbol, so if you want to use a backslash in a string as a
directory separator, you have to use a double backslash. This tends to
be confusing, which is why I recommend using the forward slash.

"Under" the root-directory there are multiple other directories, each
identified by a name, and usually also multiple files, each identified
by a name. Under each directory there may be more directories and files.

Each operating system has certain restrictions on what file and
directory names can be used, but in general most characters are
supported. It is convention that regular files have an extension, which
is placed at the end of the file name, and separated from the filename
with a period. The extension identifies what kind of file it is, for
instance, an executable program (`.exe`), a flat text file (`.txt`), or
a Python file (`.py`). It is also convention that directory names do not
have such an extension. However, this is not a rule, and you may
certainly encounter files without, and directories with an extension.
Note that in the visual environment, extensions for files are often
hidden, but they are there – you just do not see them.

To uniquely identify a file, you need to know its exact "path" from the
root to the file, following the directories. The path name for the file
is `/<directory>/<directory>/…/<filename>`. Under Windows, a drive
letter can be placed in front of this path, making it
`<drive>:/<directory>/<directory>/… /<filename>`. For instance, if
under Windows, on the "C" drive, under the root there is a directory
"Python34," under which there is a directory "Lib," in which you can
find a file "os.py," the path for that file is `C:/Python34/Lib/os.py`.
Under Windows, this path is case insensitive, so you can use only lower
case letters if you like. That is not the case for all operating
systems, though.

When you are working in the file system (and you always are working in
the file system, even if you do not realize that), there is a "current
directory," which is identified by a period (`.`). If you want to access
a file in the current directory, you do not need to know the complete
path; it is enough to know the file name. One directory "higher" than
the current directory (i.e., the "parent" directory) is identified by a
double period (`..`). The parent directory of the root is the root
itself.

Finally, it should be noted that most operating systems support a method
that allows you to access files, without knowing the path, even if those
files are not in the current directory. Under Windows, for instance, you
can set a `PATH` environment variable that contains a string that lists
all the directories that Windows will search when you use a filename
that is for a file that is not in the current directory. How to adapt
such an environment variable is not part of this book, though.
