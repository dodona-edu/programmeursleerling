KLEUREN = ('Harten', 'Schoppen', 'Klaveren', 'Ruiten')
WAARDEN = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Boer', 'Vrouw', 'Heer', 'Aas')

class Kaart:

    """
    >>> kaart_1 = Kaart('Harten', 'Aas')
    >>> kaart_2 = Kaart('Schoppen', 'Heer')
    >>> kaart_3 = Kaart('Klaveren', 'Heer')
    >>> kaart_1
    Kaart('Harten', 'Aas')
    >>> print(kaart_2)
    Heer van Schoppen
    >>> kaart_1 == kaart_2
    False
    >>> kaart_2 == kaart_3
    True
    >>> kaart_1 > kaart_2
    True
    >>> kaart_2 >= kaart_3
    True
    >>> Kaart('Bomen', 7)
    Traceback (most recent call last):
    AssertionError: ongeldige kaart
    """

    def __init__(self, kleur, waarde):

        assert kleur in KLEUREN, 'ongeldige kaart'
        assert waarde in WAARDEN, 'ongeldige kaart'

        self.kleur = kleur
        self.waarde = waarde

    def __repr__(self):

        return f'Kaart({self.kleur!r}, {self.waarde!r})'

    def __str__(self):

        return f'{self.waarde} van {self.kleur}'

    def __eq__(self, other):

        if isinstance(other, Kaart):
            return WAARDEN.index(self.waarde) == WAARDEN.index(other.waarde)
        return NotImplemented

    def __lt__(self, other):

        if isinstance(other, Kaart):
            return WAARDEN.index(self.waarde) < WAARDEN.index(other.waarde)
        return NotImplemented

    def __le__(self, other):

        if isinstance(other, Kaart):
            return WAARDEN.index(self.waarde) <= WAARDEN.index(other.waarde)
        return NotImplemented

    def __gt__(self, other):

        if isinstance(other, Kaart):
            return WAARDEN.index(self.waarde) > WAARDEN.index(other.waarde)
        return NotImplemented

    def __ge__(self, other):

        if isinstance(other, Kaart):
            return WAARDEN.index(self.waarde) >= WAARDEN.index(other.waarde)
        return NotImplemented

if __name__ == '__main__':
    import doctest
    doctest.testmod()
