Dictionaries are unordered collections of elements. To identify an
element, you have to know the element's "key."

Basically, dictionaries store "key-value pairs." Any immutable data type
can function as a key. A very common type to use as key is the string.

You create dictionaries using curly brackets `\{\}`, similar to how you
create lists using square brackets. An empty dictionary you create by
assigning `\{\}` to a variable. You can create a dictionary with
contents by describing every element of the dictionary between the curly
brackets using the syntax `<key>:<value>`, and commas between the
elements.

Here a dictionary fruitbasket is created, that contains three key-value
pairs, namely the key `"apple"` with value 3, the key `"banana"` with
value 5, and the key `"cherry"` with value 50.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
```

To access the value belonging to a specific key, you use the same syntax
as you would use for a list, except that you write the key in the place
where you would write the index for a list.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket["banana"] )
```

You can use a `for` loop to traverse a dictionary. The variable in the
`for` loop gets access to all the keys.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
for key in fruitbasket:
    print( "{}:{}".format( key, fruitbasket[key] ))
```

Trying to access a dictionary element using a key that is not available
in the dictionary will lead to a runtime error. However, adding a new
element to a dictionary you can do by simply assigning a value to the
dictionary item identified by the new key. For instance, adding a
`"mango"` to the `fruitbasket` you can do as follows:

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket )
fruitbasket["mango"] = 1
print( fruitbasket )
```

Overwriting a dictionary item works in exactly the same way as creating
a new dictionary item: you just assign a value to it.

Deleting an item from a dictionary you do using the `del` keyword, just
as you can use with lists.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket )
del fruitbasket["banana"]
print( fruitbasket )
```

You can determine the number of key-value pairs in a dictionary by using
the `len()` function.

By the way, do you understand how the ordering of a dictionary works
when looking at the display of a dictionary? Think about it.

The answer is: there is no ordering. That was what I said at the start:
dictionaries are unordered. In principle I cannot even tell you what
ordering you see on your screen when you run the code above, because it
might differ between computers, operating systems, and versions of
Python. There is a certain structure to the ordering of the items, but
nothing that you can (or should desire to) predict. By adding enough
items, the ordering might even suddenly change completely.

Since dictionaries are unordered, many of the concepts that are
applicable to lists, do not work on dictionaries. For instance, you
cannot refer to "slices" of a dictionary, and neither can you "sort" or
"reverse" a dictionary. So dictionaries are quite limited, but they do
have their uses.
