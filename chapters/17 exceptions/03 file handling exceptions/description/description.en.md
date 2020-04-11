Any problem with accessing files, whether it is the inability to find a
file, a problem with reading or writing a file, or trying to open a
protected system file or even a directory, leads to an `IOError`
exception. Since problems with file access are quite common and usually
at least partly outside the realm of control of the program, it is a
good idea to handle `IOError` exceptions in your programs when you can.

Since many different things can go wrong with files, the `args` tuple
explained above might be used to provide better information on what you
have to do to handle the problem. For instance, if your program asked
the user to supply a filename, and when you open that file you get an
`IOError`, if the error number (the first element of the tuple)
indicates that the file does not exist (2), then an appropriate response
might be to simply report this to the user and ask for a new name.

The error numbers are defined in the `errno` module, which you can
import in your program. The module offers constants that you can use
instead of the actual numbers, which is the convention. The most common
error numbers are:

-   `errno.ENOENT`: No such file or directory. You get this when you try
    to access a file that does not exist.

-   `errno.EACCESS`: Permission denied. You can get this in varied
    circumstances, such as when you try to read from a closed file, when
    you try to open a read-only file for writing, or when you try to
    open a directory as if it is a file.

-   `errno.ENOSPC`: No more space left on device. You get this when you
    try to write a file and there is no room for it, for instance when
    you try to write to a USB-stick that is full.

There is a big list of such error numbers which you can easily find in
the reference manuals. You might not understand what all of them refer
to, and actually many of them are archaic and no longer occur on modern
computer systems. The best thing to do when you develop your program, is
to try to capture `IOError`s, and when you do encounter an `IOError`,
print the arguments so that you know the number and the error message.
You can then look up which `errno` constant that message belongs to, and
respond to it in your program if you can do that in a sensible way.

However, just as with other kinds of exceptions, it is better to avoid
them than to capture them. There is no reason that you should ever
encounter a "file does not exist" error, as you can test whether a file
exists with the `exists()` and `isfile()` functions from the `os.path`
module.

```python
import errno

try:
    fp = open( "NotAFile" )
    fp.close()
except IOError as ex:
    if ex.args[0] == errno.ENOENT:
        print( "File not found!" )
    else:
        print( ex.args[0], ex.args[1] )
```

{:class="callout callout-info"}
> #### Note
> Exception `FileNotFoundError` is a "subclass" (see Chapter <a href="#ch:inheritance" data-reference-type="ref" data-reference="ch:inheritance">23</a>) of `IOError`, which, in Python 3, is actually an alias for yet another exception, namely `OSError`. This means that capturing `FileNotFoundError` is equivalent with capturing `IOError` (or `OSError`) `as ex` and testing whether `ex.args[0]` holds `errno.ENOENT`.
