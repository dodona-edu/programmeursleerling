Suppose that you want to store a certain data structure in a file, for
instance, a list of tuples. One way of doing that is to turn the tuples
into strings and write those into the file, one line for every tuple.
When you then later want to rebuild the data structure in a program, you
read the file, unravel the lines, and reconstruct the list of tuples. As
you can imagine, this encompasses a considerable amount of quite
difficult code.

Fortunately, you do not have to write such code. Python offers a
solution for storing data structures in files, including both structure
and content, which is called "pickling." You can write the whole data
structure to the file in one go, if you just open a binary file for
writing, and call the function `dump()` from the `pickle` module with
the data structure as first argument, and the file handle as second
argument.

```python
from pickle import dump

cheeseshop = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.pck", "wb" )
dump( cheeseshop, fp )
fp.close()

print( "Cheeseshop was pickled" )
```

To read the contents of a pickle file, you use the function `load()`
from the `pickle` module. `load()` gets a handle to the file as
argument. Do not forget to open the file in binary mode.

```python
from pickle import load

fp = open( "pc_cheese.pck", "rb" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )
```

As you can see, `load()` restores the data structure completely.

Pickling works even for your own classes:

```python
from pickle import dump, load

class Point:
    def __init__( self, x, y ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({},{})".format( self.x, self.y )

p = Point( 2, 5 )
fp = open( "pc_point.pck", "wb" )
dump( p, fp )
fp.close()

fp = open( "pc_point.pck", "rb" )
q = load( fp )
fp.close()

print( type( q ) )
print( q )
```
