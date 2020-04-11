The file "pc\_binarytest.tmp" actually contains a few secret words,
which you cannot recognize when printing the file. I am going to use
them as an illustration on how to move the file pointer.

The file pointer indicates where in the file you start reading or
writing. You can move the file pointer with the `seek()` method.
`seek()` gets two integer arguments, of which the second one is
optional. The first argument is a relative byte position. The second is
the position relative to which you want to move the file pointer.

The second argument can be 0, 1, or 2. 0 means "relative to the
beginning of the file," 1 means "relative to the current file pointer
position," and 2 means "relative to the end of the file." If you do not
specify a second argument, it is assumed to be 0. In the `os` module
there are constants for this argument: `os.SEEK_SET` is 0, `os.SEEK_CUR`
is 1, and `os.SEEK_END` is 2.

The first parameter indicates how many bytes you move from the indicated
position. When starting at the beginning of the file, it should be a
positive number; when starting at the end of the file, it should be a
negative number; when starting somewhere in the middle of the file, it
can be positive or negative. For instance, the statement `fp.seek(5)` is
equivalent to `fp.seek(5,0)`, which moves the file pointer 5 bytes up
from the start of the file, placing it at the sixth byte.

Should you wish to know at which position the file pointer is currently
placed, you can use the `tell()` method. Both `seek()` and `tell()` can
be called for text files too, but are not very useful then.

Now, the secret words are found starting at position 50, and run for a
length of 23 bytes. The encoding is such that if you subtract 128 from
byte values, you get the ordinals for the letters. So, here is how you
get the words out of the file:

```python
fp = open( "pc_binarytest.tmp", "rb" )
print( "1. Current position of the file pointer is", fp.tell() )
fp.seek( 50 )
print( "2. Current position of the file pointer is", fp.tell() )
buffer = fp.read( 23 )
print( "3. Current position of the file pointer is", fp.tell() )
fp.close()

print( buffer )
s = ""
for c in buffer:
    s += chr( c-128 )
print( "The secret words are:", s )
```

The `seek()` method is particularly useful when you open a file in
"reading and writing" mode (`"r+b"`). It allows you to move through the
file, reading where you need to read, and (over)writing where you need
to (over)write.

Open the file "pc\_binarytest.tmp" in binary "reading and writing" mode,
and overwrite the encoded secret words with their decoded translation.
Once you have closed the file, open it again in text mode, read the
contents, and display them. If you did it all correctly, you should see
two readable lines. Should you mess up the file in some way, you can
always recreate it.
