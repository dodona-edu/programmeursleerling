De `itertools` module bevat een verzameling functies die geavanceerde
manipulatie van iteratoren mogelijk maken. Als je dit tot het uiterste
doortrekt, voorzien ze je van een soort "iterator algebra" waarmee je
gespecialiseerde hulpmiddelen kunt bouwen in Python. Ik noem hier
slechts een klein aantal van de basisfuncties van `itertools` die
wellicht van nut kunnen zijn.

### `chain()`

`chain()` neemt twee of meer iterabelen as argumenten en functioneert
als een iterabele die de samenstellende iterabelen één voor één afwerkt.

```python
from itertools import chain

seq = chain( [1,2,3], [11,12,13,14], [x*x for x in range(1,6)] )
for item in seq:
    print( item, end=" ")
```

### `zip_longest()`

`zip_longest()` werkt net als `zip()`, maar creëert een iterabele met
een lengte gelijk aan die van de langste van de samenstellende
iterabelen. Je kunt een `fillvalue=` argument opgeven om aan te geven
welke waarde er op de lege plekken moet komen te staan.

```python
from itertools import zip_longest

seq = zip_longest( "appel", "framboos", "banaan", fillvalue=" " )
for item in seq:
    print( item )
```

### `product()`

`product()` creëert een iterabele die alle elementen produceert van het
Cartesisch product van de iterabelen die als argumenten zijn meegegeven.
In iets minder wiskundige termen: als je twee iterabelen hebt, waarvan
de eerste de elementen $x$, $y$, en $z$ heeft, en de tweede de elementen
$a$ en $b$, produceert `product()` een iterabele met de elementen $xa$,
$xb$, $ya$, $yb$, $za$, en $zb$.

```python
from itertools import product

seq = product( [1,2,3], "ABC", ["appel","banaan"] )
for item in seq:
    print( item )
```

### `permutations()`

`permutations()` krijgt een iterabele als argument, en een optioneel
tweede argument dat een lengte aangeeft. Het creëert een iterabele die
alle permutaties produceert die combinaties zijn van elementen van de
meegegeven iterabele, met de gegeven lengte. Als geen lengte wordt
meegegeven, genereert het alle permutaties van alle elementen. Als de
meegegeven iterabele elementen dubbel bevat, zullen er kopieën van
permutaties zijn.

```python
from itertools import permutations

seq = permutations( [1,2,3], 2 )
for item in seq:
    print( item )
```

### `combinations()`

`combinations()` krijgt een iterabele als argument, en een tweede
argument dat een lengte aangeeft. Het creëert een iterabele die
combinaties produceert van elementen van het eerste argument, met de
gegeven lengte. De lengte is *niet* optioneel (wat logisch is, aangezien
bij maximale lengte er maar één combinatie is). De elementen van de
combinaties staan in de volgorde dat ze in de originele iterabele
stonden. Als er elementen meerdere malen voorkomen in de originele
iterabele, zullen er kopieën van combinaties zijn.

```python
from itertools import combinations

seq = combinations( [1,2,3], 2 )
for item in seq:
    print( item )
```

### `combinations_with_replacement()`

`combinations_with_replacement()` werkt net als `combinations()`, maar
ieder element van de iterabele mag meerdere keren gebruikt worden.

```python
from itertools import combinations_with_replacement

seq = combinations_with_replacement( [1,2,3], 2 )
for item in seq:
    print( item )
```
