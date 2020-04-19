import re

def zoek_de_de(bestandsnaam):

    """
    >>> zoek_de_de('data.nl.txt')
    ['de', 'de', 'de', 'de', 'de', 'de', 'de', 'de', 'de', 'de', 'De']
    """

    patroon = re.compile(r'\bde\b', re.IGNORECASE)
    return patroon.findall(open(bestandsnaam).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
