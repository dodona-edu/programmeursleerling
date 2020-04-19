import re

def citaten(bestandsnaam):

    """
    >>> citaten('data.nl.txt')
    ['Pythonesque']
    """

    patroon = re.compile(r'"([^"]*)"')
    return patroon.findall(open(bestandsnaam).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
