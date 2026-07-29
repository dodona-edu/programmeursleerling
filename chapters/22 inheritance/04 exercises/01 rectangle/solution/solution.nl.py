class Rechthoek:

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
    Een Vierkant is gewoon een Rechthoek waarvan breedte en hoogte
    toevallig gelijk zijn, en erft daarom zoveel mogelijk van Rechthoek:
    enkel __init__ moet aangepast worden, de rest (repr, oppervlakte,
    omtrek) wordt ongewijzigd hergebruikt.

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
    """

    def __init__( self, x, y, zijde ):
        Rechthoek.__init__( self, x, y, zijde, zijde )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
