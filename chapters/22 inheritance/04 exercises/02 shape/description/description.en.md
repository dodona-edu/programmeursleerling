A `Rectangle` and a `Square` can be
considered shapes. There are, of course, different kinds of shapes which
are defined differently, but share with rectangles and squares that they
have an area and circumference. Define an interface class `Shape`, of
which `Rectangle` and `Square` are sub(sub)classes. Also define a class
`Circle` that you derive from `Shape`.

### Assignment

Below I give the `Shape` interface class from the previous exercise,
together with the `Rectangle` and `Square` classes built on top of it
(your submission is graded on its own, so it cannot import anything from
another exercise). `Shape` defines the common interface every shape must
support: a method `area` and a method `circumference`. `Shape` itself
does not know how to compute either, so both simply return
`NotImplemented`.

```python
class Shape:
    def area( self ):
        return NotImplemented
    def circumference( self ):
        return NotImplemented

class Rectangle(Shape):
    def __init__( self, x, y, w, h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
            self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)

class Square(Rectangle):
    def __init__( self, x, y, side ):
        Rectangle.__init__( self, x, y, side, side )
```

Now also create a class `Circle` that inherits directly from `Shape`
(not from `Rectangle` or `Square`). A circle is created with the `x` and
`y` coordinate of its center, and a radius `r`. If a circle is passed to
the builtin functions `repr` or `str`, the string
`"[({},{}),r={}]".format(x, y, r)` must be returned. Its `area` method
must return $$\pi r^2$$ and its `circumference` method must return
$$2\pi r$$ (use `math.pi`).

### Example

```console?lang=python&prompt=>>>
>>> shape = Shape()
>>> shape.area()
NotImplemented
>>> shape.circumference()
NotImplemented

>>> r = Rectangle(1, 1, 8, 5)
>>> r
[(1,1),w=8,h=5]
>>> r.area()
40
>>> r.circumference()
26
>>> isinstance(r, Shape)
True

>>> s = Square(2, 3, 4)
>>> s
[(2,3),w=4,h=4]
>>> s.area()
16
>>> s.circumference()
16
>>> isinstance(s, Rectangle)
True
>>> isinstance(s, Shape)
True

>>> c = Circle(0, 0, 3)
>>> c
[(0,0),r=3]
>>> c.area()
28.274333882308138
>>> c.circumference()
18.84955592153876
>>> isinstance(c, Shape)
True
>>> isinstance(c, Rectangle)
False
```
