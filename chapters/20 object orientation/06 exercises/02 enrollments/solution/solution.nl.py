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
>>> harry.inschrijven(charms)
Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> harry.cursussen()
{Cursus(983448, 'Charms')}
>>> harry.inschrijven(charms).inschrijven(dark_arts).inschrijven(defence_against_dark_arts).cursussen()
{Cursus(746473, 'Dark Arts'), Cursus(983448, 'Charms'), Cursus(462763, 'Defence Against Dark Arts')}
"""

from datetime import date

class Cursus:

    def __init__(self, id, naam):

        self.id = id
        self.naam = naam

    def __repr__(self):

        return f'Cursus({self.id!r}, {self.naam!r})'

class Student:

    def __init__(self, id, voornaam, familienaam, geboortedatum):

        self.id = id
        self.voornaam = voornaam
        self.familienaam = familienaam
        self.geboortedatum = geboortedatum
        self._cursussen = set()

    def __repr__(self):

        return f'Student({self.id}, {self.voornaam!r}, {self.familienaam!r}, {self.geboortedatum!r})'

    def __str__( self ):

        return f'{self.familienaam}, {self.voornaam}'

    def leeftijd(self):

        vandaag = date.today()
        jaren = vandaag.year - self.geboortedatum.year
        if (vandaag.month, vandaag.day) < (self.geboortedatum.month, self.geboortedatum.day):
            jaren -= 1

        return jaren

    def inschrijven(self, cursus):

        self._cursussen.add(cursus)

        return self

    def cursussen(self):

        return set(self._cursussen)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
