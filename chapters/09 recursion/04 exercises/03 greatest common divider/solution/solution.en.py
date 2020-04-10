def gcd(m, n):

    """
    >>> gcd(14, 21)
    7
    """

    if m % n == 0:
        return n

    return gcd(n, m % n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()