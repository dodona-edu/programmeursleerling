At this point you know everything you need to handle text files in
Python. However, there are several handy functions that make your life
easier when dealing with files. These are collected in the `os.path`
module. As per usual, I am not going to list all of them, but I will
list the ones that you will use the most.

In these functions, the term "path" refers to a filename or a directory
name, complete with parent directories (and drive letter). The parent
directories (and drive letter) do not need to be there explicitly, but
even if they are not, implicitly they still are as each file and each
directory is located in a particular place in the file system.

### `exists()`

The function `exists()` gets a path as argument, and returns `True` if
that path exists, and `False` if it does not.

```python
from os.path import exists

if exists( "pc_rose.txt" ):
    print( "Rose exists" )
else:
    print( "Rose does not exist" )

if exists( "pc_tulip.txt" ):
    print( "Tulip exists" )
else:
    print( "Tulip does not exist" )
```

### `isfile()`

`isfile()` tests if the path that is supplied as argument is a file. If
it is, it returns `True`. If it is not, it returns `False`. If the path
does not exist, the function also returns `False`.

```python
from os.path import isfile

if isfile( "pc_rose.txt" ):
    print( "Rose is a file" )
else:
    print( "Rose is not a file" )
```

### `isdir()`

`isdir()` tests if the path that is supplied as argument is a directory.
If it is, it returns `True`. If it is not, it returns `False`. If the
path does not exist, the function also returns `False`.

```python
from os.path import isdir

if isdir( "pc_rose.txt" ):
    print( "Rose is a directory" )
else:
    print( "Rose is not a directory" )
```

### `join()`

`join()` takes one or more parts of a path as argument, and concatenates
them reasonably intelligently to a legal name for a path, which it
returns. This means that it will add and remove slashes as needed.
`join()` is particularly handy in combination with `listdir()` (see
Chapter
16,
and the example below).

The reason that `join()` is handy with `listdir()`, is that `listdir()`
results in a list of file names that do not include the directory names.
Usually, when you ask for a list of file names, you intend to open them
at some point. But to open a file that is not in the current directory,
you need to know the complete path name that leads to the file. When you
apply `listdir()`, you know where you are looking for files, so you know
the elements of the path name. To construct the complete path name for
each file, you need to concatenate the elements of the path name to the
file name. Rather than trying to decide where you need to add slashes,
and which kind of slashes they need to be, you can leave all of that to
the `join()` function.

The code below looks for all the files in the current directory, and
lists them including their complete path name. See how `join()` is used
to construct that path name from the current directory, and the file
name.

```python
from os import listdir, getcwd
from os.path import join

filelist = listdir( "." )
for name in filelist:
    pathname = join( getcwd(), name )
    print( pathname )
```

### `basename()`

`basename()` extracts the filename from a path, and returns it.

```python
from os.path import basename

print( basename( "/System/Home/readme.txt" ) )
```

### `dirname()`

`dirname()` extracts the directory name from a path, and returns it.

```python
from os.path import dirname

print( dirname( "/System/Home/readme.txt" ) )
```

### `getsize()`

`getsize()` gets the size of the file that is supplied as argument, and
returns it as an integer (representing a number of bytes). The file must
exist, otherwise you get a runtime error.

```python
from os.path import getsize

numbytes = getsize( "pc_rose.txt" )
print( numbytes )
```

Write a program that adds up the sizes of all the files in the current
directory, and prints the result.
