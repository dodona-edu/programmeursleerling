The `collections` module contains handy classes that allow you to
manipulate iterables such as strings, tuples, lists, dictionaries, and
sets. `collections` offers many interesting functionalities, most of
which are a bit eccentric, making it unlikely that you will need to use
them soon. I discuss two of them, namely the `Counter` class and the
`deque` class.

A `Counter` object is a similar to a dictionary, which contains items as
keys, and for each of the items a "count" as value. You create a
`Counter` object by providing the sequence of which you want to count
the items as argument. It has some useful methods, such as:

-   `most_common()` gets an integer as argument and returns a list
    containing the items that have the highest count, as many as the
    integer argument indicates. The items on the list are 2-tuples, the
    first element of a tuple being the counted item, and the second
    element being the count. They are ordered from most common to least
    common. If no integer argument is specified, the list contains all
    the items.

-   `update()` gets an iterable as argument and "adds in" the items of
    the iterable.

```python
from collections import Counter

data = [ "apple", "banana", "apple", "banana", "apple", "cherry" ]
c = Counter( data )
print( c )
print( c.most_common( 1 ) )

data2 = [ "orange", "cherry", "cherry", "cherry", "cherry" ]
c.update( data2 )
print( c )
print( c.most_common() )
```

A `deque` object is a list that is supposed to be used as a "queue,"
i.e., a list for which items are added and removed from either end of
the list. It supports methods that are similar to list methods, such as
`append()`, `extend()`, and `pop()`, which work at the right side end of
the list, but also has similar methods that work at the left side end of
the list, such as `appendleft()`, `extendleft()`, and `popleft()`. For
the rest, it has the same methods that you expect a list to have. You
create a `deque` object with the iterable which you want to turn into a
`deque` as argument.

```python
from collections import deque

dq = deque( [ 1, 2, 3 ] )
dq.appendleft( 4 )
dq.extendleft( [ 5, 6 ] )
print( dq )
```
