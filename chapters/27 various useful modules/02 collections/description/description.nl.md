De `collections` module bevat handige classes die je helpen om
iterabelen te manipuleren, zoals strings, tuples, lists, dictionaries,
en sets. `collections` biedt interessante functionaliteiten, waarvan de
meeste enigszins excentriek zijn, wat het onwaarschijnlijk maakt dat je
ze snel nodig hebt. Ik noem de twee die ik het meest gebruikt zie
worden, namelijk de `Counter` class en de `deque` class.

Een `Counter` object lijkt op een dictionary, die elementen bevat in de
vorm van keys, en voor ieder van de elementen een "telling" als waarde.
Je creëert een `Counter` object door bij creatie het als argument een
sequentie te geven waarvan je de elementen wilt tellen. Wanneer het
gecreëerd hebt, kun je nuttige methodes gebruiken, zoals:

-   `most_common()` krijgt als argument een integer, en retourneert een
    list met die elementen die de hoogste "telling" hebben, zoveel als
    het integer argument aangeeft. De elementen van de list zijn
    2-tuples, waarbij het eerste element van iedere tuple een van de
    getelde elementen is, en het tweede element de corresponderende
    telling. Ze zijn geordend van hoogste naar laagste telling. Als geen
    integer argument is meegegeven, bevat de list alle elementen.

-   `update()` krijgt een iterabele als argument en telt de elementen
    van die nieuwe iterabele op bij de tellingen die al in het object
    staan.

```python
from collections import Counter

data = [ "appel", "banaan", "appel", "banaan", "appel", "kers" ]
c = Counter( data )
print( c )
print( c.most_common( 1 ) )

data2 = [ "mango", "kers", "kers", "kers", "kers" ]
c.update( data2 )
print( c )
print( c.most_common() )
```

Een `deque` object is een list die je moet gebruiken als een "queue,"
dat wil zeggen, een list waarbij elementen toegevoegd en verwijderd
worden aan alleen de uiteinden van de list. Een `deque` object
ondersteunt methodes die gelijk zijn aan de gebruikelijke list-methodes,
zoals `append()`, `extend()`, en `pop()`, maar die bij een `deque`
object alleen werken aan het "rechter-uiteinde" van de list (bij de
hoogste index). Daarnaast bevat hij ook gelijksoortige methodes die
werken aan het "linker-uiteinde" van de list (bij index 0), namelijk
`appendleft()`, `extendleft()`, en `popleft()`. Voor de rest zijn de
methodes zoals je zou verwachten. Je creëert een `deque` object met de
iterabele die je in een `deque` wilt veranderen als argument.

```python
from collections import deque

dq = deque( [ 1, 2, 3 ] )
dq.appendleft( 4 )
dq.extendleft( [ 5, 6 ] )
print( dq )
```
