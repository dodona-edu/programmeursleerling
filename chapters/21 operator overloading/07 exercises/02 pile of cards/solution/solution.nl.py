KLEUREN = ('Harten', 'Schoppen', 'Klaveren', 'Ruiten')
WAARDEN = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Boer', 'Vrouw', 'Heer', 'Aas')

class Kaart:

    """
    >>> kaart_1 = Kaart('Harten', 'Aas')
    >>> kaart_2 = Kaart('Schoppen', 'Heer')
    >>> kaart_1
    Kaart('Harten', 'Aas')
    >>> print(kaart_2)
    Heer van Schoppen
    >>> kaart_1 > kaart_2
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

class Trekstapel:

    """
    De kaarten worden bijgehouden in een lijst waarvan het eerste element de
    bovenste kaart van de stapel is, en het laatste element de onderste. Een
    kaart trekken verwijdert dus het eerste element, en een kaart toevoegen
    hangt er een nieuw laatste element aan.

    >>> stapel = Trekstapel([Kaart('Harten', 4), Kaart('Klaveren', 7)])
    >>> stapel
    Trekstapel([Kaart('Harten', 4), Kaart('Klaveren', 7)])
    >>> len(stapel)
    2
    >>> stapel[0]
    Kaart('Harten', 4)
    >>> stapel[0] < stapel[1]
    True
    >>> stapel.voegtoe(Kaart('Schoppen', 'Aas'))
    >>> stapel.trek()
    Kaart('Harten', 4)
    >>> stapel
    Trekstapel([Kaart('Klaveren', 7), Kaart('Schoppen', 'Aas')])
    >>> Trekstapel().trek()
    >>> len(Trekstapel())
    0
    """

    def __init__(self, kaarten=None):

        self.kaarten = [] if kaarten is None else list(kaarten)

    def __repr__(self):

        return f'Trekstapel({self.kaarten!r})'

    def __len__(self):

        return len(self.kaarten)

    def __getitem__(self, index):

        return self.kaarten[index]

    def voegtoe(self, kaart):

        self.kaarten.append(kaart)

    def trek(self):

        return self.kaarten.pop(0) if self.kaarten else None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
