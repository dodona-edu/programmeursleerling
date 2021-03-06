import string

def letters_tellen(bestandsnaam):

    """
    >>> letters_tellen('data_a.txt')
    {'a': 9, 'b': 0, 'c': 24, 'd': 15, 'e': 3, 'f': 2, 'g': 0, 'h': 16, 'i': 2, 'j': 0, 'k': 9, 'l': 7, 'm': 3, 'n': 1, 'o': 22, 'p': 0, 'q': 0, 'r': 0, 's': 4, 't': 0, 'u': 19, 'v': 0, 'w': 12, 'x': 0, 'y': 0, 'z': 0}
    >>> letters_tellen('data_b.txt')
    {'a': 62, 'b': 33, 'c': 17, 'd': 33, 'e': 81, 'f': 10, 'g': 21, 'h': 61, 'i': 37, 'j': 9, 'k': 8, 'l': 30, 'm': 26, 'n': 36, 'o': 54, 'p': 3, 'q': 0, 'r': 34, 's': 38, 't': 67, 'u': 21, 'v': 6, 'w': 24, 'x': 1, 'y': 17, 'z': 0}
    >>> letters_tellen('data_c.txt')
    {'a': 36, 'b': 4, 'c': 7, 'd': 7, 'e': 40, 'f': 9, 'g': 5, 'h': 27, 'i': 14, 'j': 0, 'k': 1, 'l': 14, 'm': 18, 'n': 27, 'o': 37, 'p': 3, 'q': 0, 'r': 21, 's': 15, 't': 41, 'u': 8, 'v': 0, 'w': 12, 'x': 0, 'y': 9, 'z': 0}
    """

    # dictionary initialiseren
    letters = {letter: 0 for letter in string.ascii_lowercase}

    # dictionary aanvullen
    with open(bestandsnaam) as tekst:
        for regel in tekst:
            for karakter in regel.lower():
                if karakter.isalpha():
                    letters[karakter] += 1

    # dictionary teruggeven
    return letters

def letterfrequentie(bestandsnaam):

    """
    >>> letterfrequentie('data_a.txt')
    {'a': 0.060810810810810814, 'b': 0.0, 'c': 0.16216216216216217, 'd': 0.10135135135135136, 'e': 0.02027027027027027, 'f': 0.013513513513513514, 'g': 0.0, 'h': 0.10810810810810811, 'i': 0.013513513513513514, 'j': 0.0, 'k': 0.060810810810810814, 'l': 0.0472972972972973, 'm': 0.02027027027027027, 'n': 0.006756756756756757, 'o': 0.14864864864864866, 'p': 0.0, 'q': 0.0, 'r': 0.0, 's': 0.02702702702702703, 't': 0.0, 'u': 0.12837837837837837, 'v': 0.0, 'w': 0.08108108108108109, 'x': 0.0, 'y': 0.0, 'z': 0.0}
    >>> letterfrequentie('data_b.txt')
    {'a': 0.0850480109739369, 'b': 0.04526748971193416, 'c': 0.023319615912208505, 'd': 0.04526748971193416, 'e': 0.1111111111111111, 'f': 0.013717421124828532, 'g': 0.02880658436213992, 'h': 0.08367626886145405, 'i': 0.05075445816186557, 'j': 0.012345679012345678, 'k': 0.010973936899862825, 'l': 0.0411522633744856, 'm': 0.03566529492455418, 'n': 0.04938271604938271, 'o': 0.07407407407407407, 'p': 0.00411522633744856, 'q': 0.0, 'r': 0.04663923182441701, 's': 0.05212620027434842, 't': 0.09190672153635117, 'u': 0.02880658436213992, 'v': 0.00823045267489712, 'w': 0.03292181069958848, 'x': 0.0013717421124828531, 'y': 0.023319615912208505, 'z': 0.0}
    >>> letterfrequentie('data_c.txt')
    {'a': 0.10140845070422536, 'b': 0.011267605633802818, 'c': 0.01971830985915493, 'd': 0.01971830985915493, 'e': 0.11267605633802817, 'f': 0.02535211267605634, 'g': 0.014084507042253521, 'h': 0.07605633802816901, 'i': 0.03943661971830986, 'j': 0.0, 'k': 0.0028169014084507044, 'l': 0.03943661971830986, 'm': 0.05070422535211268, 'n': 0.07605633802816901, 'o': 0.10422535211267606, 'p': 0.008450704225352112, 'q': 0.0, 'r': 0.059154929577464786, 's': 0.04225352112676056, 't': 0.11549295774647887, 'u': 0.022535211267605635, 'v': 0.0, 'w': 0.03380281690140845, 'x': 0.0, 'y': 0.02535211267605634, 'z': 0.0}
    """

    telling = letters_tellen(bestandsnaam)
    totaal = sum(telling.values())

    return {
        letter: aantal / totaal
        for letter, aantal in telling.items()
    }

def letterfrequenties(tekst1, tekst2, tekst3, resultaat):

    """
    >>> letterfrequenties('data_a.txt', 'data_b.txt', 'data_c.txt', 'data.csv')
    >>> print(open('data.csv').read(), end='')
    a,0.06081,0.08505,0.10141
    b,0.00000,0.04527,0.01127
    c,0.16216,0.02332,0.01972
    d,0.10135,0.04527,0.01972
    e,0.02027,0.11111,0.11268
    f,0.01351,0.01372,0.02535
    g,0.00000,0.02881,0.01408
    h,0.10811,0.08368,0.07606
    i,0.01351,0.05075,0.03944
    j,0.00000,0.01235,0.00000
    k,0.06081,0.01097,0.00282
    l,0.04730,0.04115,0.03944
    m,0.02027,0.03567,0.05070
    n,0.00676,0.04938,0.07606
    o,0.14865,0.07407,0.10423
    p,0.00000,0.00412,0.00845
    q,0.00000,0.00000,0.00000
    r,0.00000,0.04664,0.05915
    s,0.02703,0.05213,0.04225
    t,0.00000,0.09191,0.11549
    u,0.12838,0.02881,0.02254
    v,0.00000,0.00823,0.00000
    w,0.08108,0.03292,0.03380
    x,0.00000,0.00137,0.00000
    y,0.00000,0.02332,0.02535
    z,0.00000,0.00000,0.00000
    """

    freq1 = letterfrequentie(tekst1)
    freq2 = letterfrequentie(tekst2)
    freq3 = letterfrequentie(tekst3)

    with open(resultaat, 'w') as resultaat:
        for letter in string.ascii_lowercase:
            print(f'{letter},{freq1[letter]:.5f},{freq2[letter]:.5f},{freq3[letter]:.5f}', file=resultaat)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
