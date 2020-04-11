def product(complex1, complex2):

    """
    >>> product((3, 4), (7, 2))
    (13, 34)
    """

    a, b = complex1
    c, d = complex2

    return a * c - b * d, a * d + b * c

if __name__ == '__main__':
    import doctest
    doctest.testmod()
