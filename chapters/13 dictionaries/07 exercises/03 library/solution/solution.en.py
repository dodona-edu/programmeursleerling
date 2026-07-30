"""
>>> books = [
...     ('Adams', 'Douglas', "The Hitchhiker's Guide to the Galaxy", 42),
...     ('Adams', 'Douglas', 'The Restaurant at the End of the Universe', 43),
...     ('Adams', 'Douglas', 'Life, the Universe and Everything', 44),
...     ('Rowling', 'Joanne', "Harry Potter and the Philosopher's Stone", 271),
...     ('Rowling', 'Joanne', 'Harry Potter and the Chamber of Secrets', 272),
...     ('Tolkien', 'John', 'The Hobbit', 137),
...     ('Spronck', 'Pieter', "The Coder's Apprentice", 512),
... ]
>>> library = list2dict(books)
>>> library[('Tolkien', 'John')]
{'The Hobbit': 137}
>>> library[('Rowling', 'Joanne')]
{"Harry Potter and the Philosopher's Stone": 271, 'Harry Potter and the Chamber of Secrets': 272}
>>> location(library, 'Adams', 'Douglas', 'Life, the Universe and Everything')
44
>>> location(library, 'Adams', 'Douglas', 'The Long Dark Tea-Time of the Soul') is None
True
>>> titles(library, 'Adams', 'Douglas')
['Life, the Universe and Everything', "The Hitchhiker's Guide to the Galaxy", 'The Restaurant at the End of the Universe']
>>> titles(library, 'Pratchett', 'Terry')
[]
"""

def list2dict(books):

    library = {}
    for last_name, first_name, title, number in books:
        writer = (last_name, first_name)
        if writer not in library:
            library[writer] = {}
        library[writer][title] = number
    return library

def location(library, last_name, first_name, title):

    return library.get((last_name, first_name), {}).get(title)

def titles(library, last_name, first_name):

    titlelist = list(library.get((last_name, first_name), {}).keys())
    titlelist.sort()
    return titlelist

if __name__ == '__main__':
    import doctest
    doctest.testmod()
