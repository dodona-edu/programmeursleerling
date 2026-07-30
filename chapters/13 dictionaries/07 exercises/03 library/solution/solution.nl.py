"""
>>> boeken = [
...     ('Adams', 'Douglas', "The Hitchhiker's Guide to the Galaxy", 42),
...     ('Adams', 'Douglas', 'The Restaurant at the End of the Universe', 43),
...     ('Adams', 'Douglas', 'Life, the Universe and Everything', 44),
...     ('Rowling', 'Joanne', "Harry Potter and the Philosopher's Stone", 271),
...     ('Rowling', 'Joanne', 'Harry Potter and the Chamber of Secrets', 272),
...     ('Tolkien', 'John', 'The Hobbit', 137),
...     ('Spronck', 'Pieter', "The Coder's Apprentice", 512),
... ]
>>> bibliotheek = list2dict(boeken)
>>> bibliotheek[('Tolkien', 'John')]
{'The Hobbit': 137}
>>> bibliotheek[('Rowling', 'Joanne')]
{"Harry Potter and the Philosopher's Stone": 271, 'Harry Potter and the Chamber of Secrets': 272}
>>> locatie(bibliotheek, 'Adams', 'Douglas', 'Life, the Universe and Everything')
44
>>> locatie(bibliotheek, 'Adams', 'Douglas', 'The Long Dark Tea-Time of the Soul') is None
True
>>> titels(bibliotheek, 'Adams', 'Douglas')
['Life, the Universe and Everything', "The Hitchhiker's Guide to the Galaxy", 'The Restaurant at the End of the Universe']
>>> titels(bibliotheek, 'Pratchett', 'Terry')
[]
"""

def list2dict(boeken):

    bibliotheek = {}
    for achternaam, voornaam, titel, nummer in boeken:
        bibliotheek.setdefault((achternaam, voornaam), {})[titel] = nummer
    return bibliotheek

def locatie(bibliotheek, achternaam, voornaam, titel):

    return bibliotheek.get((achternaam, voornaam), {}).get(titel)

def titels(bibliotheek, achternaam, voornaam):

    return sorted(bibliotheek.get((achternaam, voornaam), {}))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
