Occasionally it happens that you want to exit a program early when a
certain condition arises. For instance, your program asks the user for a
value, and then processes that value extensively. But if the user enters
a value that cannot be processed, the program should just end. You could
code that as follows:

```python
from pcinput import getInteger

num = getInteger( "Please enter a positive integer: " )
if num < 0:
    print( "You should have entered a positive integer!" )
else:
    print( "Now I am processing your integer", num )
    print( "Lots and lots of processing" )
    print( "Hundreds of lines of code here" )
```

It is a bit irritating that most of your program is already one indent
deep, while you would have preferred to leave the program at the error
message, and then have the rest of the program at the top indent level.

You can do that using a special function `exit()` that is found in the
module `sys`. The code above becomes:

```python
from pcinput import getInteger
from sys import exit

num = getInteger( "Please enter a positive integer: " )
if num < 0:
    print( "You should have entered a positive integer!" )
    exit()

print( "Now I am processing your integer", num )
print( "Lots and lots of processing" )
print( "Hundreds of lines of code here" )
```

When you run this code and enter a negative number, depending on which
editor you use (IDLE does not have this issue), you may find that Python
raises a `SystemExit` exception, which looks like a big, ugly error. It
is not, however. This exception just says that you forced the program to
end, but that is exactly what you wanted. This is actually a nice, clean
exit.

In general, you are not allowed to ignore error messages and warnings.
This one is the exception to the rule. You are allowed to exit your
program this way. In Chapter
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>
I will explain how you can suppress this ugly message (if you get it and
if you really want to), but for now, just accept it.

