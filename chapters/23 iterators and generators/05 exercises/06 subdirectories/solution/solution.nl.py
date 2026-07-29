import itertools

def sub_dictionaries(dictionary):

    """
    >>> sorted(sorted(sub.items()) for sub in sub_dictionaries({'a': 1, 'b': 2}))
    [[], [('a', 1)], [('a', 1), ('b', 2)], [('b', 2)]]
    >>> sub_dictionaries({})
    [{}]
    """

    resultaat = []
    items = list(dictionary.items())
    for lengte in range(len(items) + 1):
        for combinatie in itertools.combinations(items, lengte):
            resultaat.append(dict(combinatie))

    return resultaat

if __name__ == '__main__':
    import doctest
    doctest.testmod()
