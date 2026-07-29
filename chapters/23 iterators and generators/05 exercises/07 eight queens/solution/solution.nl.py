from itertools import permutations

def koninginnen(aantal=8):

    """
    >>> sorted(koninginnen(4))
    [(1, 3, 0, 2), (2, 0, 3, 1)]

    >>> len(list(koninginnen()))
    92
    """

    for posities in permutations(range(aantal)):
        if all(abs(posities[i] - posities[j]) not in (0, j - i)
               for i in range(aantal) for j in range(i + 1, aantal)):
            yield posities

if __name__ == '__main__':
    import doctest
    doctest.testmod()
