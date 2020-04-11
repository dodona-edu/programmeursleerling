Objecten kunnen worden opgenomen in andere objecten. Bijvoorbeeld, een
rechthoek kun je definiëren als een punt dat de linkerbovenhoek
aangeeft, een breedte, en een hoogte. De class `Rechthoek` wordt dan als
volgt gedefinieerd:

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rechthoek:
    def __init__( self, punt, breedte, hoogte ):
        self.punt = punt
        self.breedte = breedte
        self.hoogte = hoogte
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.punt, self.breedte, 
            self.hoogte )

p = Punt( 3.5, 5.0 )
r = Rechthoek( p, 4.0, 2.0 )
print( r )
```

In deze definitie bevat een `Rechthoek` object een `Punt` object.

Creëer een andere versie van de `Rechthoek` class, die vastgelegd is
middels de punten in de linkerbovenhoek en de rechteronderhoek.

### Kopieën en referenties

Hieronder staat een kopie van de code hierboven, met een paar extra
regels die `Punt p` wijzigen.

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rechthoek:
    def __init__( self, punt, breedte, hoogte ):
        self.punt = punt
        self.breedte = breedte
        self.hoogte = hoogte
    def __repr__( self ):
        return "[{},b={},h={}]".format( self.punt, self.breedte, 
            self.hoogte )

p = Punt( 3.5, 5.0 )
r = Rechthoek( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )
```

Je ziet dat doort het wijzigen van `p`, de `Rechthoek r` ook gewijzigd
wordt. Het punt dat in de rechthoek is opgenomen, is feitelijk een
aliasvan het punt dat was meegegeven als argument aan de `__init__()`
methode bij het creëren van de rechthoek. Net als lists, dictionaries,
en sets, worden alle objecten die instanties zijn van een
zelf-gedefinieerde class, doorgegeven als referentie aan functies en
methodes. Dus wordt `Rechthoek r` gecreëerd met een relatie met
`Punt p`. Op deze manier kun je relaties tussen objecten representeren.

Dat is niet altijd iets wat je wilt. Het is onwaarschijnlijk dat je een
`Rechthoek` object een relatie wilt laten hebben met het punt dat
fungeert als de linkerbovenhoek. Hoe kun je dat oplossen? Je kunt het
oplossen door een kopie van het object te creëren. Dat kan middels de
`copy` module. Zoals ik eerder heb aangegeven, produceert de `copy()`
functie van de `copy` module een ondiepe kopie; als je een diepe kopie
wilt maken, moet je de `deepcopy()` functie gebruiken. Voor een `Punt`
is dat niet nodig, omdat er geen verschil is tussen een ondiepe en een
diepe kopie van instanties van deze class.

```python
from copy import copy

class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rechthoek:
    def __init__( self, punt, breedte, hoogte ):
        self.punt = copy( punt )
        self.breedte = breedte
        self.hoogte = hoogte
    def __repr__( self ):
        return "[{},b={},h={}]".format( self.punt, self.breedte, 
            self.hoogte )

p = Punt( 3.5, 5.0 )
r = Rechthoek( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )
```
