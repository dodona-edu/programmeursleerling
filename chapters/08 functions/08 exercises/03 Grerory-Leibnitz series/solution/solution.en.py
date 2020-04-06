def gregory_leibnitz(terms):

    """
    >>> gregory_leibnitz(1)
    4.0
    >>> gregory_leibnitz(10)
    3.0418396189294032
    >>> gregory_leibnitz(100)
    3.1315929035585537
    >>> gregory_leibnitz(1000)
    3.140592653839794
    """

    som = 0
    for index in range(terms):
        som += 1 / (2 * index + 1) * (-1) ** index

    return 4 * som

if __name__ == '__main__':
    import doctest
    doctest.testmod()
