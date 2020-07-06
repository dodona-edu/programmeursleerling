def discriminant(a, b, c):

    """
    >>> discriminant(1, 0, -1)
    4.0
    >>> discriminant(1, 4, -5)
    36.0
    """

    return float(b ** 2 - 4 * a * c)

def oplossingen(a, b, c):

    """
    >>> oplossingen(1, 0, -1)
    (1, -1.0, 1.0)
    >>> oplossingen(1, 4, -5)
    (1, -5.0, 1.0)
    """

    D = discriminant(a, b, c)
    if abs(D) < 1e-6:
        aantal = 1
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = x1
    elif D > 0:
        aantal = 2
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a)
    else:
        aantal = 0
        x1 = 0
        x2 = 0

    return aantal, x1, x2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
