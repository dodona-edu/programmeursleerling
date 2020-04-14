"""
>>> films_list = [
...     ('Monty Python and the Holy Grail', (9, 10, 9.5, 8.5, 3, 7.5, 8)),
...     ("Monty Python's Life of Brian", (10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9)),
...     ("Monty Python's Meaning of Life", (7, 6, 5)),
...     ('And Now For Something Completely Different', (6, 5, 6, 6)),
... ]
>>> films_dict = list2dict(films_list)
>>> films_dict['Monty Python and the Holy Grail']
(9, 10, 9.5, 8.5, 3, 7.5, 8)
>>> films_dict["Monty Python's Life of Brian"]
(10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9)
>>> beoordeling = gemiddelde_beoordeling(films_dict)
>>> beoordeling['Monty Python and the Holy Grail']
7.928571428571429
>>> beoordeling["Monty Python's Life of Brian"]
6.85
"""

def gemiddelde(waarden):

    """
    >>> gemiddelde((9, 10, 9.5, 8.5, 3, 7.5, 8))
    7.928571428571429
    """

    return sum(waarden) / len(waarden)

def list2dict(films):

    return dict(films)

def gemiddelde_beoordeling(films):

    return {
        naam: gemiddelde(beoordelingen)
        for naam, beoordelingen in films.items()
    }

if __name__ == '__main__':
    import doctest
    doctest.testmod()
