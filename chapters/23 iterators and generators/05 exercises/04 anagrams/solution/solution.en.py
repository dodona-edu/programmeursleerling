import itertools

def unique_anagrams(word):

    """
    >>> sorted(unique_anagrams("bee"))
    ['bee', 'ebe', 'eeb']

    >>> sorted(unique_anagrams("cat"))
    ['act', 'atc', 'cat', 'cta', 'tac', 'tca']
    """

    seen = set()
    for permutation in itertools.permutations(word):
        anagram = ''.join(permutation)
        if anagram not in seen:
            seen.add(anagram)
            yield anagram

if __name__ == '__main__':
    import doctest
    doctest.testmod()
