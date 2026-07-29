def anagrams(word):

    """
    >>> sorted(anagrams('ab'))
    ['ab', 'ba']
    >>> sorted(set(anagrams('eve')))
    ['eev', 'eve', 'vee']
    """

    if len(word) <= 1:
        yield word
        return

    for index, letter in enumerate(word):
        remainder = word[:index] + word[index + 1:]
        for anagram in anagrams(remainder):
            yield letter + anagram

if __name__ == '__main__':
    import doctest
    doctest.testmod()
