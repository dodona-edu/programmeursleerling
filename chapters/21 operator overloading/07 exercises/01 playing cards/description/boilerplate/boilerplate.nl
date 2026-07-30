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
