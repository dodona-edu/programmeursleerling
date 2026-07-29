from itertools import combinations

def nulsom_deelverzamelingen(getallen):

    """
    >>> sorted(nulsom_deelverzamelingen([1, 4, -3, -5, 7]))
    [(1, -3, -5, 7), (1, 4, -5)]

    >>> sorted(nulsom_deelverzamelingen([1, 4, -3, 7]))
    []
    """

    for grootte in range(1, len(getallen) + 1):
        for deelverzameling in combinations(getallen, grootte):
            if sum(deelverzameling) == 0:
                yield deelverzameling

if __name__ == '__main__':
    import doctest
    doctest.testmod()
