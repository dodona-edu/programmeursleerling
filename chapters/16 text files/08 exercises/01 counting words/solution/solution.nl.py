"""
>>> woorden_splitsen('data.txt')
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'And', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> woorden_tellen('data.txt')
{'how': 1, 'much': 3, 'wood': 3, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}
"""

def woorden_splitsen(bestandsnaam):

    woord = ''
    woorden = []
    for regel in open(bestandsnaam, 'r'):
        for karakter in regel:
            if karakter.isalpha():
                woord += karakter
            else:
                if woord:
                    woorden.append(woord)
                woord = ''

        if woord:
            woorden.append(woord)

    return woorden

def woorden_tellen(bestandsnaam):

    woorden = {}
    for woord in map(str.lower, woorden_splitsen(bestandsnaam)):
        woorden[woord] = woorden.get(woord, 0) + 1

    return woorden

if __name__ == '__main__':
    import doctest
    doctest.testmod()
