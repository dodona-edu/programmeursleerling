Schrijf een programma dat de
gebruiker vraagt om positieve integers in te geven. De gebruiker mag er
zoveel ingeven als gewenst, en geeft aan dat de laatste integer is
ingegeven door nul in te geven. Het programma toont vervolgens alle
getallen tussen 1 en 100 die niet deelbaar zijn door ieder van de
integers die zijn ingegeven. Toon die getallen middels een
`for ... in ...` loop, waarbij je gebruik maakt van een iterator om de
getallen te produceren.

### Opgave

Schrijf een **generatorfunctie** `niet_deelbaar` waaraan één argument moet
doorgegeven worden, een lijst van positieve integers (`delers`). De functie
moet elke integer van 1 tot en met 100 die niet deelbaar is door één van de
integers in `delers` **yielden**, in stijgende volgorde.

Omdat `niet_deelbaar` een generatorfunctie is, wordt er bij het aanroepen
niets onmiddellijk berekend: er wordt een iterator teruggegeven die de
getallen één voor één, op aanvraag, produceert, net zoals in de
`for ... in ...` loop hierboven.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> g = niet_deelbaar([2, 3])
>>> next(g)
1
>>> next(g)
5
>>> next(g)
7

>>> list(niet_deelbaar([1]))
[]
```
