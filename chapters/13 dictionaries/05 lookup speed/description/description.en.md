Lists and dictionaries are the two most-used data structures in Python.
While often it is clear when you should use which data structure, it is
helpful if you know a little bit about how Python processes these data
structures in case you have a choice.

Suppose that you read a large bunch of numbers from a file. The numbers
are all different and can be anything. You later need to compare the
numbers on another list to the numbers that you read from the file.

Should you use a list or a dictionary to store the numbers that you read
from the file? Since they are just numbers, without extra data, a list
seems to be the best option. There is, however, a problem if you use a
list here. Check out the following code, in which a list of 10000
numbers is created, and after that some code checks for 10000 different
numbers whether they are on the list (which none of them are).

```python
from datetime import datetime

numlist = []
for i in range( 10000 ):
    numlist.append( i )

start = datetime.now()
count = 0
for i in range( 10000, 20000 ):
    if i in numlist:
        count += 1
end = datetime.now()

print( "{}.{} seconds needed to find {} numbers".format( 
    (end - start).seconds, (end - start).microseconds,count ) )
```

Here is the code for doing the same thing with a dictionary, where I
simply store the value 1 with each number.

```python
from datetime import datetime

numdict = {}
for i in range( 10000 ):
    numdict[i] = 1

start = datetime.now()
count = 0
for i in range( 10000, 20000 ):
    if i in numdict:
        count += 1
end = datetime.now()

print( "{}.{} seconds needed to find {} numbers".format( 
    (end - start).seconds, (end - start).microseconds,count ) )
```

You will notice that for a dictionary, the code gives an answer almost
immediately, while for a list it takes quite some time for the code to
provide an answer.

The reason is that I use the `in` operator to check whether a number is
in the list, or in the dictionary. For a list this means that Python
searches through the list, sequentially, until it reaches the number or
reaches the end of the list. In this case, it means that Python checks
10000 times 10000 numbers (as it cannot find any of them), which is 100
million numbers.

For a dictionary, the process of finding a key is much faster. Python
can quickly decide whether or not a key is in a dictionary.[^9] Usually,
the checking of just a handful of numbers suffices. Therefore, the code
is much, much faster for a dictionary.

You might think that a couple of seconds for the list search is still
negligible, but the search time increases quadratically with the size of
the data. Depending on the problem, using a dictionary might be highly
preferable over using a list.

On the other hand, lists take less memory than dictionaries, and if you
can directly access a list item via its index, lists are faster than
dictionaries. For instance, in the problem above, if the list is sorted
you can find numbers on it in a smarter way than using the `in` operator
(checking about 14 indices would suffice) – in that case, a list may be
faster again.

From this, you should remember that a list is fast if you can access its
elements directly via their index, while a dictionary is a much better
choice if the main way to find something is by scanning items. The `in`
operator seems easy and reads well, but if you use it to seek something
in a long list, you better think again.

[^9]: Technically, Python stores the keys for the dictionary in a
    so-called "hash table." I will not explain the details here, and
    just tell you that a hash table allows for very fast look-up of keys
    at the cost of some memory.
