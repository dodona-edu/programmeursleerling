Because lists are mutable, you can change the contents of a list.

To overwrite an element of a list, you can assign a new value to it.

```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[2] = "strawberry"
print( fruitlist )
```

You can also overwrite list slices by assigning a new list to the slice.
The slice you remove need not be of equal length to the new list you
insert.

```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:3] = ["raspberry", "strawberry", "blueberry"]
print( fruitlist )
```

You can insert new elements into a list by assigning them to an empty
slice.

```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:1] = ["raspberry", "strawberry", "blueberry"]
print( fruitlist )
```

You can delete elements from a list by assigning an empty list to a
slice.

```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:3] = []
print( fruitlist )
```

Using slices and assignments, you can adapt a list in any way that you
like. However, it is easier to change lists using methods. There are
many helpful methods available, which I am going to discuss below.

Change a list that contains only words (you can take one of the
`fruitlist`s above) by turning every word in the list into a word
consisting of only capitals. At this point in the book, the way to do
that is by using a `while` loop that uses a variable `i` that starts at
0 and runs up to `len(<``list``>)-1`. Use `i` as an index for this list.
