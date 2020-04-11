def flatten(nested):

    """
    >>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
    >>> flatten(inttuple)
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    """

    flattened = tuple()
    for element in nested:
        if isinstance(element, tuple):
            flattened += flatten(element)
        else:
            flattened += element,

    return flattened

if __name__ == '__main__':
    import doctest
    doctest.testmod()
