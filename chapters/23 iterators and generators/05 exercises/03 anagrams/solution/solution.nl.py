def anagrammen(woord):

    """
    >>> sorted(anagrammen('ab'))
    ['ab', 'ba']
    >>> sorted(set(anagrammen('eve')))
    ['eev', 'eve', 'vee']
    """

    if len(woord) <= 1:
        yield woord
        return

    for index, letter in enumerate(woord):
        rest = woord[:index] + woord[index + 1:]
        for anagram in anagrammen(rest):
            yield letter + anagram

if __name__ == '__main__':
    import doctest
    doctest.testmod()
