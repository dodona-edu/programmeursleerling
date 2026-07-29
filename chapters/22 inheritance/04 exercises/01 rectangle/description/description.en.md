Below I give a `Rectangle` class that
is created with the `x` and `y` coordinate of the top-left corner, a
width `w`, and a height `h`. Now create a `Square` class that inherits
as much as possible from the `Rectangle` class.

```python
class Rectangle:
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
```

### Example

```console?lang=python&prompt=>>>
>>> r = Rectangle(1, 1, 8, 5)
>>> r
[(1,1),w=8,h=5]
>>> print(r)
[(1,1),w=8,h=5]
>>> r.area()
40
>>> r.circumference()
26

>>> s = Square(2, 3, 4)
>>> s
[(2,3),w=4,h=4]
>>> print(s)
[(2,3),w=4,h=4]
>>> s.area()
16
>>> s.circumference()
16
>>> isinstance(s, Rectangle)
True
```
