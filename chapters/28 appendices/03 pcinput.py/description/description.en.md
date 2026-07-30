{:class="callout callout-info"}
> #### Note
> This appendix documents the `pcinput` module from the printed book, as reference material for readers who run the exercises in their own environment, outside Dodona. The module is not available on Dodona, so you cannot import it in a solution that you submit. On Dodona you read the input with `input()` and cast it to the type you need: `int(input(prompt))` instead of `getInteger(prompt)`, `float(input(prompt))` instead of `getFloat(prompt)`, and `input(prompt)` instead of `getString(prompt)` or `getLetter(prompt)`. The functions below keep asking until the user enters something valid, and that is not needed on Dodona, where the input of an exercise comes from a fixed test case and is thus always valid already.

In many of the exercises in this book, it is useful to have a function
available that accepts inputs of a certain type. I created a module
called `pcinput` which contains a number of such functions. During many
of the exercises in this book, I assume that you have that module
available. To get it, download it from
<http://www.spronck.net/pythonbook>{:target="_blank"}, or copy the code below to a file
called "pcinput.py," and make sure that it is located in same folder
where you keep the files with your own code.

Note that these functions are rather ugly as they print error messages
if something is wrong. However, nicer functions would be more difficult
to use (you would have to know about exceptions, which are not covered
until Chapter
18).
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
