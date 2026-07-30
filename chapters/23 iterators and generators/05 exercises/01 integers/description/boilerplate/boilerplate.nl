def niet_deelbaar(delers):

    """
    >>> list(niet_deelbaar([2, 3]))[:5]
    [1, 5, 7, 11, 13]
    >>> list(niet_deelbaar([1]))
    []
    """

    for n in range(1, 101):
        yield

if __name__ == '__main__':
    import doctest
    doctest.testmod()
