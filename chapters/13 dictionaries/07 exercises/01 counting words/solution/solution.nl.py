"""
>>> tekst = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
>>> woorden_splitsen(tekst)
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'and', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> woorden = woorden_tellen(tekst)
>>> woorden['wood']
3
>>> woorden['chuck']
5
"""

def woorden_splitsen(tekst):

    woord = ''
    woorden = []
    for karakter in tekst:
        if karakter.isalpha():
            woord += karakter
        else:
            if woord:
                woorden.append(woord)
            woord = ''

    if woord:
        woorden.append(woord)

    return woorden

def woorden_tellen(tekst):

    woorden = {}
    for woord in map(str.lower, woorden_splitsen(tekst)):
        woorden[woord] = woorden.get(woord, 0) + 1

    return woorden

if __name__ == '__main__':
    import doctest
    doctest.testmod()
