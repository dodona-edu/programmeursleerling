import re

def quotes(filename):

    """
    >>> quotes('data.en.txt')
    ['Pythonesque']
    """

    pattern = re.compile(r'"([^"]*)"')
    return pattern.findall(open(filename).read())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
