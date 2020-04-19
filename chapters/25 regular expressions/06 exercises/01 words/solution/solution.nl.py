import re

def woorden_splitsen(bestandsnaam):

    """
    >>> woorden_splitsen('data.txt')
    ['Broadcast', 'by', 'the', 'BBC', 'between', 'and', 'Monty', 'Python', 's', 'Flying', 'Circus', 'was', 'conceived', 'written', 'and', 'performed', 'by', 'its', 'members', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'and', 'Michael', 'Palin']
    """

    patroon = re.compile(r'[A-Za-z]+')
    return patroon.findall(open(bestandsnaam).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
