A generator is a function that emulates the behavior of an iterable
object. In general, implementing a generator is shorter and easier than
creating an iterable. Several standard functions are implemented as
generators, for example `range()`.

Generators are based on the `yield` keyword. When calling `__next__()`
on a generator, the function is executed until `yield` is reached, then
the value that is associated with `yield` is returned. At that point,
the function "waits" until `__next__()` is called again, after which it
continues until `yield` is reached again. `StopIteration` is raised
automatically when the function ends.

There is no need to explicitly define `__next__()` and/or `__iter__()`.
A function is a generator simply because it contains the `yield`
keyword, and the associated iterable object is automatically created by
Python, including appropriate implementations for `__next__()` and
`__iter__()`.

```python
def fibo( maxnum ):
    nr1 = 0
    nr2 = 1
    while nr2 <= maxnum:
        nr3 = nr1 + nr2
        nr1 = nr2
        nr2 = nr3
        yield nr1

fseq = fibo( 1000 )
for n in fseq:
    print( n, end=" " )
print()
for n in fseq:
    print( n, end=" " )
```

### Generator expressions

In Chapter
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>,
I introduced the concept of list comprehension. Since any list can be
turned into an iterator, and thus into a generator, Python introduced a
similar concept for generators, and calls it "generator expressions."
The syntax for a generator expression is the same as for a list
comprehension, except that the square brackets are replaced by round
brackets.

For example, the following generator expression returns all squares up
to 100:

```python
seq = (x*x for x in range( 11 ))
for x in seq:
    print( x, end=" " )
```

If you just replace the outer two parentheses by square brackets in the
generator expression, the code runs with `seq` being the result of list
comprehension. To be absolutely clear about it: with list comprehension
the whole list is generated at once, while with a generator expression
the items are generated when needed. Thus, in principle a generator
expression is preferable, as it saves memory.
