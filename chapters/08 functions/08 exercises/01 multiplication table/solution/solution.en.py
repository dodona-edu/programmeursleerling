def multiplication_table(number):

    """
    >>> multiplication_table(12)
    1 * 12 = 12
    2 * 12 = 24
    3 * 12 = 36
    4 * 12 = 48
    5 * 12 = 60
    6 * 12 = 72
    7 * 12 = 84
    8 * 12 = 96
    9 * 12 = 108
    10 * 12 = 120
    """

    for factor in range(1, 11):
        print(f'{factor} * {number} = {factor * number}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
