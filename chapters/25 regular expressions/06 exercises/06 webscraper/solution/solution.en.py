import re

def webscraper(filename):

    """
    >>> webscraper('data.html')
    [(123123123, 'Groucho Marx'), (123123124, 'Harpo Marx'), (123123125, 'Chico Marx'), (123123126, 'Zeppo Marx'), (123123127, 'Gummo Marx')]
    """

    pattern = re.compile(r'<id>([^<]+)</id><name>([^<]+)</name>')
    return [(int(mo[0]), mo[1]) for mo in pattern.findall(open(filename).read())]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
