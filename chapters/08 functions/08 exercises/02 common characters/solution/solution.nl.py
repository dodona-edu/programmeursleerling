def gemeenschappelijke_karakters(woord1, woord2):

    """
    >>> gemeenschappelijke_karakters('een', 'twee')
    1
    """

    aantal = 0
    gemeenschappelijke_karakters = ''
    for karakter in woord1:
        if karakter in woord2 and karakter not in gemeenschappelijke_karakters:
            aantal += 1
            gemeenschappelijke_karakters += karakter

    return aantal

if __name__ == '__main__':
    import doctest
    doctest.testmod()
