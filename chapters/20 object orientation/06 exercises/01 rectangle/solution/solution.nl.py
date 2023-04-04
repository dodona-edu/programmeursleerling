class Punt:

    """
    >>> p = Punt(3, 4)
    >>> p
    Punt(3, 4)
    >>> print(p)
    Punt(3, 4)
    """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __repr__(self):

        return f'Punt({self.x}, {self.y})'

    def __eq__(self, other):

        return (self.x, self.y) == (other.x, other.y)

class Rechthoek:

    """
    >>> r1 = Rechthoek(Punt(1, 1), 8, 5)
    >>> r2 = Rechthoek(Punt(2, 3), 9, 2)
    >>> r1
    Rechthoek(Punt(1, 1), 8, 5)
    >>> print(r2)
    Rechthoek(Punt(2, 3), 9, 2)
    >>> r1.oppervlakte()
    40
    >>> r1.omtrek()
    26
    >>> r1.rechtsonder()
    Punt(9, 6)
    >>> r1.overlap(r2)
    Rechthoek(Punt(2, 3), 7, 2)
    >>> r2.overlap(Rechthoek(Punt(0, 0), 2, 2))

    >>> Rechthoek(Punt(3, 4), -2, 7)
    Traceback (most recent call last):
    AssertionError: ongeldige rechthoek
    """

    def __init__(self, punt, breedte, hoogte):

        assert breedte > 0, 'ongeldige rechthoek'
        assert hoogte > 0, 'ongeldige rechthoek'

        self.punt = punt
        self.breedte = breedte
        self.hoogte = hoogte

    def __repr__(self):

        return f'Rechthoek({self.punt!r}, {self.breedte}, {self.hoogte})'

    def __eq__(self, other):

        return (self.punt, self.breedte, self.hoogte) == (other.punt, other.breedte, other.hoogte)

    def oppervlakte(self):

        return self.breedte * self.hoogte

    def omtrek(self):

        return 2 * (self.breedte + self.hoogte)

    def rechtsonder(self):

        return Punt(self.punt.x + self.breedte, self.punt.y + self.hoogte)

    def overlap(self, other):

        # bepaal punt linkboven
        x1 = max(self.punt.x, other.punt.x)
        y1 = max(self.punt.y, other.punt.y)

        # bepaal punt rechtsonder
        x2 = min(self.rechtsonder().x, other.rechtsonder().x)
        y2 = min(self.rechtsonder().y, other.rechtsonder().y)

        return Rechthoek(Punt(x1, y1), x2 - x1, y2 - y1) if x1 < x2 and y1 < y2 else None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
