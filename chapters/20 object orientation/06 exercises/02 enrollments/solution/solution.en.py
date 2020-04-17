"""
>>> astronomy = Course(238273, 'Astronomy')
>>> astronomy
Course(238273, 'Astronomy')
>>> print(astronomy)
Course(238273, 'Astronomy')

>>> import datetime
>>> harry = Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> harry
Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> print(harry)
Potter, Harry
>>> harry.age()
39
>>> harry.courses()
set()
>>> harry.enroll(charms)
Student(29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31))
>>> harry.courses()
{Course(983448, 'Charms')}
>>> harry.enroll(charms).enroll(dark_arts).enroll(defence_against_dark_arts).courses()
{Course(746473, 'Dark Arts'), Course(983448, 'Charms'), Course(462763, 'Defence Against Dark Arts')}
"""

from datetime import date

class Course:

    def __init__(self, id, name):

        self.id = id
        self.name = name

    def __repr__(self):

        return f'Course({self.id!r}, {self.name!r})'

    def __eq__(self, other):

        return (self.id, self.name) == (other.id, other.name)

class Student:

    def __init__(self, id, firstname, lastname, birthdate):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self._courses = set()

    def __repr__(self):

        return f'Student({self.id}, {self.firstname!r}, {self.lastname!r}, {self.birthdate!r})'

    def __str__( self ):

        return f'{self.lastname}, {self.firstname}'

    def __eq__(self, other):

        return (self.id, self.firstname, self.lastname, self.birthdate) == (other.id, other.firstname, other.lastname, other.birthdate)

    def age(self):

        today = date.today()
        years = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            years -= 1

        return years

    def enroll(self, course):

        self._courses.add(course)

        return self

    def courses(self):

        return set(self._courses)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
