To handle exceptions explicitly in your program, you use a
`try ... except` clause. There are different ways of applying this
clause.

### `try` ... `except`

The most basic form of the `try ... except` clause has the following
syntax:

```python
try:
    <statements>
except:
    <exception handling>
```

When the `<statements>` between `try:` and `except:` are executed and
raise an exception, Python immediately jumps to the
`<exception handling>` statements and executes those, after which the
program continues as normal, at the first line below the
`<exception handling>` statements. If no exceptions are raised during
the execution of the `<statements>`, the `<exception handling>`
statements are skipped.

Using exception handling, the code at the start of this chapter can be
written as follows to avoid runtime errors:

```python
from pcinput import getInteger

num = getInteger( "Please enter a number: " )
try:
    print( "3 divided by {} is {}".format( num, 3/num ) )
except:
    print( "Division by zero is not allowed" )
print( "Goodbye!" )
```

Multiple statements may be part of a single `try ... except` clause. For
instance, the following code raises an exception both when a user enters
zero and when a user enters 3. Both exceptions are handled by the same
`try ... except` clause.

```python
from pcinput import getInteger

num = getInteger( "Please enter a number: " )
try:
    print( "3 divided by {} is {}".format( num, 3/num ) )
    print( "3 divided by {}-3 is {}".format( num, 3/(num-3) ) )
except:
    print( "Division by zero is not allowed" )
print( "Goodbye!" )
```

This is slightly ugly, not only because these errors should have been
avoided rather than handled via exceptions, but also because when an
exception occurs, it is unclear which of the statements caused it
(though in this case, if you enter 3, you can see that the first of the
two statements under the `try` executed correctly). However, this is
just a demonstration, and there certainly can be situations where you
say "I do not care where an exception occurs in this sequence of
statements, but if anything happens, I want to do this."

### Handling specific exceptions

Examine the code below. This code can cause at least two different
exceptions. Which?

```python
print( 3 / int( input( "Please enter a number: " ) ) )
```

The two different exceptions that this code can generate are the
`ZeroDivisionError` when you enter a zero, and the `ValueError` when you
enter something that is not an integer. Try it if you did not try it
already.

You can handle both these errors with a single `try ... except` clause,
but you can distinguish them by specifying multiple `except`s. Each
`except` can be followed by one of the specific exceptions, and the code
below it will only be executed if that specific exception is raised.

```python
try:
    print( 3 / int( input( "Please enter a number: " ) ) )
except ZeroDivisionError:
    print( "Dividing by zero is not allowed" )
except ValueError:
    print( "You have not entered an integer" )
print( "Goodbye!" )
```

If you want to capture "all remaining exceptions," you add an `except`
without a specific exception at the end. Only one of the `except`
clauses will be executed, namely the first one encountered that applies.
It is a lot like an `if ... elif ... elif ... else` clause.

```python
try:
    print( 3 / int( input( "Please enter a number: " ) ) )
except ZeroDivisionError:
    print( "Dividing by zero is not allowed" )
except ValueError:
    print( "You have not entered an integer" )
except:
    print( "Something unforeseen went wrong" )
print( "Goodbye!" )
```

Here is a list of some specific exceptions that are raised often:

-   `ZeroDivisionError`: Trying to divide by zero

-   `IndexError`: Trying to access a list or tuple element with an
    out-of-bounds index

-   `KeyError`: Trying to access a dictionary element with an unknown
    key

-   `IOError`: Any error that occurs while trying to access a file

-   `FileNotFoundError`: Trying to open a file that does not exist for
    reading

-   `ValueError`: Error while trying to type cast a value to another
    value

-   `TypeError`: Using a value of a type that is not supported for an
    operation

The code below can generate several exceptions. These are now handled by
a single `try ... except` clause. Extend this code by handling all
exceptions that may occur explicitly (there are at least three different
kinds of exceptions that can be raised). Note: Let me stress again that
I rather have you avoid exceptions occurring than handling them, but in
this case I want you to practice with exception handling.

```python
fruitlist = ["apple", "banana", "cherry"]
try:
    num = input( "Please enter a number: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except:
    print( "Something went wrong" )    
```

### Adding an `else` clause

At the end of a `try ... except` clause you can add an `else` clause.
The statements with that `else` will be executed if no exception occurs.
For instance, in the code block below, the calculated value for `num`
will only be printed if no exception is raised.

```python
try:
    num = 3 / int( input( "Please enter a number: " ) ) 
except ZeroDivisionError:
    print( "Dividing by zero is not allowed" )
except ValueError:
    print( "You have not entered an integer" )
except:
    print( "Something unforeseen went wrong" )
else:
    print( num )
print( "Goodbye" )
```

In general, I prefer not to use an `else` clause with an exception, as
it feels like the code under the `except` clauses should be code that is
only executed in abnormal circumstances. But if you really want you can
use it.

### Adding a `finally` clause

You can add an extra branch to the `try` clause, which is `finally:`.
The `finally` clause has statements which are executed regardless of the
manner in which the `try` clause is exited. If it ends normally, it is
executed, but if you get a runtime error, it is executed too. You can
use such a `finally` clause to, for instance, make sure that a file gets
closed before code is harshly interrupted.

```python
try:
    fp = open( "pc_rose.txt" )
    print( "File opened" )
    print( fp.read() )
finally:
    fp.close()
    print( "File closed" )
```

### Accessing exception information

You can get extra information on the exception by adding and `as` clause
to the `except` statement, using the syntax
`except <exception> as <variable>`. When an `<exception>` occurs, the
variable is filled with an "exception object," that may provide more
information on the exception. The problem is that there is no
standardized way to get the information out: it depends on the kind of
exception what the variable contains.

The variable will always have a tuple of arguments (even if there is
only one), that were provided to the exception when it was raised. You
can examine these arguments by means of the attribute `<variable>.args`.
A `ValueError` gets a tuple with only one value, namely a string.

```python
try:
    print( int( "NotAnInteger" ) )
except ValueError as ex:
    print( ex.args )
```

If you run the code below, you see that an `IOError` gets a tuple of two
values: an integer and a string. The integer that is provided for the
`IOError` is actually quite informative, as it explains what went wrong.

```python
try:
    fp = open( "NotAFile" )
    fp.close()
except IOError as ex:
    print( ex.args )
```

### General advice on using exception handling

Never capture an exception and then just ignore it. In particular, you
should not use a general `try ... except` clause and then do nothing
with the exception. If you think you can ignore a certain exception,
make sure that you capture that specific exception, and comment in your
program why you think you can ignore it. Basically, all exceptions
should either be handled responsibly or should just make the program
crash.
