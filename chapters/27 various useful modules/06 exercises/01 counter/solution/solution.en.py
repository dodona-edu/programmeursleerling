from collections import Counter

def most_common_letters(text):

    """
    >>> most_common_letters('mississippi')
    [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
    """

    letters = [character.lower() for character in text if character.isalpha()]
    return Counter(letters).most_common(5)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
