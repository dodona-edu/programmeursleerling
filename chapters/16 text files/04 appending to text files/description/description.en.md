"Appending" refers to writing at the end of an existing file. When you
open a file for appending, the contents are not erased, but the file
pointer is placed at the end of the file, where you can then write new
data. You open a file in "append" mode by using `"a"` as the mode
argument when opening the file.

The code below first displays the contents of "pc_writetest.tmp" (which
should exist by now). It then asks the user for lines which are appended
to the file. Finally, it displays the contents of the new file. I took
the liberty of creating this little program in a slightly-better
structured manner than before, using a constant for the filename that is
repeated three times in the program, and using a function to display the
file contents as this functionality is needed twice.

```python
FILENAME = "pc_writetest.tmp"

def displaycontents( filename ):
    fp = open( filename )
    print( fp.read() )
    fp.close()

displaycontents( FILENAME )

fp = open( FILENAME, "a" )
while True:
    text = input( "Please enter a line of text: " )
    if text == "":
        break
    fp.write( text+"\n" )
fp.close()

displaycontents( FILENAME )
```
