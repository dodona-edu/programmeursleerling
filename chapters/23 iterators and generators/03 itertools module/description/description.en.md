The `itertools` module contains a collection of functions that allow
advanced manipulation of iterators. Taken to the extreme, they allow for
a sort of "iterator algebra" that can be used to implement specialized
tools in Python. Here I just highlight a few of the basic functions from
`itertools` that you might find handy at times.

### `chain()`

`chain()` takes two or more iterables as arguments and functions as an
iterable that works through them in sequence.

```python
from itertools import chain

seq = chain( [1,2,3], [11,12,13,14], [x*x for x in range(1,6)] )
for item in seq:
    print( item, end=" ")
```

### `zip_longest()`

`zip_longest()` works like `zip()`, but will create an iterable that
generates as many elements as there are elements in the longest
argument. You specify a `fillvalue=` argument to indicate what value
should be used for empty spots.

```python
from itertools import zip_longest

seq = zip_longest( "apple", "coconut", "banana", fillvalue=" ")
for item in seq:
    print( item )
```

### `product()`

`product()` creates an iterable that produces all elements of the
Cartesian product of the iterables that are given as its arguments. To
put that in less mathematical terms: if two iterables are given as
arguments, and the first has elements $x$, $y$, and $z$, while the
second has elements $a$ and $b$, `product()` produces $xa$, $xb$, $ya$,
$yb$, $za$, and $zb$.

```python
from itertools import product

seq = product( [1,2,3], "ABC", ["apple","banana"] )
for item in seq:
    print( item )
```

### `permutations()`

`permutations()` gets an iterable as argument, and an optional second
argument that indicates a length. It creates an iterable that produces
all permutations of the elements of the first argument of the given
length. If no length is given, it generates all permutations that
contain all the elements. Note that if the iterable has certain elements
multiple times, you will get copies of permutations.

```python
from itertools import permutations

seq = permutations( [1,2,3], 2 )
for item in seq:
    print( item )
```

### `combinations()`

`combinations()` gets an iterable as argument, and a second argument
that indicates a length. It creates an iterable that produces all
combinations of the elements of the first argument of the given length.
The length is *not* optional (which is logical, if you think about it
for one moment – for maximum length there is only one combination). The
elements of the combinations will be in the order that they appeared in
the original iterable. Note that if the iterable has certain elements
multiple times, you will get copies of combinations.

```python
from itertools import combinations

seq = combinations( [1,2,3], 2 )
for item in seq:
    print( item )
```

### `combinations_with_replacement()`

`combinations_with_replacement()` works like `combinations()`, except
that each element of the iterable can be used multiple times.

```python
from itertools import combinations_with_replacement

seq = combinations_with_replacement( [1,2,3], 2 )
for item in seq:
    print( item )
```
