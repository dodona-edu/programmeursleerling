You can type cast a sequence of elements to a list using the `list()`
function. The code below turns a tuple into a list.

```python
t1 = ( "apple", "banana", "cherry" )
print( t1 )
print( type( t1 ) )
fruitlist = list( t1 )
print( fruitlist )
print( type( fruitlist ) )
```

This is sometimes necessary, in particular when you have an "iterator"
available and you want to use the elements in a list format. An iterator
is a function that generates a sequence (more on iterators is given in
Chapter
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>).
An example of an iterator that I already discussed is the `range()`
function. The `range()` function generates a sequence of numbers. If you
want to use these numbers as a list, you can use list casting.

```python
numlist = range( 1, 11 )
print( numlist )
numlist = list( range( 1, 11 ) )
print( numlist )
```

You can turn a string into a list of its characters by using a list
casting on the string.
