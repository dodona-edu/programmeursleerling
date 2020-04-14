Wat is de gemiddelde beoordeling van een film?

### Opgave

**Data over filmboordelingen** worden voorgesteld als een lijst (`list`) met films waarin elke film wordt voorgesteld als een `tuple` met twee elementen: *i*) de naam van de film (`str`) en *ii*) een `tuple` met één of meer beoordelingen (`int` of `float`) die de film kreeg. Gevraagd wordt:

- Schrijf een functie `list2dict` waarin data over filmbeoordelingen moet doorgegeven worden. De functie moet een dictionary (`dict`) teruggeven die de naam (`str`) van elke film afbeeldt op de beoordelingen (`tuple`) die de film kreeg.

- Schrijf een functie `gemiddelde_beoordeling` waaraan een dictionary (`dict`) moet doorgegeven worden, die opgebouwd is als de dictionaries die door de functie `list2dict` teruggegeven worden. De functie moet een dictionary (`dict`) teruggeven die de naam (`str`) van elke film afbeeldt op de gemiddelde beoordeling (`float`) die de film kreeg.

### Voorbeeld

```console?lang=python&prompt=>>>
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
```
