As binary files do not know the concept of "lines," the only way to read
from a binary file is to use the `read()` method. If you use `read()`
without argument, it reads the whole file (starting at the file
pointer). If you give the method an integer as parameter, that integer
indicates the number of bytes that are read from the file (starting at
the file pointer, and reading at maximum until the end of the file).

A "byte," if you do not know, is an 8-bit character, i.e., a number
between zero and 255, which is stored in the smallest possible memory
unit that a computer supports. The regular characters on a keyboard are
each stored in a single byte, and the characters in a string are also
each a byte, though limited to a specific range of numbers.

### Byte strings

Here we enter one of the more obscure parts of the Python language. When
you read from a binary file, the `read()` method does not return a
regular string – it returns a "byte string." There are some subtle
differences between regular strings and byte strings. To show you these
differences, I first have to tell you that you can indicate that a
string is a byte string by placing a letter `b` in front of it. So
`"Hello, world`"! is a string, while `b"Hello, world`"! is a byte
string.

![binary file](media/BinaryFile.png "binary file"){:width="50%"}

```python
hw1 = "Hello, world!"
hw2 = b"Hello, world!"

print( hw1 )
print( hw2 )
```

The difference between a string and a byte string is that a byte string
can contain characters that a string cannot. For instance, if you
remember the discussion on the ASCII table, you may recall that each
character has a number associated with it. You saw, for instance, that
"A" has the number 65, and the space has the number 32. The space was
the lowest numbered character that I showed, and you might wonder which
characters are associated with numbers 0 to 31. The answer is: these are
control codes, and are not legal characters that you can put in a string
(barring a few exceptions). You can try to put them in a string using an
"escape code": the escape sequence `\x` can be followed by a
two-character hexadecimal code that represents the character with the
specified number. For example, the hexadecimal code for a space is
`\x20`, i.e., `"Hello, world\`"! is the same as `"Hello,\\x20world\`"!
(this was discussed in Chapter
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>).

```python
hw1 = "Hello,\x20world!"
print( hw1 )
```

But what if you try to put illegal characters in a string that way? They
are ignored:

```python
print( "Hello,\x00\x01\x02world!" )
```

The problem is that such characters can occur in binary files, so you
must be able to read them from binary files. Since byte strings can
contain such characters, reading from binary files results in byte
strings.

```python
print( b"Hello,\x00\x01\x02world!" )
```

Characters from a byte string you can access using indices, just like
you do with regular strings. The difference here is that with regular
strings you get letters, while with byte strings you get numbers. The
numbers are the codes for the letters, which you would also get when you
use the `ord()` function on the corresponding letter.

```python
hw1 = "Hello, world!"
hw2 = b"Hello, world!"

for c in hw1:
    print( c, end=" " )
print()
for c in hw1:
    print( ord( c ), end=" " )
print()
for c in hw2:
    print( c, end=" " )
```

Since bytes are numbers between 0 and 255, you might want to convert a
number to a single-character byte string, or a list of numbers to a
multi-character byte string. You can do so using a `bytes` casting on a
list of those numbers. Note that if you want to convert a single
character, you still have to use a list, but a list with just one
element. Do not forget to put the list brackets around that element,
because if you do not, the result will not be what you expect.

```python
bs = bytes( [72,101,108,108,111,44,32,119,111,114,108,100,33] )
print( bs )
bch = bytes( [72] )
print( bch )
wrong = bytes( 72 )
print( wrong )
```

Can you convert from a byte string to a regular string? You might think
that string casting works, but unfortunately it does not:

```python
hw1 = b"Hello, world!"
hw2 = str( hw1 )
print( hw2 )
```

The reason that it does not, is that when a string is in the format of a
byte string, it uses an encoding scheme, according to the Unicode
standard (discussed in Chapter
<a href="#ch:textfiles" data-reference-type="ref" data-reference="ch:textfiles">17</a>).
You have to "decode" the byte string according to a certain decoding
scheme, which usually is `"utf-8"`, as that is the most common Unicode
format. You decode using the `decode()` method, with the encoding scheme
as a string parameter. You can also go from a string to a byte string by
encoding using the `encode()` method, again with the encoding scheme as
string parameter.

```python
hw1 = b"Hello, world!"
hw2 = hw1.decode( "utf-8" )
print( hw2 )
hw3 = hw2.encode( "utf-8" )
print( hw3 )
```

In general you have little reason to read text files in binary mode, at
least not if you just want to access the text, and so you do not have to
worry about encoding and decoding byte strings. The exception is when
you have to deal with a text file that uses Unicode characters. Such a
file cannot be treated as a text file, and you have to open it in binary
mode.

### Binary reading demonstration

To demonstrate how reading a binary file works, I now open the file
"pc\_rose.txt," and read ten times ten bytes from it.

```python
fp = open( "pc_rose.txt", "rb" )
for i in range( 10 ):
    buffer = fp.read( 10 )
    print( buffer )
fp.close()
```

When you run the code, you see the ten byte strings being displayed. You
may also notice that there are certain control characters visible, such
as `\r` and `\n`. The `\r` you would not see if you read this file as a
text file, because Python converts it, together with the following `\n`,
to a single `\n`. Moreover, in a regular string you would not see the
`\n`, because it is a newline character which tells Python to move to
the next line.

If instead of a text file, you open an actual binary file, you probably
will not be able to make much sense of the output when you display it.
