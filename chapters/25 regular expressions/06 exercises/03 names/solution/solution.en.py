import re

def names(filename):

    """
    >>> names('data.en.txt')
    ['Monty Python', 'Flying Circus', 'Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Monty Python', 'Holy Grail', 'The Meaning', 'North\nAmerica', 'Saturday Night']
    """

    pattern = re.compile(r'\b([A-Z][a-z]*\s+[A-Z][a-z]*)\b')
    return pattern.findall(open(filename).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
