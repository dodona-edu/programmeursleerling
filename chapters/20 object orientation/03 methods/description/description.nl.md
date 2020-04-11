Ik heb al drie methodes geïntroduceerd, namelijk `__init__()`,
`__repr__()`, en `__str__()`. Dit zijn voorgedefinieerde methodes die
iedere class heeft. Omdat ze door de ontwikkelaars van Python
gedefinieerd zijn, hebben ze excentrieke namen die beginnen en eindigen
met een dubbele underscore. Er zijn nog meer van zulke methodes, die ik
in latere hoofdstukken aan de orde laat komen.

Je kunt ook je eigen methodes definiëren voor een class. Zulke methodes
krijgen namen die lijken op de namen van functies, en die dezelfde
conventies volgen: ze beginnen met een kleine letter, en als er meerdere
woorden zijn, hebben ze underscores tussen of hoofdletters voor de
eerste letter van ieder tweede en volgende woord. De prefix `is` wordt
gebruikt voor methodes die een `True`/`False` statement maken over een
object, de prefix `get` wordt gebruikt om een waarde uit een object te
krijgen, en de prefix `set` wordt gebruikt om een waarde in een object
te zetten.

Bijvoorbeeld, voor een punt kan ik de methode `afstand_tot_oorsprong()`
creëren, die berekent hoe ver het punt afligt van het punt (0,0).

```python
from math import sqrt

class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def afstand_tot_oorsprong( self ):
        return sqrt( self.x*self.x + self.y*self.y )

p = Punt( 3.5, 5.0 )
print( p.afstand_tot_oorsprong() )
```

Je kunt ook methodes maken die een object wijzigen. Bijvoorbeeld, een
"translatie" van een punt is een verschuiving van een punt langs een
vector, dat wil zeggen, over een bepaalde afstand in horizontale en een
bepaalde afstand in verticale richting. De methode `translatie()` krijgt
twee argumenten (naast `self`, uiteraard), die de horizontale en
verticale verschuivingen vastleggen.

```python
from math import sqrt

class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def translatie( self, shift_x, shift_y ):
        self.x += shift_x
        self.y += shift_y

p = Punt( 3.5, 5.0 )
p.translatie( -3, 7 )
print( p )
```

Zoals je ziet heb ik geen retourwaarde voor `translatie()` gedefinieerd
(die had ik niet nodig), maar de `translatie()` methode wijzigt de
coördinaten van het punt, en effectueert daarbij de translatie actie.

Breid de class `Punt` uit met een methode die een punt wijzigt in het
spiegelpunt ten opzichte van de oorsprong, dat wil zeggen, inverteer de
tekens van de coördinaten, bijvoorbeeld: (3,4) wordt (-3,-4) en (-1,2)
wordt (1,-2).
