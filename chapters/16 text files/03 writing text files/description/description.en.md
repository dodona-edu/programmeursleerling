Writing a text file is similar to reading. You open the file, write to
it, and close it.

### Opening a file for writing

To open a file for writing, and writing only, you give the value `"w"`
as the second argument to the `open()` function. If the file does not
exist yet, it will create it. If it does exist, it will delete its
contents.

Let me repeat that: **when you open a file for writing and it already
exists, its contents are deleted!** There is no warning message saying
"are you sure?" The file is simply emptied. So you have to be very, very
careful when opening a file for writing. Usually I ask students to write
their programs in such a way that they first check if a file exists
before opening it for writing, and give an error message when it already
exists. Functions for checking if a file exists are discussed later in
this chapter.

### Writing using `write()`

To write something to a text file, you use the `write()` method with as
argument a string that you want to write to the file. The example code
below asks you to enter some strings, and writes them to a file. It
stops asking for inputs when you enter an empty line. It then opens the
file, reads the contents, and displays them. Run the code, enter at
least two lines of text, and see what happens.

```python
fp = open( "pc_writetest.tmp", "w" )
while True:
    text = input( "Please enter a line of text: " )
    if text == "":
        break
    fp.write( text )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )
```

If you did what I asked, you have noticed that all the text that you
entered is in the file, but it all is on one line. There are no newlines
in between. The reason is that you have to explicitly write newline
characters when you want newlines in your file. When you get input from
the keyboard using `input()`, while you stop entering input using the
`Enter` key, that does not result in a newline character in the string
that `input()` returns. So you have to add that to the string that you
write manually.

Adapt the code above so that every line of text that you enter, is a
separate line in the file that you write.

### Writing using `writelines()`

You can write a list of strings at once, by using the `writelines()`
method that gets the list as argument. Each of the strings in the list
must end in a newline character if you want those newline characters in
the output file. `writelines()` is the opposite of `readlines()`; if you
use the list that `readlines()` returns as argument for `writelines()`,
the contents of the output file will be exactly the same as the contents
of the input file.

Note that there is no `writeline()` method. `writeline()` would be
exactly the same method as `write()`, so it is not needed.

### Practice

Write a program that reads the contents of "pc_rose.txt," and writes
exactly the same contents to the file "pc_writetest.tmp." Then open the
file "pc_writetest.tmp" and display the contents. You can easily
construct this program by cobbling together some of the code given
above.

Write a program that reads the contents of "pc_rose.txt," reverses each
of the lines, and writes the reversed lines to the file
"pc_writetest.tmp." Then open the file "pc_writetest.tmp" and display
the contents.
