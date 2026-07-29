Schrijf een programma
dat alle mogelijke sub-dictionaries produceert van een dictionary, en ze
opslaat in een list. Bijvoorbeeld, als de dictionary `\{"a":1,"b":2\}`
is, dan produceert het programma
`[\{\},\{"a":1\},\{"b":2\},\{"a":1,"b":2\}]` (de volgorde in de list
maakt niet uit). Gebruik de `itertools` module.

### Opgave

Schrijf een functie `sub_dictionaries` waaraan een `dict` moet
doorgegeven worden. De functie moet een `list` teruggeven met daarin
alle sub-dictionaries van die dictionary: elke dictionary die je kan
vormen door een deelverzameling van de key/value-paren van de
gegeven dictionary te behouden. Dit omvat ook de lege dictionary en de
volledige dictionary zelf. De volgorde van de sub-dictionaries in de
teruggegeven list maakt niet uit, en de volgorde van de key/value-paren
binnen elke sub-dictionary evenmin.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> sub_dictionaries({"a": 1, "b": 2})
[{}, {'a': 1}, {'b': 2}, {'a': 1, 'b': 2}]

>>> sorted(sorted(sub.items()) for sub in sub_dictionaries({"x": 3, "y": 8}))
[[], [('x', 3)], [('x', 3), ('y', 8)], [('y', 8)]]
```
