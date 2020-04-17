from copy import copy

class Punt:

    """
    >>> p = Punt(3, 4)
    >>> p
    Punt(3, 4)
    >>> print(p)
    Punt(3, 4)
    """

    def __init__(self, x=0.0, y=0.0):

        self.x = x
        self.y = y

    def __repr__(self):

        return f'Punt({self.x}, {self.y})'

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

        self.punt = copy(punt)
        self.breedte = breedte
        self.hoogte = hoogte

    def __repr__(self):

        return f'Rechthoek({self.punt!r}, {self.breedte}, {self.hoogte})'

    def oppervlakte(self):

        return self.breedte * self.hoogte

    def omtrek(self):

        return 2 * (self.breedte + self.hoogte)

    def rechtsonder(self):

        return Punt(self.punt.x + self.breedte, self.punt.y + self.hoogte)

    def overlap(self, r):

        r1, r2 = self, r
        if (
            r1.punt.x > r2.punt.x or
            (
                r1.punt.x == r2.punt.x and
                r1.punt.y > r2.punt.y
            )
        ):
            r1, r2 = r, self

        if (
            r1.rechtsonder().x <= r2.punt.x or
            r1.rechtsonder().y <= r2.punt.y
        ):
            return None

        return Rechthoek(
            r2.punt,
            min(r1.rechtsonder().x - r2.punt.x, r2.breedte),
            min(r1.rechtsonder().y - r2.punt.y, r2.hoogte)
        )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
