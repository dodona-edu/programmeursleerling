I already introduced to you the three methods `__init__()`,
`__repr__()`, and `__str__()`. These are predefined methods that every
class has. As they were defined by the Python developers, they have the
eccentric names that start and end with a double underscore. There are
several more of such methods, which I will discuss in later chapters.

You can also define your own methods for a class. Such methods get names
similar to names you give to functions, and tend to follow the same
conventions: starting with a lower case letter, and if there are
different words either have underscores between them or capitalize the
first letter of the second and later words. The prefix `is` is used for
methods that provide a `True`/`False` statement about the object, the
prefix `get` is used to get a value from an object, and the prefix `set`
is used to set a value for an object.

For instance, for a point I can create a method
`distance_from_origin()`, which calculates the distance from the point
(0,0) to the given point.

```python
from math import sqrt

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def distance_from_origin( self ):
        return sqrt( self.x*self.x + self.y*self.y )

p = Point( 3.5, 5.0 )
print( p.distance_from_origin() )
```

You may also create methods that change the object in some way. For
instance, the "translation" of points over a distance is defined as a
specific shift in the horizontal and in the vertical direction. A method
`translate()` gets two arguments (beyond the `self` reference), which
are the horizontal and vertical shifts.

```python
from math import sqrt

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def translate( self, shift_x, shift_y ):
        self.x += shift_x
        self.y += shift_y

p = Point( 3.5, 5.0 )
p.translate( -3, 7 )
print( p )
```

As you can see, I did not specify a return value (I did not need it),
but the new `translate()` method made changes to the point coordinates.

Enhance the `Point` class with a method that turns a point into its
polar opposite, i.e., invert the signs of its coordinates, e.g., (3,4)
becomes (-3,-4) and (-1,2) becomes (1,-2).
