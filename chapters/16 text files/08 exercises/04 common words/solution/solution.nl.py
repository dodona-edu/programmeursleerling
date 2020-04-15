"""
>>> gemeenschappelijke_woorden('data_a.txt', 'data_b.txt', 'data_c.txt')
{'and', 'as', 'he'}
"""

def woorden_splitsen(bestandsnaam):

    woord = ''
    woorden = set()
    for regel in open(bestandsnaam, 'r'):
        for karakter in regel:
            if karakter.isalpha():
                woord += karakter
            else:
                if woord:
                    woorden.add(woord.lower())
                woord = ''

        if woord:
            woorden.add(woord.lower())

    return woorden

def gemeenschappelijke_woorden(bestandsnaam1, bestandsnaam2, bestandsnaam3):

    woorden = woorden_splitsen(bestandsnaam1)
    woorden &= woorden_splitsen(bestandsnaam2)
    woorden &= woorden_splitsen(bestandsnaam3)

    return woorden

if __name__ == '__main__':
    import doctest
    doctest.testmod()
