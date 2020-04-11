You write to a binary file using the `write()` method. The difference
with writing to text files is that you have to supply a byte string as
argument, rather than a regular string. The following code creates a
binary file with some text in it.

```python
from os.path import getsize

FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, "wb" )
fp.write( b"And now for something completely different...\x0A\
\x00\x00\x00\x00\xD4\xE8\xE5\xA0\xD3\xF0\xE1\xEE\xE9\xF3\xE8\xA0\
\xC9\xEE\xF1\xF5\xE9\xF3\xE9\xF4\xE9\xEF\xEE\x00\x00\x00" )
fp.close()
print( getsize( FILENAME ), "bytes written" )
```

Run the code above to create the binary file. The code below opens it in
text mode (you can do that, as Python cannot know that it actually is a
binary file), reads the contents, and prints the contents. You will see
some readable text and some unreadable characters.

```python
FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, encoding="latin-1" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()
```

Change the code above to open the file in binary mode and print the
contents.
