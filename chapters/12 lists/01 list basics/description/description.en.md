A list is a collection of elements.

The elements of a list are *ordered*. Because they are ordered, you can
access each of the elements of a list using an index, just like you can
access the characters of a string, and just like you can access the
elements of a tuple. Indices start at zero, just as with strings.

In Python, lists are recognizable from the fact that they enclose their
elements in square brackets (`[]`). You can get the number of elements
in a list by using the `len()` function. You can use a `for` loop to
traverse the elements of a list. You can mix data types in a list. You
can apply the `max()`, `min()` and `sum()` functions to a list. You can
test for the existence of an element in a list using the `in` operator
(or for the non-existence by using `not in`).

![list](media/List.png "list"){:width="70%"}

```python
fruitlist = ["apple", "banana", "cherry", 27, 3.14]
print( len( fruitlist ) )
for element in fruitlist:
    print( element )
print( fruitlist[2] )

numlist = [314, 315, 642, 246, 129, 999]
print( max( numlist ) )
print( min( numlist ) )
print( sum( numlist ) )
print( 100 in numlist )
print( 999 in numlist )
```

Write a `while` loop to print the elements of a list.

Apart from the square brackets, lists seem to be a lot like tuples. Yet
there is a big difference...
