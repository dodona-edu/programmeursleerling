class FruitBasket:

    """
    The pieces of fruit are kept in a dictionary that maps the name of a
    fruit onto the number of pieces of it in the basket. A fruit whose
    number drops to zero disappears from that dictionary, so that len() and
    the in operator never see it again.

    Note that __add__ and __sub__ have to work on a copy of the basket: they
    are used in expressions such as basket_2 = basket_1 + 'mango', which are
    not supposed to change basket_1. Their in place counterparts __iadd__
    and __isub__ do change the basket itself, and return it.

    >>> basket = FruitBasket({'mango': 2})
    >>> basket
    FruitBasket({'mango': 2})
    >>> len(basket)
    1
    >>> basket['mango']
    2
    >>> basket['kiwi']
    0
    >>> 'kiwi' in basket
    False
    >>> basket['kiwi'] = 3
    >>> basket + 'kiwi'
    FruitBasket({'kiwi': 4, 'mango': 2})
    >>> basket
    FruitBasket({'kiwi': 3, 'mango': 2})
    >>> basket -= 'mango'
    >>> basket -= 'mango'
    >>> basket
    FruitBasket({'kiwi': 3})
    >>> basket - 'papaya'
    FruitBasket({'kiwi': 3})
    """

    def __init__(self, fruits=None):

        self.fruits = {} if fruits is None else dict(fruits)

    def __repr__(self):

        fruits = ', '.join(
            f'{fruit!r}: {self.fruits[fruit]}' for fruit in sorted(self.fruits)
        )
        return f'FruitBasket({{{fruits}}})'

    def __len__(self):

        return len(self.fruits)

    def __contains__(self, fruit):

        return fruit in self.fruits

    def __getitem__(self, fruit):

        return self.fruits.get(fruit, 0)

    def __setitem__(self, fruit, number):

        if number > 0:
            self.fruits[fruit] = number
        elif fruit in self.fruits:
            del self.fruits[fruit]

    def __add__(self, fruit):

        basket = FruitBasket(self.fruits)
        basket[fruit] = basket[fruit] + 1
        return basket

    def __iadd__(self, fruit):

        self[fruit] = self[fruit] + 1
        return self

    def __sub__(self, fruit):

        basket = FruitBasket(self.fruits)
        basket[fruit] = basket[fruit] - 1
        return basket

    def __isub__(self, fruit):

        self[fruit] = self[fruit] - 1
        return self

if __name__ == '__main__':
    import doctest
    doctest.testmod()
