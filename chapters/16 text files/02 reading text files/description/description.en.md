To read the contents of a file, you must first open it, then read the
contents, then close it.

### Opening a file using `open()`

To open a file, you use the `open()` function.

The `open()` function gets two arguments, of which the second one is
optional. The first argument is the name of the file. If the file is not
in the current directory, you have to include the complete path to the
file so that Python can find it. The second argument is the "mode." The
mode indicates how you want to treat the file. The default mode (which
is picked when you do not supply the second argument) is opening the
file as a text file for reading only. How you set other modes is
discussed later.

The `open()` function returns a file handle, which you use for all the
remaining functionalities.

Rather than writing `<handle> = open( <filename> )`, you will often see
Python programs that write this as `open( <filename> ) as <handle>`.
These two ways of writing code are equivalent. I myself prefer the
first, as that is the way it is done in most programming languages.
However, the second method has an advantage that I discuss below, when
talking about closing a file.

### Reading a file using `read()`

The simplest way to read the contents of a file is using the `read()`
method, without arguments, on the file handle. This returns a string
that contains the complete contents of the file. `read()` can get an
argument, but I will discuss that in the chapter on binary files.

Reading from a file moves the file pointer to right after the part of
the file that was read. This means that if you use the `read()` method
without arguments, the file pointer is moved to the end of the file.
This entails that if you would try to `read()` from it a second time,
nothing would be read, as there is nothing to be read after the spot
where the file pointer is. `read()` then returns an empty string.

### Closing a file using `close()`

To close a file, you use the `close()` method on the file handle. After
that, the handle is no longer associated with the file. Every file that
you open, you should close at some point in your program.

So, a complete program that opens a file, reads the complete contents,
prints them, and closes the file again, is as follows:

```python
fp = open( "pc_rose.txt" )
print( fp.read() )
fp.close()
```

If everything that you need to do with a file is done in a single block,
you can write this block as follows:

```python
with open( <filename> ) as <handle>:
    <statements>
```

This syntactic construction has the advantage that the file will be
closed automatically after the block `<statements>` ends, so you do not
need to include an explicit `close()` call. This construction is
typically Python; you do not see it in many other programming languages.

### Displaying the contents of a file

Now the first few functions and methods for dealing with text files have
been introduced, I can show some code that reads the contents of a file.

```python
with open( "pc_rose.txt" ) as fp:
    buffer = fp.read()
print( buffer )
```

This code assumes that a file is available with the name "pc\_rose.txt,"
and that it is located in the same directory as the program. Appendix
<a href="#ch:testtextfiles" data-reference-type="ref" data-reference="ch:testtextfiles">33</a>
explains how to get it. If the file is unavailable, you get a runtime
error. How to deal with such errors will be explained in the next
chapter.

In the code above, change the file name "pc\_rose.txt" to something that
does not exist. Run the program and observe the error that you get.

In the code above, change the file name to "pc\_woodchuck.txt" (if you
have that file). Run the program and observe the output.

### Reading lines using `readline()`

To read a text file line by line, you can use the `readline()` method.
The `readline()` method reads characters starting at the file pointer up
to and including the next newline character, and returns them as a
string. You can recognize that you have reached the end of the file by
the fact that no characters are read anymore, i.e., the string that is
returned is empty.

```python
fp = open( "pc_rose.txt" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()
```

Notice that the output of the code above has an empty line between each
of the lines displayed. Where is that extra line coming from? Think
about it.

The extra line is there because the `readline()` method returns a string
of the characters read, up to and including the newline character. So
when the buffer is printed, it prints a newline character too. And since
the `print()` function also moves to a new line after it is executed,
there is an empty line printed after each line of text.

Write a program that reads the lines from "pc\_rose.txt," and displays
only those lines that contain the word `"name"`.

### Reading lines using `readlines()`

A corollary to the `readline()` method is the `readlines()` method.
`readlines()` reads all the lines in the file, and returns them as a
list of strings. The strings include the newline characters.

```python
fp = open( "pc_rose.txt" )
buffer = fp.readlines()
for line in buffer:
    print( line, end="" )
fp.close()
```

Note that the output of the code above does not have the empty lines
between the lines of text, as the `print()` function includes the
`"end="""` argument, which entails that `print()` itself does not go to
the next line after printing.

### When to use which file-reading method

Both the `read()` and `readlines()` method read a whole file at once.
Obviously, for small files this is acceptable, but for long files you
might not have enough memory to store the file contents efficiently. In
such circumstances (or when you do not know the file size), you should
read a file line by line with the `readline()` method.

It is often a good idea, during code development, to process only the
first few lines of a file. That way you limit the amount of time that
the program needs to process a file, and limit its output, which makes
debugging easier. For instance, the code below process the first 5 lines
of a file.

```python
fp = open( "pc_jabberwocky.txt" )
count = 0
while count < 5:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer, end="" )
    count += 1
fp.close()
```

Once the program is finished and debugged, I can remove the references
to `count` and change the loop to `while True`, to process the whole
file.

Adapt the code above to count how often the word "jabberwock" (with any
capitalization) occurs in the first 5 lines. Print only the number of
occurrences of that word. Once it works, remove the `count` so that you
count the number of occurrences of the word in the text as a whole.
