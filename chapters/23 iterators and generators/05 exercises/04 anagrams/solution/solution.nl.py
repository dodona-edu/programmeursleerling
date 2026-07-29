import itertools

def unieke_anagrammen(woord):

    """
    >>> sorted(unieke_anagrammen("aap"))
    ['aap', 'apa', 'paa']

    >>> sorted(unieke_anagrammen("kat"))
    ['akt', 'atk', 'kat', 'kta', 'tak', 'tka']
    """

    gezien = set()
    for permutatie in itertools.permutations(woord):
        anagram = ''.join(permutatie)
        if anagram not in gezien:
            gezien.add(anagram)
            yield anagram

if __name__ == '__main__':
    import doctest
    doctest.testmod()
