def faculteit(n):

    """
    >>> faculteit(5)
    120
    """

    resultaat = 1
    for factor in range(1, n + 1):
        resultaat *= factor

    return resultaat

def binomiaal(n, k):

    """
    >>> binomiaal(7, 3)
    35
    """

    if not 0 <= k <= n:
        return 0

    return faculteit(n) // (faculteit(k) * faculteit(n - k))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
