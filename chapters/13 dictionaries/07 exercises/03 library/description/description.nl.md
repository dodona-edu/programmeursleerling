Een bibliotheek heeft boeken. Ieder boek
heeft een schrijver, die je kunt identificeren door achter- en voornaam.
Boeken hebben een titel. Boeken hebben ook een locatienummer dat
aangeeft waar ze staan in de bibliotheek. De bibliothecaris wil kunnen
vinden waar een boek staat als de schrijver en titel gekend zijn, en wil
ook alle boeken kunnen afdrukken die van een bepaalde schrijver zijn.

### Opgave

**Data over de boeken van een bibliotheek** worden voorgesteld als een lijst (`list`) met boeken waarin elk boek wordt voorgesteld als een `tuple` met vier elementen: *i*) de achternaam van de schrijver (`str`), *ii*) de voornaam van de schrijver (`str`), *iii*) de titel van het boek (`str`) en *iv*) het locatienummer van het boek (`int`). Gevraagd wordt:

- Schrijf een functie `list2dict` waaraan data over de boeken van een bibliotheek moet doorgegeven worden. De functie moet een dictionary (`dict`) teruggeven die de schrijver (`tuple` met de achternaam en de voornaam van de schrijver) van elk boek afbeeldt op een dictionary (`dict`) die de titel (`str`) van elk boek van die schrijver afbeeldt op het locatienummer (`int`) van dat boek.

- Schrijf een functie `locatie` waaraan een dictionary (`dict`) moet doorgegeven worden die opgebouwd is als de dictionaries die door de functie `list2dict` teruggegeven worden, gevolgd door de achternaam (`str`) van een schrijver, de voornaam (`str`) van die schrijver en de titel (`str`) van een boek. De functie moet het locatienummer (`int`) van dat boek teruggeven, of `None` als de bibliotheek dat boek niet heeft.

- Schrijf een functie `titels` waaraan een dictionary (`dict`) moet doorgegeven worden die opgebouwd is als de dictionaries die door de functie `list2dict` teruggegeven worden, gevolgd door de achternaam (`str`) en de voornaam (`str`) van een schrijver. De functie moet de gesorteerde lijst (`list`) met titels (`str`) teruggeven van de boeken die de bibliotheek van die schrijver heeft. Dit moet een lege lijst zijn als de bibliotheek geen boeken van die schrijver heeft.

### Voorbeeld

```console?lang=python&prompt=>>>
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
```
