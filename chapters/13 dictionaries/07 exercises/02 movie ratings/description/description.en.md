What is the average rating of a movie?

### Assignment

**Data about movie ratings** is represented as a `list` of movies, with each movie represented as a `tuple` containing two elements: *i*) the name of the movie (`str`) and *ii*) a `tuple` containing one or more ratings (`int` of `float`) for that movie. Your task:

- Write a function `list2dict` that takes data about movie ratings. The function must return a dictionary (`dict`) that maps the name (`str`) of each movie onto the ratings (`tuple`) for that movie.

- Write a function `average_rating` that takes a dictionary (`dict`) formatted as the dictionaries returned by the function `list2dict`. The function must return a dictionary (`dict`) that maps the name (`str`) of each movie onto the average rating (`float`) for that movie.

### Example

```console?lang=python&prompt=>>>
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
```
