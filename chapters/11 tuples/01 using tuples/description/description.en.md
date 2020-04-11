A tuple is a group of one or more values, separated by commas. Normally,
tuples are written with parentheses around them, but the parentheses are
not actually necessary (except in circumstances where otherwise
confusion would arise). For example:

```python
t1 = ("apple", "orange")
print( type( t1 ) )
t2 = "banana", "cherry"
print( type( t2 ))
```

You can mix data types within tuples. You can even put tuples in tuples.

```python
t1 = ("apple", 3, 1.4)
t2 = ("apple", 3, 1.4, ("banana", 5))
```

To find out how many elements a tuple contains, you can use the `len()`
function.

```python
t1 = ("apple", "orange")
t2 = ("apple", 3, 1.4)
t3 = ("apple", 3, 1.4, ("banana", 5))
print( len( t1 ) )
print( len( t2 ) )
print( len( t3 ) )
```

Note that in this example, the length of `t3` is 4, and not 5. The last
element of `t3` is the tuple `("banana", 5)`, which counts as one
element.

You can use a `for` loop to access individual elements of a tuple in
sequence.

```python
t1 = ("apple", 3, 1.4, ("banana", 5))
for element in t1:
    print( element )
```

You can also use the `max()` and `min()` functions to get the maximum
respectively the minimum from a tuple of numbers. You can sum the
elements of a tuple using the `sum()` function.

```python
t1 = (327, 419, 101, 667, 925, 225)
print( max( t1 ) )
print( min( t1 ) )
print( sum( t1 ) )
```

You can test whether an element is part of a tuple by using the `in`
operator.

```python
t1 = ("apple", "banana", "cherry")
print( "banana" in t1 )
print( "orange" in t1 )
```

### Tuple assignments

As you have seen, you can create a tuple by assigning comma-separated
values to a variable. Parentheses around it are optional. What if you
want to create a tuple with only one element?

```python
t1 = ("apple")
print( type( t1 ) )
```

If you run this code, you will find that `t1` is of the class `str`,
i.e., a string. Putting parentheses around the element does not work, as
parentheses are optional. Python introduced a little trick to create a
tuple with only one element, and that is that you indicate that it is a
tuple by placing a comma after the value. This is rather unintuitive and
I would even say "degenerate," but historically this was the solution
that an early version of Python introduced, and for compatibility
reasons it was not changed.

```python
t1 = ("apple",)
print( type( t1 ) )
print( len( t1 ) )
```

Python allows you to place a tuple left of the assignment operator. This
is an exception to the rule that only one variable can be placed left of
an assignment. The values at the right side are copied one-by-one to the
left side, left to right.

```python
t1, t2 = "apple", "banana"
print( t1 )
print( t2 )
```

You can place parentheses around the values at the right side, and/or
parentheses around the variables at the left side, which makes no
difference.

If you place more variables at the left side than values at the right
side, you get a runtime error. The same for placing fewer (unless you
place just one, as shown above). However, you can create tuples at the
right side by placing parentheses.

```python
t1, t2 = ("apple", "banana"), "cherry"
print( t1 )
print( t2 )
```

### Tuple indices

Just like with strings, you can access the individual elements of a
tuple using indices. Where with strings the individual elements are
characters, for tuples they are the values. For instance:

```python
t1 = ("apple", "banana", "cherry", "durian")
print( t1[2] )
```

You can even use slices, with the same rules as for strings (if you do
not remember, check Chapter
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>
again). A slice of a tuple is another tuple. For example:

```python
t1 = ("apple", "banana", "cherry", "durian", "orange")
print( t1[1:4] )
```

Since tuples are indexed, an alternative for a `for` loop to access the
individual elements of a tuple is to loop over the indices.

```python
t1 = ("apple", "banana", "cherry", "durian", "orange")
i = 0
while i < len( t1 ):
    print( t1[i] )
    i += 1
```

Write a `for` loop that displays all the values of the elements of a
tuple, and also displays their index.

### Tuple comparisons

You can compare two tuples with each other by using the regular
comparison operators. These operators first compare the first two
elements of the tuples. If these are different, then the comparison will
determine which one is "smaller" based on the rules for these data
types, and result in `True` or `False`. If they are equal, the second
elements will be compared, etcetera.

```python
t1 = ( "apple", "banana" )
t2 = ( "apple", "banana" )
t3 = ( "apple", "cherry" )
t4 = ( "apple", "banana", "cherry" )
print( t1 == t2 )
print( t1 < t3 )
print( t1 > t4 )
print( t3 > t4 )
```

### Tuple return values

In Chapter
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>,
you learned that functions can return multiple values. If you code
something like that, what actually happens is that the function is
returning a tuple. To deal with such return values, you assign them to
variables as explained under "tuple assignments" above.
