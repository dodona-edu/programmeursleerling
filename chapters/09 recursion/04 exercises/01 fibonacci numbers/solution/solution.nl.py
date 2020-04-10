def fib(getal):

    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    """

    if getal < 2:
        return getal

    return fib(getal - 1) + fib(getal - 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
