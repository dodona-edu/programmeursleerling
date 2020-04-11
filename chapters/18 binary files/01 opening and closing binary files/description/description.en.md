The handling of binary files is quite similar to the handling of text
files. You have to `open()` a file when you want to access its contents,
`close()` it when you are finished, `read()` from the file and `write()`
to the file.

When you open a binary file, you have to indicate to Python that you
want to handle this file in "binary mode." You do this by adding a
letter `"b"` to the mode argument. For instance, to open a file in
"binary read" mode, the mode argument should be `"rb"`. You can also
open a file both for reading and writing; reading and writing you
indicate with mode `"r+"`, so reading and writing in binary mode is
`"r+b"` (while it is also possible to open text files in `"r+"` mode, I
did not indicate it in Chapter
<a href="#ch:textfiles" data-reference-type="ref" data-reference="ch:textfiles">17</a>,
as it seldom makes sense to open text files in this mode). Just as with
text files, if you open a binary file in write-mode, with `"wb"`, the
file gets emptied. The mode `"w+b"` will open a file for both reading
and writing, but also empties the file to start with.

When you open a file for both reading and writing, if the file pointer
is not at the end of the file, when you write you actually overwrite.

You can open any file in binary mode, even text files. However, when you
open text files in binary mode, you treat them like binary files, which
means that Python does not do the automatic conversion of newline
characters.

Closing a binary file is no different from closing a text file.

```python
fp = open( "pc_rose.txt", "rb" )
fp.close()
```

{:class="callout callout-info"}
> #### Note
> The code above has no output – if it does have output, that is a
> runtime error, meaning that "pc\_rose.txt" is not available.
