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

        pass

    def __repr__(self):

        pass

    def __str__(self):

        pass

    def __eq__(self, other):

        pass

    def __lt__(self, other):

        pass

    def __le__(self, other):

        pass

    def __gt__(self, other):

        pass

    def __ge__(self, other):

        pass

class Trekstapel:

    """
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

        pass

    def __repr__(self):

        pass

    def __len__(self):

        pass

    def __getitem__(self, index):

        pass

    def voegtoe(self, kaart):

        pass

    def trek(self):

        pass

def oorlogje(stapel_1, stapel_2):

    """
    >>> stapel_1 = Trekstapel([Kaart('Ruiten', 2), Kaart('Harten', 'Heer'), Kaart('Klaveren', 7)])
    >>> stapel_2 = Trekstapel([Kaart('Harten', 4), Kaart('Harten', 3), Kaart('Schoppen', 8)])
    >>> oorlogje(stapel_1, stapel_2) is stapel_1
    True
    >>> stapel_1
    Trekstapel([Kaart('Schoppen', 8), Kaart('Harten', 3), Kaart('Harten', 'Heer'), Kaart('Harten', 4), Kaart('Klaveren', 7), Kaart('Ruiten', 2)])
    >>> len(stapel_2)
    0
    >>> oorlogje(Trekstapel(), stapel_1) is stapel_1
    True
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
