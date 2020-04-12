You have used the `for ... in ...` command on many occasions. You may
have noticed that it can be used for many different applications.

```python
for i in [1,2,3,4]:
    print( i, end=" " )
print()
for i in ( "pi", 3.14, 22/7 ):
    print( i, end=" ")
print()
for i in range( 3, 11, 2 ):
    print( i, end=" ")
print()
for c in "Hello":
    print( c, end=" " )
print()
for key in { "apple":1, "banana":3 }:
    print( key, end=" " )
```

List, strings, and dictionaries are all "iterables," which means they
can be used in such `for ... in ...` expressions. Many other objects can
also be used as iterables. You can actually ensure that your own classes
can be used as iterables as well.

An "iterator" is an object that returns a new item every time you call
the `next()` function with the object as argument. When there are no
items left, it raises a `StopIteration` exception. If you want to avoid
the exception, you can give an optional second argument to `next()`,
which is returned when the iterator is exhausted. You can turn an
iterable into an iterator object using the built-in function `iter()`.

```python
iterator = iter( ["apple", "banana", "cherry"] )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
```

You can use iterators in `for ... in ...` statements.

```python
iterator = iter( ["apple", "banana", "cherry"] )
for fruit in iterator:
    print( fruit )
```

### Iterable objects

An object that should function as an iterable has two elements:

-   a method `__iter__()` that returns the object itself

-   a method `__next__()` that provides access to all the items that the
    object contains, one by one, and when no more objects are left,
    raises `StopIteration` (in a `for ... in ...` loop, this will cause
    the loop to end)

You can loop over all the items of the iterable using `for ... in ...`.
There are three main ways that you can create such an iterable object.
The first two ways start with the iterable as a container of a sequence
of items.

The first way, when `__next__()` is called, removes one of the items and
returns it, after which the iterable holds one less item. Once all items
are "consumed," it can only raise `StopIteration`. Here is an example of
such an iterator that contains the first 10 numbers of the Fibonacci
sequence.

```python
class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
```

The second way keeps track of an index in the sequence of items,
increasing it every time `__next__()` is called, and raises
`StopIteration` when the index goes beyond the range of items. In the
second way, you can implement a method that resets the index so that the
iterable can be used again.

```python
class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
        self.index = -1
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.index < len( self.seq )-1:
            self.index += 1
            return self.seq[self.index]
        raise StopIteration()
    def reset( self ):
        self.index = -1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
```

The third way has the iterable not as a container of items, but as a
calculator that every time that `__next__()` is called, determines the
next item. Such an iterable can either be finite, or have the ability to
supply an infinite number of items. It can also be reset if the
programmer supplied a method to do that.

```python
class Fibo:
    def reset( self ):
        self.nr1 = 0
        self.nr2 = 1
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
        self.reset()
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.nr2 > self.maxnum:
            raise StopIteration()
        nr3 = self.nr1 + self.nr2
        self.nr1 = self.nr2
        self.nr2 = nr3
        return self.nr1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
```

{:class="callout callout-warning"}
> #### Warning
> You have to be very careful when making an iterable that in
> principle may return an infinite number of items. Programmers count on
> `for ... in ...` never leading to an endless loop, but in the example
> above, without limiting the number of items to a maximum of 1000 when
> creating the `fseq` object, an endless loop would result. It is best to
> force the programmer to set a maximum to the number of items.

Create an iterator that generates all the squares of integers between 1
and 10. You may choose whichever approach you prefer.

### Delegated iteration

In the examples above, the iterable was created by calling the
`__iter__()` method for the object, which returned itself. That is not
needed. An iterable may delegate[^12] the iteration to another object,
that it creates and returns when `__iter__()` is called.

```python
class FiboIterable:
    def __init__( self, seq ):
        self.seq = seq
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()

class Fibo:
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
    def __iter__( self ):
        nr1 = 0
        nr2 = 1
        seq = []
        while nr2 <= self.maxnum:
            nr3 = nr1 + nr2
            nr1 = nr2
            nr2 = nr3
            seq.append( nr1 )
        return FiboIterable( seq )

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
for n in fseq:
    print( n, end=" " )
```

This approach has several advantages:

-   You can run several instances of the iterable in parallel without
    the need to explicitly create more than one (as they are created
    automatically when needed, i.e., when you use `for ... in ...`)

-   You do not need to call a `reset()` method to start from the
    beginning

-   The delegated iterable is automatically erased from memory after it
    is used up (Python automatically frees up memory of objects that the
    program no longer can refer to)

### `zip()`

You can create tuples that contain the items of multiple iterables using
the standard function `zip()`. To give a simple example:

```python
z = zip( [1,2,3], [4,5,6], [7,8,9] )
for x in z:
    print( x )
```

A zip-object is an iterator, i.e., you cannot print the zip-object
itself, but you have to loop over its elements instead. The $i$th
element of the zip-object consists of the $i$th elements of each of the
iterables that are its arguments. If these iterables are of unequal
length, the number of elements in the zip-object will be the same as the
number of elements of the shortest of the iterables.

In the example above, I just used lists as arguments. But you can use
any kind of iterable as argument. For example, the following code block
I zip together a range, an iterator, and a list comprehension:

```python
class Doubles:
    def __init__( self ):
        self.seq = [2*x for x in range( 1, 11 )]
    def __iter__( self ):
        return self
    def __next__( self ):
        return self.seq.pop(0)

seq = zip( range( 1, 11 ), Doubles(), [3*x for x in range(1,11)])
for x in seq:
    print( x )
```

Create a zip-object that produces tuples of two items: the first item is
an integer, which runs from 1 to 10. The second item is the square of
that integer.

### `reversed()`

The built-in function `reversed()` creates an iterator from an iterable
that processes the items of the iterator in reversed order. It gets the
iterable as argument.

Not all iterables can be reversed, but the ones that are part of the
standard Python specification (such as lists) can. For details on how to
make sure that iterables that you create yourself can be `reversed()`,
study the Python documentation.

```python
fruitlist = ["apple", "orange", "cherry", "banana"]
for fruit in reversed( fruitlist ):
    print( fruit )
```

### `sorted()`

The built-in function `sorted()` creates an iterator from an iterable
that processes the items of the iterator in sorted order. It gets the
iterable as argument.

Moreover, it can get two optional arguments. The first is `key=<key>`,
where `<key>` is the name of a function that is used to determine the
key for the sorting process. This works exactly as the `key=<key>`
parameter for the list `sort()` method – see Chapter
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>
for more information. If no key is given, the sorting is alphabetical
order for strings, and numerical order for numbers. For other data
types, or mixed data types, it depends on the specification of the key
argument.

The second optional argument is `reverse=<boolean>`, that indicates with
`True` or `False` whether or not the sorting should give a reversed
result.

```python
fruitlist = ["apple", "orange", "cherry", "banana"]
for fruit in sorted( fruitlist ):
    print( fruit )
```

[^12]: The name "delegated iteration" I came up with myself. If there is
    an "official" name for the approach, I gladly update the book.
