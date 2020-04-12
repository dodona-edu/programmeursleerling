Om de inhoud van een set te manipuleren, zijn de volgende methodes
beschikbaar. Dit is geen complete lijst van set methodes, maar het zijn
de meest gebruikte.

### `add()` en `update()`

Om een nieuw element aan een set toe te voegen gebruik je de `add()`
methode, met het nieuwe element als argument. Als je meerdere nieuwe
elementen wilt toevoegen, kun je de `update()` methode gebruiken, met
een list die de nieuwe elementen bevat als argument. Je kunt ook een
tuple als argument gebruiken, of zelfs een string. Als je een string
gebruikt, wordt ieder teken van de string gezien als een element.

Omdat een set alleen unieke elementen kan bevatten, worden duplicaten
genegeerd.

```python
fruitset = { "appel", "banaan", "kers", "doerian", "mango" }
print( fruitset )

fruitset.add( "appel" )
fruitset.add( "aalbes" )
print( fruitset )

fruitset.update( ["appel","appel","appel","aardbei",
    "aardbei","appel","mango"] )
print( fruitset )
```

### `remove()`, `discard()`, en `clear()`

Om elementen uit een set te verwijderen, gebruik je de `remove()` of
`discard()` methodes. Beide krijgen het te verwijderen element als
argument. Het verschil is dat `remove()` een runtime error geeft als het
element niet bestaat in de set, terwijl `discard()` niet-bestaande
elementen gewoon negeert.

```python
fruitset = { "appel", "banaan", "kers", "doerian", "mango" }
print( fruitset )

fruitset.remove( "appel" )
print( fruitset )
```

`clear()` verwijdert alle elementen van de set in één keer.

### `pop()`

De `pop()` methode verwijdert een element uit de set en retourneert het.
Je kunt niet zelf aangeven welk element je wilt verwijderen, en je kunt
ook niet voorspellen welk element het is, omdat sets ongeordend zijn.

```python
fruitset = { "appel", "banaan", "kers", "doerian", "mango" }
while len( fruitset ) > 0:
    print( fruitset.pop() )
```

### `copy()`

Net als bij lists en dictionaries geldt voor sets dat als je een
bestaande set toekent aan een andere variabele, je een alias creëert.
Als je een kopie wilt creëren van de set, kun je de `copy()` methode
gebruiken.

### `union()`

De vereniging (Engels: "union") van twee sets is een set die alle
elementen van beide verenigde sets bevat. Je kunt de `union()` methode
voor de ene set, met als argument de andere set, gebruiken om de
vereniging van beide geretourneerd te krijgen. Dit verandert niets aan
de twee gebruikte sets zelf. Je kunt als alternatief de speciale
operator $$|$$ ("pipeline") gebruiken om de vereniging te creëren. Merk
op: je zou misschien denken dat je de $$+$$ operator kunt gebruiken om
twee sets te verenigen, maar $$+$$ is niet voor sets gedefinieerd, en $$*$$
is evenmin gedefinieerd.

```python
fruit1 = { "appel", "banaan", "kers" }
fruit2 = { "banaan", "kers", "doerian" }
fruitunion = fruit1.union( fruit2 )
print( fruitunion )

fruitunion = fruit1 | fruit2
print( fruitunion )
```

### `intersection()`

De doorsnede (Engels: "intersection") van twee sets is een set die
alleen de elementen bevat die beide samenstellende sets gemeen hebben.
Je kunt de `intersection()` methode gebruiken voor de ene set, met als
argument de andere set, om de doorsnede van beide geretourneerd te
krijgen. Dit verandert de samenstellende sets niet. Als alternatief kun
je de speciale operator `&` ("ampersand") gebruiken om de doorsnede te
creëren.

```python
fruit1 = { "appel", "banaan", "kers" }
fruit2 = { "banaan", "kers", "doerian" }
fruitintersection = fruit1.intersection( fruit2 )
print( fruitintersection )

fruitintersection = fruit1 & fruit2
print( fruitintersection )
```

### `difference()`

Het verschil (Engels: "difference") van twee sets is een set die de
elementen van de eerste set bevat, met daaruit verwijderd de elementen
die de eerste set gemeen heeft met de tweede set. Je kunt het verschil
creëren door de `difference()` methode aan te roepen voor de ene set,
met als argument de set waarvan je de elementen uit de eerste set wilt
verwijderen. Dit verandert de samenstellende sets niet. Als alternatief
kun je de speciale operator `-` ("minus") gebruiken om het verschil te
creëren.

```python
fruit1 = { "appel", "banaan", "kers" }
fruit2 = { "banaan", "kers", "doerian" }
fruitdifference = fruit1.difference( fruit2 )
print( fruitdifference )

fruitdifference = fruit1 - fruit2
print( fruitdifference )

fruitdifference = fruit2 - fruit1
print( fruitdifference )
```

### `isdisjoint()`, `issubset()`, en `issuperset()`

The methodes `isdisjoint()`, `issubset()`, en `issuperset()` worden alle
aangeroepen als methodes voor een set, met een tweede set als argument.
Ze retourneren alle `True` of `False`. `isdisjoint()` retourneert `True`
als de twee sets geen elementen gemeen hebben. `issubset()` retourneert
`True` als alle elementen van de eerste set ook voorkomen in de set die
als argument dient. `issuperset()` retourneert `True` als alle elementen
van de set die als argument dient ook voorkomen in de eerste set.

```python
fruit1 = { "appel", "banaan", "kers" }
fruit2 = { "banaan", "kers" }

print( fruit1.isdisjoint( fruit2 ) )
print( fruit1.issubset( fruit2 ) )
print( fruit2.issubset( fruit1 ) )
print( fruit1.issubset( fruit1 ) )
print( fruit1.issuperset( fruit2 ) )
print( fruit2.issuperset( fruit1 ) )
print( fruit1.issuperset( fruit1 ) )
```

Een set is zowel een subset als een superset van zichzelf.

### Oefening

Er is ook een methode `symmetric_difference()` die een set retourneert
die alle elementen bevat van de vereniging van twee sets, behalve de
elementen die zich bevinden in de doorsnede van de twee sets.
Bijvoorbeeld, als set 1 de elementen A, B, en C bevat, en set 2 de
elementen B, C, en D, dan bevat de "symmetric difference" van sets 1 en
2 alleen de elementen A en D. Kun je de `symmetric_difference()`
methode implementeren via de combinatie van een aantal van bovenstaande
methodes?

In hoofdstuk
<a href="#ch:iterations" data-reference-type="ref" data-reference="ch:iterations">8</a>
was een oefening die je vroeg om alle letters te vinden die twee woorden
gemeen hebben, waarbij iedere letter slechts eenmalig gerapporteerd
wordt. Dit kun je zeer efficiënt doen met sets. Schrijf de code
hiervoor.
