import math

class Vorm:

    """
    >>> v = Vorm()
    >>> v.oppervlakte()
    NotImplemented
    >>> v.omtrek()
    NotImplemented
    """

    def oppervlakte( self ):
        return NotImplemented
    def omtrek( self ):
        return NotImplemented

class Rechthoek(Vorm):

    """
    >>> r = Rechthoek(1, 1, 8, 5)
    >>> r
    [(1,1),b=8,h=5]
    >>> print(r)
    [(1,1),b=8,h=5]
    >>> r.oppervlakte()
    40
    >>> r.omtrek()
    26
    """

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

class Vierkant(Rechthoek):

    """
    >>> v = Vierkant(2, 3, 4)
    >>> v
    [(2,3),b=4,h=4]
    >>> v.oppervlakte()
    16
    >>> v.omtrek()
    16
    >>> isinstance(v, Rechthoek) and isinstance(v, Vorm)
    True
    """

    def __init__( self, x, y, zijde ):
        Rechthoek.__init__( self, x, y, zijde, zijde )

class Cirkel(Vorm):

    """
    >>> c = Cirkel(0, 0, 3)
    >>> c
    [(0,0),straal=3]
    >>> print(c)
    [(0,0),straal=3]
    >>> c.oppervlakte()
    28.274333882308138
    >>> c.omtrek()
    18.84955592153876
    >>> isinstance(c, Vorm)
    True
    """

    def __init__( self, x, y, straal ):
        pass
    def __repr__( self ):
        pass
    def oppervlakte( self ):
        pass
    def omtrek( self ):
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
