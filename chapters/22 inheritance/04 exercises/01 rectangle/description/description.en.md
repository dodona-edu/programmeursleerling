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
