import re

def woorden_splitsen(bestandsnaam):

    """
    >>> woorden_splitsen('data.nl.txt')
    ['Monty', 'Python', 's', 'Flying', 'Circus', 'werd', 'uitgezonden', 'door', 'de', 'BBC', 'tussen', 'en', 'en', 'werd', 'bedacht', 'geschreven', 'en', 'uitgevoerd', 'door', 'haar', 'leden', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'en', 'Michael', 'Palin']
    """

    patroon = re.compile(r'[A-Za-z]+')
    return patroon.findall(open(bestandsnaam).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
