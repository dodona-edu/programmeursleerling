Hieronder geef ik een class `Rechthoek`
met een `x` en `y` coördinaat die de linkerbovenhoek vastleggen, en een
breedte `b` en hoogte `h`. Creëer nu een class `Vierkant` die zoveel
mogelijk erft van `Rechthoek`.

```python
class Rechthoek:
    def __init__( self, x, y, b, h ):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
    def __repr__( self ):
        return "[({},{}),b={},h={}]".format( self.x, self.y, 
            self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)
```

### Voorbeeld

```console?lang=python&prompt=>>>
>>> r = Rechthoek(1, 1, 8, 5)
>>> r
[(1,1),b=8,h=5]
>>> print(r)
[(1,1),b=8,h=5]
>>> r.oppervlakte()
40
>>> r.omtrek()
26

>>> v = Vierkant(2, 3, 4)
>>> v
[(2,3),b=4,h=4]
>>> print(v)
[(2,3),b=4,h=4]
>>> v.oppervlakte()
16
>>> v.omtrek()
16
>>> isinstance(v, Rechthoek)
True
```
