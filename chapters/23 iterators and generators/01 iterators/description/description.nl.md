Je hebt het `for ... in ...` commando regelmatig gebruikt. Het is je
wellicht opgevallen dat het op allerlei verschillende manieren gebruikt
wordt.

```python
for i in [1,2,3,4]:
    print( i, end=" " )
print()
for i in ( "pi", 3.14, 22/7 ):
    print( i, end=" ")
print()
for i in range( 3, 11, 2 ):
    print( i, end=" ")
print()
for c in "Hallo":
    print( c, end=" " )
print()
for key in { "appel":1, "banaan":3 }:
    print( key, end=" " )
```

Lists, strings, en dictionaries zijn alle "iterabelen" (een
vernederlandsing van het Engelse woord "iterable"), wat betekent dat ze
gebruikt mogen worden in `for ... in ...` statements. Vele andere
objecten kunnen ook als iterabelen gebruikt worden. Je kunt ervoor
zorgen dat dat ook geldt voor instanties van je eigen classes.

Een "iterator" is een object dat een nieuwe element retourneert iedere
keer dat je de standaardfunctie `next()` aanroept met het object als
argument. Als het object niks meer heeft dat geretourneerd kan worden,
genereert het een `StopIteration` exception. Als je deze exception wilt
vermijden, kun je een optioneel tweede argument aan `next()` meegeven,
dat geretourneerd wordt als de iterator niks meer heeft. Je kunt van
iedere iterabele een iterator object maken middels de standaardfunctie
`iter()`.

```python
iterator = iter( ["appel", "banaan", "kers"] )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
```

Je kunt iteratoren gebruiken in `for ... in ...` statements.

```python
iterator = iter( ["appel", "banaan", "kers"] )
for fruit in iterator:
    print( fruit )
```

### Iterabele objecten

Een object dat dient te functioneren als iterabele moet de volgende twee
methodes bevatten:

-   een methode `__iter__()` die de iterabele (meestal het object zelf)
    retourneert

-   een methode `__next__()` die toegang geeft tot alle elementen die
    het object bevat, één voor één, en die als er geen elementen meer
    zijn de `StopIteration` exception genereert (in een `for ... in ...`
    loop, betekent dit dat de loop eindigt)

Je kunt alle elementen van een iterabele doorlopen met `for ... in ...`.
Er zijn drie manieren om zulke iterabele objecten te maken. De eerste
twee beginnen met de iterabele als een container die een sequentie van
elementen bevat.

De eerste manier verwijdert, iedere keer als `__next__()` wordt
aangeroepen, één van de elementen en retourneert het, waarna de
iterabele dus één element minder bevat. Wanneer alle elementen behandeld
zijn, zal het bij iedere volgende aanroep `StopIteration` genereren.
Hier is een voorbeeld van zo'n iterator die de eerste tien getallen van
de Fibonacci reeks retourneert.

```python
class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
```

De tweede manier houdt een index bij in de sequentie van elementen, en
verhoogt die index bij iedere aanroep van `__next__()`, waarna het
corresponderende element geretourneerd wordt. Wanneer de index buiten de
grenzen van de sequentie komt, wordt `StopIteration` gegenereerd. Je
kunt op deze manier een herbruikbare iterabele maken, als je een methode
toevoegt die de index weer op nul zet.

```python
class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
        self.index = -1
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.index < len( self.seq )-1:
            self.index += 1
            return self.seq[self.index]
        raise StopIteration()
    def reset( self ):
        self.index = -1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
```

De derde manier maakt van de iterabele niet een container met elementen,
maar een object dat het volgende element berekent wanneer `__next__()`
wordt aangeroepen. Een dergelijke iterabele kan eindig zijn, maar kan in
principe ook een oneindige aantal elementen retourneren. Je kunt de
iterabele ook opnieuw laten beginnen als je een methode toevoegt om de
berekening opnieuw te initialiseren.

```python
class Fibo:
    def reset( self ):
        self.nr1 = 0
        self.nr2 = 1
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
        self.reset()
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.nr2 > self.maxnum:
            raise StopIteration()
        nr3 = self.nr1 + self.nr2
        self.nr1 = self.nr2
        self.nr2 = nr3
        return self.nr1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
```

{:class="callout callout-warning"}
> #### Waarschuwing
> Wees erg voorzichtig met het bouwen van een iterabele
> die een oneindig aantal elementen kan retourneren. Programmeurs gaan
> ervan uit dat `for ... in ...` geen eindeloze loop kan veroorzaken, maar
> in het voorbeeld hierboven kan een eindeloze loop ontstaan als ik geen
> limiet aan het aantal elementen stel. Bij een dergelijke iterabele kun
> je het beste een verplicht maximum stellen aan het aantal elementen, wat
> ik in dit voorbeeld doe door de parameter `maxnum` op te nemen.

Creëer een iterator die alle kwadraten van integers tussen 1 en 10
genereert. Je mag zelf kiezen welke aanpak je volgt.

### Gedelegeerde iteratie

In de voorbeelden hierboven werd een iterabele gecreëerd door het
aanroepen van de `__iter__()` methode voor een object, dat zichzelf
retourneert. Dat hoeft niet op die manier. Een iterabele mag de iteratie
delegeren[^24] aan een ander object, dat wordt aangemaakt door de
iterabele en geretourneerd wordt als de `__iter__()` methode wordt
aangeroepen.

```python
class FiboIterable:
    def __init__( self, seq ):
        self.seq = seq
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()

class Fibo:
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
    def __iter__( self ):
        nr1 = 0
        nr2 = 1
        seq = []
        while nr2 <= self.maxnum:
            nr3 = nr1 + nr2
            nr1 = nr2
            nr2 = nr3
            seq.append( nr1 )
        return FiboIterable( seq )

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
for n in fseq:
    print( n, end=" " )
```

Deze aanpak heeft een aantal voordelen:

-   Je kunt meerdere instanties van de iterabele parallel aan elkaar
    uitvoeren zonder er expliciet meer dan één te creëren (omdat ze
    automatisch worden gecreëerd wanneer dat nodig is, dus als
    `for ... in ...` gebruikt wordt)

-   Je hoeft geen methode `reset()` aan te roepen om weer van voor af
    aan te beginnen; iedere nieuwe aanroep van de iterabele begint weer
    van voor af aan

-   De gedelegeerde iterabele wordt automatisch uit het geheugen
    verwijderd wanneer er geen elementen meer in zitten (Python geeft
    namelijk automatisch geheugen vrij als het gebruikt wordt door een
    object waaraan het programma niet langer kan refereren)

### `zip()`

Je kunt tuples creëren die de elementen bevatten van meerdere iterabelen
middels de standaardfunctie `zip()`. Om een eenvoudig voorbeeld te
geven:

```python
z = zip( [1,2,3], [4,5,6], [7,8,9] )
for x in z:
    print( x )
```

Een zip-object is een iterator, dat wil zeggen, je kunt het zip-object
zelf niet printen, maar je kunt de elementen van het object doorlopen
via een `for ... in ...` constructie. Het $i$de element van het
zip-object bestaat uit de $i$de elementen van ieder van de iterabelen
die als argumenten gebruikt worden. Als deze iterabelen van ongelijke
lengte zijn, dan is de lengte van het zip-object gelijk aan de kortste
lengte van de argumenten.

In het voorbeeld hierboven heb ik lists gebruikt als argumenten, maar je
kunt iedere iterabele als argument gebruiken. Bijvoorbeeld, in de code
hieronder zip ik een range, een iterator, en een list comprehension.

```python
class Dubbel:
    def __init__( self ):
        self.seq = [2*x for x in range( 1, 11 )]
    def __iter__( self ):
        return self
    def __next__( self ):
        return self.seq.pop(0)

seq = zip( range( 1, 11 ), Dubbel(), [3*x for x in range(1,11)] )
for x in seq:
    print( x )
```

Creëer een zip-object dat tuples met twee elementen produceert: het
eerste element is een integer, lopend van 1 tot 10. Het tweede element
is het kwadraat van het eerste element.

### `reversed()`

De ingebouwde functie `reversed()` creëert vanuit een iterabele een
iterator die de elementen van de iterator in omgekeerde volgorde
verwerkt. De iterabele wordt als argument meegegeven. Niet alle
iterabelen kunnen omgekeerd worden, maar de iterabelen die onderdeel
zijn van standaard Python (zoals lists) kunnen het in ieder geval. Als
je ervoor wilt zorgen dat een iterabele die je zelf creëert middels
`reversed()` omgekeerd kan worden, moet je de Python documentatie
bestuderen.

```python
fruitlist = ["appel", "peer", "kers", "banaan"]
for fruit in reversed( fruitlist ):
    print( fruit )
```

### `sorted()`

De ingebouwde functie `sorted()` creëert vanuit een iterabele een
iterator die de elementen van de iterator gesorteerd verwerkt. De
iterabele wordt als argument meegegeven. Er zijn daarnaast twee
optionele argumenten. De eerste is `key=<key>`, waarbij `<key>` de naam
is van een functie die gebruikt wordt om de key van het sorteerproces te
definiëren. Dit werkt gelijk aan de `key=<key>` parameter voor de list
`sort()` methode – zie hoofdstuk
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>
voor meer informatie. Als geen key wordt meegegeven is de
sorteervolgorde voor strings alfabetisch, en voor getallen numeriek.
Voor andere data types, of gemixte data types, hangt het van de
specificatie van het key argument af. Het tweede optionele argument is
`reverse=<boolean>`, dat via `True` of `False` aangeeft of de sortering
een omgekeerd resultaat moet geven.

```python
fruitlist = ["appel", "peer", "kers", "banaan"]
for fruit in sorted( fruitlist ):
    print( fruit )
```

[^24]: De naam "gedelegeerde iteratie" heb ik zelf bedacht. Als er een
    "officiële" naam voor deze werkwijze bestaat, hoor ik dat graag.
