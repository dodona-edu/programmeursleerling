def factorial(n):

    """
    >>> factorial(5)
    120
    """

    result = 1
    for factor in range(1, n + 1):
        result *= factor

    return result

def binomial(n, k):

    """
    >>> binomial(7, 3)
    35
    """

    if not 0 <= k <= n:
        return 0

    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
