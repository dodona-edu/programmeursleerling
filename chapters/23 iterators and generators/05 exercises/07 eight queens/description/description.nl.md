Schrijf een programma dat
bepaalt hoe je acht koninginnen kunt plaatsen op een schaakbord op zo'n
manier dat geen van hen de anderen aanvalt. Dit is een klassiek probleem
dat lijkt weinig van doen te hebben met dit hoofdstuk, maar als je een
slimme manier bedenkt om het aan te pakken met de `permutations()`
functie, dan zul je zien dat dit een verrassend kort programma is.

### Opgave

Schrijf een generatorfunctie `koninginnen` waaraan optioneel een geheel
getal `aantal` (`int`) kan doorgegeven worden, met standaardwaarde `8`.
De functie moet met `yield` elke oplossing genereren om `aantal`
koninginnen te plaatsen op een schaakbord van `aantal` × `aantal`
velden, zodat geen enkele koningin een andere aanvalt.

Elke oplossing wordt voorgesteld als een tuple van lengte `aantal`. De
waarde op index $$i$$ van de tuple is de (0-based) kolom van de
koningin op rij $$i$$. Zo betekent de tuple `(1, 3, 0, 2)` dat de
koningin op rij 0 in kolom 1 staat, de koningin op rij 1 in kolom 3, de
koningin op rij 2 in kolom 0, en de koningin op rij 3 in kolom 2.

De volgorde waarin de oplossingen gegenereerd worden, maakt niet uit.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> len(list(koninginnen()))
92

>>> sorted(koninginnen(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
```
