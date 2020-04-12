Text files use an "encoding," i.e., a system that prescribes how
characters in the files are supposed to be interpreted. This encoding
may differ between operating systems. You can see the preferred encoding
that your system uses with a call to `sys.getfilesystemencoding()`.

```python
from sys import getfilesystemencoding

print( getfilesystemencoding() )
```

If you read a text file which uses a different encoding than your file
system prefers, you may get a `UnicodeDecodeError`. Whether or not you
get this error for a particular file, is related to your operating
system. An annoying consequence of that is that when you port Python
code that reads a file to another system, a file that could be read by
your code previously may cause your code to crash after the port.[^10]

An easy way to get around this problem is by adding an extra parameter
when opening a file, which indicates the encoding mechanism that you
want to use when reading the file. You do this by adding a parameter
`encoding=<encodingname>`, where `<encodingname>` is a string that can
have a variety of values, for which some typical ones are:

-   `ascii`: 7-bits encoding, characters with values in the range 00-7F

-   `latin-1`: 8-bits encoding, characters with values in the range
    00-FF

-   `mbcs`: 2-byte encoding, that is currently getting replaced by UTF-8

-   `utf-8`: variable bytes encoding

Typically, text files are created with `ascii` or `latin-1` encoding.
Since `ascii` is incorporated in `latin-1`, you can safely open any text
file by specifying `latin-1` as encoding. It is possible that for the
characters beyond the `ascii` range, you get different characters than
the person who created the file wanted you to see – that depends on the
encoding mechanism that your file system uses. But at least the
`UnicodeDecodeError` is avoided. So, when you try to read the contents
of a file and get a `UnicodeDecodeError`, you may try to open it using
`open( <``file``>, encoding="latin-1" )`. Usually that will solve the
problem.

Note that while `utf-8` supports a much wider range of characters than
`latin-1`, you may still get the `UnicodeDecodeError` when you read a
text file that uses `latin-1` encoding on a system that uses `utf-8`
encoding, as `utf-8` has no corresponding characters with values in the
(hexadecimal) range 80-FF.

If you want to see which special characters are supported with values in
the range 80-FF on your system, run the code below. The numerical value
of a character in the table can be derived by calculating $$16*row+col$$,
whereby `row` and `col` are the hexadecimal row and column number,
respectively. I do not display the characters in the range 80-9F, as
these are normally not filled in.

```python
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 10, 16 ):
    print( chr( ord( 'A' )+i-10 ), end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

More details on UTF-8 encoding will be given in Chapter
<a href="#ch:bitwiseoperators" data-reference-type="ref" data-reference="ch:bitwiseoperators">20</a>,
but for dealing with text files, the information above suffices.

[^10]: I have to make note of some Python behavior that seems bizarre
    when you first encounter it: you may get this error when your file
    contains characters in an encoding that is not supported by your
    system in lines that you are not even trying to read! E.g., suppose
    that there is such an erroneous character on line 10 of your file,
    but you are only trying to read the first 5 lines before closing the
    file again – your program may still crash! I suspect that this is
    related to the buffering of data: rather than reading exactly what
    you ask Python to read, Python reads data in bigger chunks, so that
    the program is faster when you actually want to go through the whole
    file. So, by trying to be smart, Python may saddle you up with
    problems that you did not expect could arise. It is good to be aware
    of such issues.
