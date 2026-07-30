"""
>>> astronomy = Cursus(238273, 'Astronomy')
>>> astronomy
Cursus(238273, 'Astronomy')
>>> print(astronomy)
Cursus(238273, 'Astronomy')

>>> import datetime
>>> harry = Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> harry
Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> print(harry)
Potter, Harry
>>> harry.leeftijd()
39
>>> harry.cursussen()
set()
>>> charms = Cursus(983448, 'Charms')
>>> dark_arts = Cursus(746473, 'Dark Arts')
>>> defence_against_dark_arts = Cursus(462763, 'Defence Against Dark Arts')
>>> harry.inschrijven(charms)
Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> harry.cursussen()
{Cursus(983448, 'Charms')}
>>> harry.inschrijven(charms).inschrijven(dark_arts).inschrijven(defence_against_dark_arts).cursussen()
{Cursus(746473, 'Dark Arts'), Cursus(983448, 'Charms'), Cursus(462763, 'Defence Against Dark Arts')}
"""

class Cursus:

    def __init__(self, id, naam):

        pass

    def __repr__(self):

        pass

class Student:

    def __init__(self, id, voornaam, familienaam, geboortedatum):

        pass

    def __repr__(self):

        pass

    def __str__(self):

        pass

    def leeftijd(self):

        pass

    def inschrijven(self, cursus):

        pass

    def cursussen(self):

        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
