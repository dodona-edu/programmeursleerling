def discriminant(a, b, c):

    """
    >>> discriminant(1, 0, -1)
    4.0
    >>> discriminant(1, 4, -5)
    36.0
    """

    return float(b ** 2 - 4 * a * c)

def solutions(a, b, c):

    """
    >>> solutions(1, 0, -1)
    (1, -1.0, 1.0)
    >>> solutions(1, 4, -5)
    (1, -5.0, 1.0)
    """

    D = discriminant(a, b, c)
    if abs(D) < 1e-6:
        count = 1
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = x1
    elif D > 0:
        count = 2
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a)
    else:
        count = 0
        x1 = 0
        x2 = 0

    return count, x1, x2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
