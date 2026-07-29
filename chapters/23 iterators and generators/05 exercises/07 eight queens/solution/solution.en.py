from itertools import permutations

def queens(number=8):

    """
    >>> sorted(queens(4))
    [(1, 3, 0, 2), (2, 0, 3, 1)]

    >>> len(list(queens()))
    92
    """

    for positions in permutations(range(number)):
        if all(abs(positions[i] - positions[j]) not in (0, j - i)
               for i in range(number) for j in range(i + 1, number)):
            yield positions

if __name__ == '__main__':
    import doctest
    doctest.testmod()
