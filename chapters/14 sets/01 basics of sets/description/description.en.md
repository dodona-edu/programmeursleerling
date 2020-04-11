Sets are unordered collections of elements. You cannot access specific
elements using an index or a key. The only way to access items in a set
is by using a `for` loop, or by testing for the existence of elements in
the set using the `in` operator.

You have to think of sets in the mathematical sense. In mathematics, a
set is a collection of elements, all unique, and elements can be part of
a specific set, or not part of the set. You use special set operators to
combine sets in different ways.

Python uses dictionaries to implement sets; specifically, it implements
the elements of a set as dictionary keys. Thus, only immutable data
types can be set elements. Sets themselves, however, are mutable.

Since Python uses dictionaries to implement sets, you might think that
you can create an empty set by assigning `\{\}` to a variable. That,
however, does not work as it creates an empty dictionary, not an empty
set. Instead, you create an empty set by assigning a call to the
function `set()` to a variable.

To create a set with some elements already in it, you can assign the
elements to the variable between curly brackets. Alternatively, you can
call the `set()` function with a list of the elements as argument.

```python
fruitset = { "apple", "banana", "cherry" }
print( fruitset )
```

If you want to create a set consisting of the different characters in a
string, you can call `set()` with the string as argument.

```python
helloset = set( "hello world" )
print( helloset )
```

You can use a `for` loop to traverse a set. The variable in the `for`
loop gets access to all the set elements. There is no way to determine
in which order you get to see the elements. Sorting them is not possible
as long as they form a set. You can, however, use list casting on a set
to create a list of its elements, which can then be sorted.

```python
fruitset = { "apple", "banana", "cherry", "durian", "mango" }
for element in fruitset:
    print( element )
print()

fruitlist = list( fruitset )
fruitlist.sort()
for element in fruitlist:
    print( element )
```

You can determine the number of elements in a set using the `len()`
function.
