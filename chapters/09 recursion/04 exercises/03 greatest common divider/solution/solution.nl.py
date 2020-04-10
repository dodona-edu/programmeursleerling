def ggd(m, n):

    """
    >>> ggd(14, 21)
    7
    """

    if m % n == 0:
        return n

    return ggd(n, m % n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()