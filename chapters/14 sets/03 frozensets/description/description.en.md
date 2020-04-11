Python kent als variant op het set type de `frozenset`. Je creëert een
`frozenset` via de `frozenset()` functie. De elementen van een
`frozenset` kunnen niet veranderd worden. Je creëert dus een `frozenset`
onmiddellijk als je de `frozenset()` functie aanroept, want zodra de
`frozenset` bestaat kun je geen elementen meer toevoegen of weghalen.
Met andere woorden, `frozenset`s zijn onveranderbaar.

Alle reguliere set methodes werken ook op `frozenset`s, behalve de
methodes die proberen de set te veranderen. Als je een dergelijke
methode probeert aan te roepen voor een `frozenset` krijg je een syntax
error.

```python
fruit1 = frozenset( ["appel", "banaan", "kers"] )
fruit2 = frozenset( ["banaan", "kers", "doerian"] )

print( fruit1.union( fruit2 ) )
```
