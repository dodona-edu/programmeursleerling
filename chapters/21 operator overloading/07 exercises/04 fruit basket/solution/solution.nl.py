class Fruitmand:

    """
    De stukken fruit worden bijgehouden in een dictionary die de naam van een
    fruitsoort afbeeldt op het aantal stuks ervan in de mand. Een fruitsoort
    waarvan het aantal op nul komt verdwijnt uit die dictionary, zodat len()
    en de operator in ze niet meer zien.

    Merk op dat __add__ en __sub__ op een kopie van de mand moeten werken: ze
    worden gebruikt in uitdrukkingen zoals mand_2 = mand_1 + 'mango', die
    mand_1 niet mogen wijzigen. Hun tegenhangers __iadd__ en __isub__
    wijzigen de mand zelf wel, en geven ze terug.

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

        self.fruit = {} if fruit is None else dict(fruit)

    def __repr__(self):

        fruit = ', '.join(
            f'{soort!r}: {self.fruit[soort]}' for soort in sorted(self.fruit)
        )
        return f'Fruitmand({{{fruit}}})'

    def __len__(self):

        return len(self.fruit)

    def __contains__(self, soort):

        return soort in self.fruit

    def __getitem__(self, soort):

        return self.fruit.get(soort, 0)

    def __setitem__(self, soort, aantal):

        if aantal > 0:
            self.fruit[soort] = aantal
        elif soort in self.fruit:
            del self.fruit[soort]

    def __add__(self, soort):

        mand = Fruitmand(self.fruit)
        mand[soort] = mand[soort] + 1
        return mand

    def __iadd__(self, soort):

        self[soort] = self[soort] + 1
        return self

    def __sub__(self, soort):

        mand = Fruitmand(self.fruit)
        mand[soort] = mand[soort] - 1
        return mand

    def __isub__(self, soort):

        self[soort] = self[soort] - 1
        return self

if __name__ == '__main__':
    import doctest
    doctest.testmod()
