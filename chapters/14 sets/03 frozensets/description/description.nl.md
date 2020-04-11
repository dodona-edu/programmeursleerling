Python supports a variant on the set type, namely the `frozenset`. You
create a `frozenset` by using the `frozenset()` function. The elements
of a `frozenset`, once assigned, cannot be changed. You therefore have
to create the `frozenset` immediately when you call the `frozenset()`
function, because it is impossible to add or remove elements later.
I.e., `frozenset`s are immutable.

All the regular set methods work for `frozenset`s, except for those that
try to change the set. Trying to use such a method for a `frozenset`
will lead to a syntax error.

```python
fruit1 = frozenset( ["apple", "banana", "cherry"] )
fruit2 = frozenset( ["banana", "cherry", "durian"] )

print( fruit1.union( fruit2 ) )
```