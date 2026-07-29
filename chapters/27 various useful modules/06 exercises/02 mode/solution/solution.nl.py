from collections import Counter
from statistics import mean, median

def modus(getallen):

    """
    >>> modus([1, 2, 2, 3])
    [2]
    """

    if not getallen:
        return []

    tellingen = Counter(getallen)
    hoogste = tellingen.most_common(1)[0][1]
    if hoogste < 2:
        return []

    return sorted(getal for getal, telling in tellingen.items() if telling == hoogste)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    getallen = []
    while True:
        getal = int(input('Geef een getal (0 om te stoppen): '))
        if getal == 0:
            break
        getallen.append(getal)

    print('gemiddelde:', mean(getallen))
    print('mediaan:', median(getallen))
    modi = modus(getallen)
    if modi:
        print('modus:', ', '.join(str(getal) for getal in modi))
    else:
        print('er is geen modus')
