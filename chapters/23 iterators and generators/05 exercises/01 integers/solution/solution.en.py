def not_divisible(divisors):

    """
    >>> list(not_divisible([2, 3]))[:5]
    [1, 5, 7, 11, 13]
    >>> list(not_divisible([1]))
    []
    """

    for n in range(1, 101):
        if all(n % divisor != 0 for divisor in divisors):
            yield n

if __name__ == '__main__':
    import doctest
    doctest.testmod()
