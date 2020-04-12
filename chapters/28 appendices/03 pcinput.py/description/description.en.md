In many of the exercises in this book, it is useful to have a function
available that accepts inputs of a certain type. I created a module
called `pcinput` which contains a number of such functions. During many
of the exercises in this book, I assume that you have that module
available. To get it, download it from
<http://www.spronck.net/pythonbook>, or copy the code below to a file
called "pcinput.py," and make sure that it is located in same folder
where you keep the files with your own code.

Note that these functions are rather ugly as they print error messages
if something is wrong. However, nicer functions would be more difficult
to use (you would have to know about exceptions, which are not covered
until Chapter
<a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a>).
For the purpose of learning to code Python, they work fine.

Each of the functions asks the user to supply a value of a certain type
(a float, an integer, a string, or a capital letter), and returns that
value. You can call each of the functions with a string as argument,
that will be used as prompt.

```python
def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "That is not a number -- please try again" )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()

def getLetter( prompt ):
    while True:
        line = input( prompt )
        line = line.strip()
        line = line.upper()
        if len( line ) != 1:
            print( "Please enter exactly one character" )
            continue
        if line < 'A' or line > 'Z':
            print( "Please enter a letter from the alphabet" )
            continue
        return line
```
