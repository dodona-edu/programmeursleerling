def tel_letters(tekst):

    """
    >>> tel_letters('Hello, World!')
    l: 3
    o: 2
    d: 1
    e: 1
    h: 1
    r: 1
    w: 1
    """

    # tel hoe vaak elke letter voorkomt, zonder onderscheid tussen hoofd- en
    # kleine letters en zonder rekening te houden met andere tekens
    letters = []
    aantallen = []
    for teken in tekst.lower():
        if teken.isalpha():
            if teken in letters:
                aantallen[letters.index(teken)] += 1
            else:
                letters.append(teken)
                aantallen.append(1)

    # sorteer de letters van veel naar weinig voorkomend, en alfabetisch als ze
    # even vaak voorkomen
    paren = sorted(zip(letters, aantallen), key=lambda paar: (-paar[1], paar[0]))

    # druk elke letter samen met haar aantal af
    for letter, aantal in paren:
        print(f'{letter}: {aantal}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
