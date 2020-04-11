Objects can be part of other objects. For instance, a rectangle can be
defined as a point that indicates its top-left corner, a width, and a
height. As such, the class `Rectangle` can be defined as follows:

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = point
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, 
            self.height )

p = Point( 3.5, 5.0 )
r = Rectangle( p, 4.0, 2.0 )
print( r )
```

In this definition, the `Rectangle` object contains a `Point` object.

Create a different version of the `Rectangle` class, that instead of the
top-left corner point, width, and height, gets the top-left corner point
and the lower-right corner point.

### Copies and references

Below is a copy of the code above, expanded with a few extra lines that
make a change to the `Point p`.

```python
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = point
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, 
            self.height )

p = Point( 3.5, 5.0 )
r = Rectangle( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )
```

When you run this code, you see that by changing `p`, the `Rectangle r`
is also changed. The point that it contains, is actually a reference to
the point that was passed to the `__init__()` method. Like lists,
dictionaries, and sets, all the objects that are instances of classes
that you define, are "passed by reference" to functions and methods.
Therefore, `Rectangle r` gets created with a reference to `p`. This way,
relationships between objects can be represented.

You do not always want this. In fact, it is unlikely that you would want
a `Rectangle` object to have a relationship with the point that is
indicated as its upper left corner. How can you solve that? You can
solve it by creating a copy of the object. You can do this using the
`copy` module. As discussed before, the `copy()` function of the `copy`
module creates a shallow copy; if you want a deep copy, you have to use
the `deepcopy()` function. For `Point`s this is not needed, as there is
no difference between shallow and deep copies of instances of this
class.

```python
from copy import copy

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = copy( point )
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, 
            self.height )

p = Point( 3.5, 5.0 )
r = Rectangle( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )
```
