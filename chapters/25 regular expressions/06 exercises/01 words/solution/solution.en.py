import re

def word_split(filename):

    """
    >>> word_split('data.en.txt')
    ['Broadcast', 'by', 'the', 'BBC', 'between', 'and', 'Monty', 'Python', 's', 'Flying', 'Circus', 'was', 'conceived', 'written', 'and', 'performed', 'by', 'its', 'members', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'and', 'Michael', 'Palin']
    """

    pattern = re.compile(r'[A-Za-z]+')
    return pattern.findall(open(filename).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
