Tuples worden niet vaak in Python code gebruikt (behalve als
retourwaardes van functies). Een logische applicatie van tuples zou zijn
de afhandeling van waardes die altijd voorkomen in kleine verzamelingen.
Echter, object oriëntatie (hoofdstuk
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
en verder) biedt veel technieken en hulpmiddelen om met zulke kleine
verzamelingen om te gaan, wat betekent dat programmeurs meestal voor
object oriëntatie kiezen als ze dat soort zaken onder handen hebben.

Hier volgt toch een voorbeeld van het gebruik van tuples in een
applicatie. Stel je voor dat je een applicatie moet schrijven die
geometrische figuren in een 2-dimensionale ruimte bewerkt. Een concept
dat je daarbij nodig hebt is een punt: een locatie in de 2D ruimte die
geïdentificeerd wordt via twee coördinaten. In plaats van functies te
schrijven die steeds een aparte X en een aparte Y coördinaat meekrijgen,
kun je specificeren dat coördinaten worden meegegeven als tuples.

```python
from math import sqrt

# Retourneert de afstand tussen twee punten in 2-dimensionale
# ruimte. The punten zijn de parameters van de functie.
# Ieder punt is een tuple met twee numerieke waardes.
def afstand( p1, p2 ):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

punt1 = (1,2)
punt2 = (5,5)
print( "Afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )
```

Een voordeel van het gebruik van tuples op deze manier is dat het
relatief eenvoudig is om een functie te schrijven die kan omgaan met
coördinaten in willekeurige ruimtes.

```python
from math import sqrt

# afstand tussen twee punten in N-dimensionale ruimte.
# De punten hebben dezelfde dimensie, ze zijn allebei tuples
# met numerieke waardes, met dezelfde lengte.
def afstand( p1, p2 ):
    totaal = 0
    for i in range( len( p1 ) ):
        totaal += (p1[i] - p2[i])**2
    return sqrt( totaal )

# 1-dimensionale ruimte
punt1 = (1,)
punt2 = (5,)
print( "1D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )

# 2-dimensionale ruimte
punt1 = (1,2)
punt2 = (5,5)
print( "2D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )

# 3-dimensionale ruimte
punt1 = (1,2,4)
punt2 = (5,5,8)
print( "3D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )
```
