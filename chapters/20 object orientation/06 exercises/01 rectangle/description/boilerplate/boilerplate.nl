class Punt:

    """
    >>> p = Punt(3, 4)
    >>> p
    Punt(3, 4)
    >>> print(p)
    Punt(3, 4)
    """

    def __init__(self, x, y):

        pass

    def __repr__(self):

        pass

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

        pass

    def __repr__(self):

        pass

    def oppervlakte(self):

        pass

    def omtrek(self):

        pass

    def rechtsonder(self):

        pass

    def overlap(self, other):

        pass
