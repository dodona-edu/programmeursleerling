You are allowed to raise exceptions yourself. For that, you use the
keyword `raise`, and follow that with one of the known exceptions
(potentially, you could create your own, new exceptions if you like, but
you need to have studied Chapters
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
and
<a href="#ch:inheritance" data-reference-type="ref" data-reference="ch:inheritance">23</a>
before you are ready for it). You can give the exception arguments of
any kind that you like.

You might wonder why you would want to raise your own exceptions. The
answer is that when you create a module, when an error occurs (for
instance because the main program that uses the module passes arguments
to a function that are of an incorrect type), it is bad form to print an
error message. It is much better to just raise an exception, and let the
main program handle the exception. Here is an example of raising an
exception:

```python
def getStringLenMax10( prompt ):
    s = input( prompt )
    if len( s ) > 10:
        raise ValueError( "Length exceeds 10", len( s ) )
    return s

print( getStringLenMax10( "Use 10 characters or less: " ) )
```

When you run this code, you see that if you enter a string of more than
10 characters, a `ValueError` exception is raised. It has two arguments,
which you can see displayed as a tuple when Python splashes the
exception on the screen. You can handle this exception just as you would
handle exceptions that Python itself produces.

The `raise` keyword has a second function: if you are in an `except`
clause, and rather than handle the exception there, you want to pass it
on to the "next level" of the program, you can just write the keyword
`raise`, and the exception will be "re-raised." This can be useful when
you want to do a bit of extra handling before the program "crashes" or
the exception is handled elsewhere. For instance:

```python
fp = open( "pc_rose.txt ")
try:
    buffer = fp.read()
    print( buffer )
except IOError:
    fp.close()
    raise
fp.close()
```

This code probably runs fine, but if an `IOError` occurs when reading
the file, the file gets closed before the exception is re-raised.
