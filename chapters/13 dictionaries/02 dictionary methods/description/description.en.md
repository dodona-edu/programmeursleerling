This section describes the dictionary methods that are most often used.

### `copy()`

Just like lists, if you assign a variable that contains a dictionary to
another variable, you are not creating a copy of the dictionary; you are
actually creating an alias (if you do not remember what an alias is, see
Chapter
13).
You cannot use the trick which is used for lists to create a copy, as it
uses a slice-syntax, and dictionaries do not support slices. Therefore,
there is a method `copy()` that returns a copy of a dictionary.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
fruitbasketalias = fruitbasket
fruitbasketcopy = fruitbasket.copy()

print( id( fruitbasket ) )
print( id( fruitbasketalias ) )
print( id( fruitbasketcopy ) )
```

Note that this method makes a shallow copy of the dictionary (see
Chapter
13
if you do not remember the difference between shallow and deep copies).
If you want to make a deep copy, use the `deepcopy()` function from the
`copy` module.

### `keys()`, `values()`, and `items()`

The method `keys()` provides an iterator that lists all the keys of a
dictionary. The method `values()` provides an iterator that lists all
the values of a dictionary. The method `items()` provides an iterator
that lists all the key-value pairs of a dictionary as tuples.

I specifically say that these methods returns an iterator and not a
list. If you want to turn them into lists, you have to use list casting
(see Chapter
13).

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( list( fruitbasket.keys() ) )
print( list( fruitbasket.values() ) )
print( list( fruitbasket.items() ) )
```

At this point you might be wondering when you can use an iterator. You
mainly use iterators for `for` loops (though you can also use them as
arguments for the functions `max()`, `min()` and `sum()`).

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }
for key in fruitbasket.keys():
    print( "{}:{}".format( key, fruitbasket[key] ) )
print( sum( fruitbasket.values() ) )
```

Since this code provides an unpredictable order for the keys, you might
want to sort them before looping over them. Since `keys()` does not
provide a list, it cannot be sorted directly, but you can turn the
result into a list using list casting. After doing that, you can sort.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }
keylist = list( fruitbasket.keys() )
keylist.sort()
for key in keylist:
    print( "{}:{}".format( key, fruitbasket[key] ) )
```

`keylist = list( fruitbasket.key() ).sort()` does not work, as you
cannot apply the `sort()` method directly to the list casting. You must
first create the list, then sort it. Neither can you write
`for key in keylist.sort()`, as the `sort()` method has no return value.

If you wonder why Python seems to prefer iterators instead of lists: the
answer is that iterators are more general and use much less memory. They
are "lazy" methods, as they only provide an item when it is requested.

### `get()`

The `get()` method can be used to get a value from a dictionary even
when you do not know if the key for which you seek the value exists. You
call the `get()` method with the key you are looking for, and it will
return the corresponding value when the key exists in the dictionary, or
the special value `None` when the key does not exist in the dictionary.
If you want to return a specific value instead of `None` if the key does
not exist, you can add that value as a second argument to the method.

```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }

apple = fruitbasket.get( "apple" )
if apple:
    print( "apple is in the basket" )
else:
    print( "no apples in the basket")

orange = fruitbasket.get( "orange" )
if orange:
    print( "orange is in the basket" )
else:
    print( "no oranges in the basket")

banana = fruitbasket.get( "banana", 0 )
print( "number of bananas in the basket:", banana )

strawberry = fruitbasket.get( "strawberry", 0 )
print( "number of strawberries in the basket:", strawberry )
```

Run and study the example above closely, as what it demonstrates about
the `get()` method is very useful. Suppose that you store a collection
of items with corresponding quantities, for instance, the contents of a
fruit basket with the keys being the names of the fruits and the values
being the quantities. When you query the `fruitbasket` using the `get()`
method with a second parameter zero, you can look for any fruit in the
basket without the need to check first if the fruit exists in the
basket, because if you ask for a fruit that is not there, the `get()`
method returns zero, which is exactly what you want to hear.

### Practice

The code below contains a list of words. Build a dictionary that
contains all these words as keys, and their quantities as values. Print
the words with their quantities.

```python
wordlist = ["apple","durian","banana","durian","apple","cherry",
    "cherry","mango","apple","apple","cherry","durian","banana",
    "apple","apple","apple","apple","banana","apple"]
```

The code block below contains a string that is a list of words,
separated by commas. Build a dictionary that contains all these words as
keys, and how often they occur as values. Then print the words with
their quantities.

```python
text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
    "apple,apple,cherry,durian,banana,apple,apple,apple," + \
    "apple,banana,apple"
```

The code block below contains a very small dictionary that contains the
translations of English words to Dutch. Write a program that uses this
dictionary to create a word-for-word translation of the given sentence.
A word for which you cannot find a translation, you can leave "as is."
The dictionary is supposed to be used case-insensitively, but your
translation may consist of all lower case words. It is nice if you leave
punctuation in the translation, but if you take it out, that is
acceptable (as leaving punctuation in is quite a bit of work, and does
not really have anything to do with dictionaries – besides, leaving
punctuation in is much easier to do once you have learned about regular
expressions).

```python
english_dutch = { "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
    "zaag", "first":"eerst", "performance":"optreden", "of":"van",
    "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
    "one":"een", "world":"wereld", "leading":"leidend", "modern":
    "modern", "composer":"componist", "composers":"componisten",
    "two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson."
```
