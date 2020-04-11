When you try to run a Python program, Python first does a quick check to
see if all the statements in the program meet the basic Python syntax
requirements. If they do not, Python announces a "syntax error" and will
not run the program.

If no syntax errors are encountered, Python will run the program, but
may encounter statements that generate errors while trying to execute
them. Such statements cause a "runtime error." You have seen runtime
errors many times while writing code (don't try to deny it).

In general, you try to fix runtime errors by extending or changing your
code. For instance, the following program causes a runtime error when
you enter a zero as input:

```python
from pcinput import getInteger

num = getInteger( "Please enter a number: " )
print( "3 divided by {} is {}".format( num, 3/num ) )
print( "Goodbye!" )
```

Python tells you what kind of error it is, namely a `ZeroDivisionError`.
To fix it, you can change the program:

```python
from pcinput import getInteger

num = getInteger( "Please enter a number: " )
if num == 0:
    print( "Dividing by zero is not allowed" )
else:
    print( "3 divided by {} is {}".format( num, 3/num ) )
print( "Goodbye!" )
```

`ZeroDivisionError` is actually the name of an "exception" that Python
"raises" (generates). If you do not handle such an exception in your
program, Python interrupts the program's execution and splashes its
error message on the screen. However, this entails that you actually can
handle exceptions in your program and simply continue running it.

While in the code above you should ensure that no exception is raised on
dividing by zero – because you can foresee that this might happen – it
occasionally happens that you have to accept that exceptions might be
raised as you cannot foresee all the circumstances that your program
might have to deal with. This is especially relevant when your program
depends on elements outside its direct control, such as files and user
behavior.
