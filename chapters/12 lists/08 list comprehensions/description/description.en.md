List comprehensions are a concise way to create lists. They are typical
for Python, but you do not find them in many other programming
languages. They are not actually needed, as you can use functions to
achieve the same effect, but as they are often used in examples
(especially by people who want to show off their Python abilities to
create short statements that have extensive effects), I thought it
prudent to discuss them. If you are never going to use them in your own
code, that is fine as they are completely optional. But you should be
able to recognize them in other people's code.

Suppose that you want to create a list consisting of the squares of the
numbers 1 to 25. A function that creates such a list is:

```python
def squareslist():
    squares = []
    for i in range( 1, 26 ):
        squares.append( i*i )
    return squares

sl = squareslist()
print( sl )
```

In Python, you can create that list with one single statement, namely as
follows:

```python
sl = [ x*x for x in range( 1, 26 ) ]
print( sl )
```

Now suppose that you want to create this list, but want to leave out
(for some reason) the squares of any numbers that end in 5. That would
add at least two lines to the function above, but with list
comprehensions you can still do it with that single line:

```python
sl = [ x*x for x in range( 1, 26 ) if x%10 != 5]
print( sl )
```

A list comprehension consists of an expression in square brackets,
followed by a `for` clause, followed by zero or more `for` and/or `if`
clauses. The result is a list that contains the elements that result
from evaluating the expression for the combination of the `for` and `if`
clauses.

The results can become quite complex. For instance, here is a list
comprehension that creates a list of tuples with three integers between
1 and 4, whereby the three integers are all different:

```python
triplelist = [ (x,y,z) for x in range( 1, 5 ) 
    for y in range( 1, 5 ) for z in range( 1, 5 ) 
    if x != y if x != z if y != z]
print( triplelist )
```

If you find list comprehensions hard to use, remember that there is
absolutely no reason to use them except for keeping code concise, and
that keeping code readable and understandable is far more important than
keeping it concise.
