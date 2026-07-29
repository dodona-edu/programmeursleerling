import itertools

def sub_dictionaries(dictionary):

    """
    >>> sorted(sorted(sub.items()) for sub in sub_dictionaries({'a': 1, 'b': 2}))
    [[], [('a', 1)], [('a', 1), ('b', 2)], [('b', 2)]]
    >>> sub_dictionaries({})
    [{}]
    """

    result = []
    items = list(dictionary.items())
    for length in range(len(items) + 1):
        for combination in itertools.combinations(items, length):
            result.append(dict(combination))

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
