def afvlakken(genest):

    """
    >>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
    >>> afvlakken(inttuple)
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    """

    plat = tuple()
    for element in genest:
        if isinstance(element, tuple):
            plat += afvlakken(element)
        else:
            plat += element,

    return plat

if __name__ == '__main__':
    import doctest
    doctest.testmod()
