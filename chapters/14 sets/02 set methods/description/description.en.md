To manipulate the contents of sets, the following methods are supported.
This is not a complete list of set methods, but these are the most
common ones.

### `add()` and `update()`

Adding new items to a set you can do using the `add()` method, to add
one new element that you provide as an argument. If you want to add
multiple new elements at once, you can use the `update()` method, which
you provide with a list of the new elements as argument. You can also
use `update()` with a tuple as argument, and you can even use it with a
string as argument. If you use it with a string, it will consider each
letter of the string as a separate element to add.

Since sets can only contain unique elements, any duplicate element that
you try to add will be ignored.

```python
fruitset = { "apple", "banana", "cherry", "durian", "mango" }
print( fruitset )
fruitset.add( "apple" )
fruitset.add( "elderberry" )
print( fruitset )
fruitset.update( ["apple","apple","apple","strawberry",
    "strawberry","apple","mango"] )
print( fruitset )
```

### `remove()`, `discard()`, and `clear()`

To remove elements from a set, you can use the `remove()` or `discard()`
method. Both get the element to remove as argument. The difference
between the two methods is that `remove()` will cause a runtime error if
the element is not part of the set, while `discard()` will ignore such
errors.

```python
fruitset = { "apple", "banana", "cherry", "durian", "mango" }
print( fruitset )

fruitset.remove( "apple" )
print( fruitset )
```

`clear()` removes all elements of the set at once.

### `pop()`

Calling the `pop()` method will remove an element from the set and
return it. You cannot predict which element will be removed, as sets are
unordered.

```python
fruitset = { "apple", "banana", "cherry", "durian", "mango" }
while len( fruitset ) > 0:
    print( fruitset.pop() )
```

### `copy()`

Just like lists and dictionaries, if you assign a variable that contains
a set to another variable, you are creating an alias. Like with
dictionaries (and probably because sets are implemented as
dictionaries), you use the method `copy()` to create a copy of a set.

### `union()`

The union of two sets is a set which contains elements of both of them.
You can use the `union()` method for one set, with as argument a second
set, to return the union of both sets involved. This does not change the
sets themselves. Alternatively, you can use the special operator $$|$$
(pipeline) to create the union of two sets. Note: you might suspect that
you can also use the $$+$$ operator to combine two sets, but $$+$$ is not
defined for sets, and neither is $$*$$.

```python
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitunion = fruit1.union( fruit2 )
print( fruitunion )

fruitunion = fruit1 | fruit2
print( fruitunion )
```

### `intersection()`

The intersection of two sets is a set which contains only the elements
that they both have. You can use the `intersection()` method for one
set, with as argument a second set, to return the intersection of the
sets involved. This does not change the sets themselves. Alternatively,
you can use the special operator `&` (ampersand) to create the
intersection of two sets.

```python
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitintersection = fruit1.intersection( fruit2 )
print( fruitintersection )

fruitintersection = fruit1 & fruit2
print( fruitintersection )
```

### `difference()`

The difference of two sets is a set which contains only the elements
that the first set has that are not also in the second set. You can use
the `difference()` method for one set, with as argument a second set, to
return the difference whereby the elements of the argument set are
removed from the first set. This does not change the sets themselves.
Alternatively, you can use the special operator `-` (minus) to create
the difference of two sets.

```python
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitdifference = fruit1.difference( fruit2 )
print( fruitdifference )

fruitdifference = fruit1 - fruit2
print( fruitdifference )

fruitdifference = fruit2 - fruit1
print( fruitdifference )
```

### `isdisjoint()`, `issubset()`, and `issuperset()`

The methods `isdisjoint()`, `issubset()`, and `issuperset()` are all
called as methods of one set, with a second set as argument. All return
`True` or `False`. `isdisjoint()` returns `True` if the two sets share
no elements. `issubset()` returns `True` if all the elements of the
first set are also found in the argument set. `issuperset()` returns
`True` if all the elements of the argument set are also found in the
first set. Note that a set is both a subset and a superset of itself.

```python
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry" }

print( fruit1.isdisjoint( fruit2 ) )
print( fruit1.issubset( fruit2 ) )
print( fruit2.issubset( fruit1 ) )
print( fruit1.issubset( fruit1 ) )
print( fruit1.issuperset( fruit2 ) )
print( fruit2.issuperset( fruit1 ) )
print( fruit1.issuperset( fruit1 ) )
```

### Practice

There is also a set method `symmetric_difference()` which returns a set
that contains all the elements that are in the union of two sets, except
those that are found in both sets. For example, if set 1 contains A, B,
and C, and set 2 contains B, C, and D, the symmetric difference of sets
1 and 2 contains A and D. Can you implement the
`symmetric_difference()` method by using only some of the methods found
above?

In the chapter on iterations you were asked to write code that
determines all the letters that two words have in common, whereby each
letter should only be reported once. Using sets, you can do this very
efficiently. Please write the appropriate code.
