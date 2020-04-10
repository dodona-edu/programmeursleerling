def fib(number):

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

    if number < 2:
        return number

    return fib(number - 1) + fib(number - 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
