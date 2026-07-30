def faculteiten(aantal=10):

    """
    >>> list(faculteiten())
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    >>> list(faculteiten(5))
    [1, 2, 6, 24, 120]
    >>> list(faculteiten(0))
    []
    """

    for n in range(1, aantal + 1):
        yield

if __name__ == '__main__':
    import doctest
    doctest.testmod()
