def sum(complex1, complex2):

    """
    >>> sum((3, 4), (7, 2))
    (10, 6)
    """

    a, b = complex1
    c, d = complex2

    return a + c, b + d

if __name__ == '__main__':
    import doctest
    doctest.testmod()
