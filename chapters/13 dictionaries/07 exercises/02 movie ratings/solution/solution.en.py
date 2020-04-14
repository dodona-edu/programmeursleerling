"""
>>> movies_list = [
...     ('Monty Python and the Holy Grail', (9, 10, 9.5, 8.5, 3, 7.5, 8)),
...     ("Monty Python's Life of Brian", (10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9)),
...     ("Monty Python's Meaning of Life", (7, 6, 5)),
...     ('And Now For Something Completely Different', (6, 5, 6, 6)),
... ]
>>> movies_dict = list2dict(movies_list)
>>> movies_dict['Monty Python and the Holy Grail']
(9, 10, 9.5, 8.5, 3, 7.5, 8)
>>> movies_dict["Monty Python's Life of Brian"]
(10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9)
>>> rating = average_rating(movies_dict)
>>> rating['Monty Python and the Holy Grail']
7.928571428571429
>>> rating["Monty Python's Life of Brian"]
6.85
"""

def average(values):

    """
    >>> average((9, 10, 9.5, 8.5, 3, 7.5, 8))
    7.928571428571429
    """

    return sum(values) / len(values)

def list2dict(movies):

    return {
        name: ratings
        for name, ratings in movies
    }

def average_rating(movies):

    return {
        name: average(ratings)
        for name, ratings in movies.items()
    }

if __name__ == '__main__':
    import doctest
    doctest.testmod()
