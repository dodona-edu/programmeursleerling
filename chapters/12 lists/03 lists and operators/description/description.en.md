Lists support the use of the operators $$+$$ and $$*$$. These operators work
similar as to how they work for strings.

You can add two lists together with the $$+$$ operator, the result of
which is a list which contains the elements of both lists involved. Of
course, you have to assign the result to a variable to store it.

You can multiply a list by a number to create a list that contains the
elements of the original list, repeated as often as the number
indicates. This can be a fast approach to create a list with all equal
elements.

```python
fruitlist = ["apple", "banana"] + ["cherry", "durian"]
print( fruitlist )
numlist = 10 * [0]
print( numlist )
```

Note: With the $$+$$ you can add a list to another list, but you cannot
add a new element to a list, unless you turn that new element into a
list with a single element by putting two square brackets around it. If
you try to add something to a list that is not a list, Python will try
to interpret it as a list – if it can do that (which it can, for
instance, for a string, which it can consider a list of letters); it
will then still do the addition but the result will not be what you
want. For instance, the code below tries to add a "cherry" to a list,
but only the second addition actually does what is intended.

```python
fruitlist = ["apple", "banana"]
fruitlist += "cherry"
print( fruitlist )

fruitlist = ["apple", "banana"]
fruitlist += ["cherry"]
print( fruitlist )
```
