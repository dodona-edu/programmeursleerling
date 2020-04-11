The `os` module supports many functions that allow you to affect the
file system. I will mention only a few of them, as many of them are
actually a bit dangerous to use (you can easily delete files that you
wanted to keep) and you do not need them anyway. If you are really
interested in manipulating the file system, you can read up on the
dozens of other functions that `os` supports.

### `getcwd()`

`getcwd()` returns the current working directory as a string.

```python
from os import getcwd
print( getcwd() )
```

### `chdir()`

`chdir()` changes the current working directory. The new directory is
provided as a string argument.

```python
from os import getcwd, chdir

home = getcwd()
print( home )
chdir( ".." )
print( getcwd() )
chdir( home )
print( getcwd() )
```

### `listdir()`

`listdir()` returns a list of all the files and directories in the
directory that is given as argument. The names are given in arbitrary
order. Notice that they do not include the full path name.

```python
from os import listdir

flist = listdir( "." )
for name in flist:
print( name )
```

### `system()`

`system()` gets a string argument that is a command, that Python
executes on the command line. You can use it to do anything that the
operating system supports, including running other programs. There are
better ways to execute other programs, though (look for functions that
start with "exec").
