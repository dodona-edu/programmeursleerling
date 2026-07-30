class Fruitmand:

    """
    >>> mand = Fruitmand({'mango': 2})
    >>> mand
    Fruitmand({'mango': 2})
    >>> len(mand)
    1
    >>> mand['mango']
    2
    >>> mand['kiwi']
    0
    >>> 'kiwi' in mand
    False
    >>> mand['kiwi'] = 3
    >>> mand + 'kiwi'
    Fruitmand({'kiwi': 4, 'mango': 2})
    >>> mand
    Fruitmand({'kiwi': 3, 'mango': 2})
    >>> mand -= 'mango'
    >>> mand -= 'mango'
    >>> mand
    Fruitmand({'kiwi': 3})
    >>> mand - 'papaya'
    Fruitmand({'kiwi': 3})
    """

    def __init__(self, fruit=None):

        pass

    def __repr__(self):

        pass

    def __len__(self):

        pass

    def __contains__(self, soort):

        pass

    def __getitem__(self, soort):

        pass

    def __setitem__(self, soort, aantal):

        pass

    def __add__(self, soort):

        pass

    def __iadd__(self, soort):

        pass

    def __sub__(self, soort):

        pass

    def __isub__(self, soort):

        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
