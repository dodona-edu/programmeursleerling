from itertools import combinations

def zero_subsets(numbers):

    """
    >>> sorted(zero_subsets([1, 4, -3, -5, 7]))
    [(1, -3, -5, 7), (1, 4, -5)]

    >>> sorted(zero_subsets([1, 4, -3, 7]))
    []
    """

    for size in range(1, len(numbers) + 1):
        for subset in combinations(numbers, size):
            if sum(subset) == 0:
                yield subset

if __name__ == '__main__':
    import doctest
    doctest.testmod()
