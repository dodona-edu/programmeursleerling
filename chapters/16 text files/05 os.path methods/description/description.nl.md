Je weet nu alles wat je moet weten om tekstbestanden in Python te
manipuleren. Er zijn nog een aantal handige functies beschikbaar die het
werken met bestanden vergemakkelijken. Deze vind je in de `os.path`
module. Zoals gewoonlijk geef ik ze hier niet allemaal, maar ik noem wel
de functies die je het meest zult gebruiken.

In deze functies refereert de term "pad" (Engels: "path") aan een
bestandsnaam of directory naam, compleet met het volledige pad vanaf de
"root." Zelfs als het pad niet volledig genoemd is, is het impliciet
opgenomen aangezien ieder bestand op een specifieke plaats in het
bestandssysteem te vinden is.

### `exists()`

De functie `exists()` krijgt een pad als argument, en retourneert `True`
als het pad bestaat, en anders `False`.

```python
from os.path import exists

if exists( "pc_rose.txt" ):
    print( "pc_rose.txt bestaat" )
else:
    print( "pc_rose.txt bestaat niet" )

if exists( "pc_tulip.txt" ):
    print( "pc_tulip.txt bestaat" )
else:
    print( "pc_tulip.txt bestaat niet" )
```

### `isfile()`

`isfile()` test of het pad dat als argument gegeven is een bestand is.
Als het dat is, retourneert de functie `True`. Anders retourneert het
`False`. Als het pad in het geheel niet bestaat, retourneert de functie
ook `False`.

```python
from os.path import isfile

if isfile( "pc_rose.txt" ):
    print( "pc_rose.txt is een bestand" )
else:
    print( "pc_rose.txt is geen bestand" )
```

### `isdir()`

`isfile()` test of het pad dat als argument gegeven is een directory
(folder) is. Als het dat is, retourneert de functie `True`. Anders
retourneert het `False`. Als het pad in het geheel niet bestaat,
retourneert de functie ook `False`.

```python
from os.path import isdir

if isdir( "pc_rose.txt" ):
    print( "pc_rose.txt is een directory" )
else:
    print( "pc_rose.txt is geen directory" )
```

### `join()`

`join()` krijgt één of meerdere delen van een pad mee als argument, en
plakt die op een redelijk slimme manier aan elkaar om een geschikte naam
voor een pad te vormen, die het retourneert. Dit betekent dat het
"slashes" verwijdert of toevoegt waar nodig. `join()` is vooral handig
in combinatie met `listdir()` (uitgelegd in hoofdstuk
16,
en als voorbeeld gebruikt hieronder).

De reden dat `join()` handig is in combinatie met `listdir()`, is dat
`listdir()` een list van bestandsnamen teruggeeft, waarbij de directory
namen niet zijn opgenomen. Als je een list van bestandsnamen vraagt, wil
je ze meestal op een of ander moment openen. Maar als je een bestand
probeert te openen dat niet in de huidige directory staat, dan moet je
het complete pad kennen. Als je `listdir()` uitvoert, geef je de
directory mee als argument, dus je weet waar de bestanden zich bevinden.
Om een compleet pad te bouwen, moet je dus die directory naam aan de
naam van ieder bestand toevoegen. In plaats van zelf te beslissen waar
je "slashes" moet zetten (en wat voor slashes het moeten zijn), kun je
de samenstelling van het pad overlaten aan de `join()` functie.

De code hieronder zoekt alle bestanden in de huidige directory, en toont
ze inclusief het complete pad. De code laat zien hoe je een padnaam
bouwt middels `join()`.

```python
from os import listdir, getcwd
from os.path import join

bestandslist = listdir( "." )
for naam in bestandslist:
    pad = join( getcwd(), naam )
    print( pad )
```

### `basename()`

`basename()` haalt de bestandsnaam uit een pad, en retourneert die.

```python
from os.path import basename

print( basename( "/System/Home/readme.txt" ) )
```

### `dirname()`

`dirname()` haalt de directory naam uit een pad, en retourneert die.

```python
from os.path import dirname

print( dirname( "/System/Home/readme.txt" ) )
```

### `getsize()`

`getsize()` krijgt een pad als argument, en retourneert de grootte van
het betreffende bestand als een integer (die het aantal bytes
weergeeft). Als het pad geen bestand is, krijg je een runtime error.

```python
from os.path import getsize

num = getsize( "pc_rose.txt" )
print( num )
```

Schrijf een programma dat de groottes van alle bestanden in de huidige
directory bij elkaar optelt, en het resultaat toont.
