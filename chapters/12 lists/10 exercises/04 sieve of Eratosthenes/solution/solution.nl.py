def zeef(n):

    """
    >>> zeef(10)
    [2, 3, 5, 7]
    >>> zeef(1)
    []
    """

    # begin met de reeks getallen van 0 tot en met n
    getallen = list(range(max(n + 1, 0)))

    # 0 en 1 zijn geen priemgetallen
    for index in range(min(2, len(getallen))):
        getallen[index] = 0

    # zet alle veelvouden van elk getal dat nog op de list staat op nul
    for getal in range(2, len(getallen)):
        if getallen[getal] != 0:
            for veelvoud in range(2 * getal, len(getallen), getal):
                getallen[veelvoud] = 0

    # de getallen die overblijven op de list zijn de priemgetallen
    return [getal for getal in getallen if getal != 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
