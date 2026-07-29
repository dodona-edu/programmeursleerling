from collections import Counter

def meest_voorkomende_letters(tekst):

    """
    >>> meest_voorkomende_letters('mississippi')
    [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
    """

    letters = [teken.lower() for teken in tekst if teken.isalpha()]
    return Counter(letters).most_common(5)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
