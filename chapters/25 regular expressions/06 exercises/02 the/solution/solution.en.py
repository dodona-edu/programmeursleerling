import re

def find_the_the(filename):

    """
    >>> find_the_the('data.en.txt')
    ['the', 'the', 'the', 'the', 'The', 'the', 'the', 'the']
    """

    pattern = re.compile(r'\bthe\b', re.IGNORECASE)
    return pattern.findall(open(filename).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
