Stel dat je een bepaalde data structuur in een bestand wilt opslaan,
bijvoorbeeld een list van tuples. Je kunt dat doen door de tuples naar
strings te converteren en die op te slaan in een bestand, met iedere
tuple op een eigen regel. Als je dan later de data structuur weer wilt
opbouwen, moet je het bestand inlezen, de regels uiteen rafelen, en de
list van tuples weer opbouwen. Je kunt je voorstellen dat dit een
behoorlijk bewerkelijke aanpak is die een lastig stuk code vereist.

Gelukkig hoef je deze code niet te schrijven. Python biedt een oplossing
voor het opslaan van data structuren in bestanden, waarbij zowel de
structuur als de inhoud wordt opgeslagen. Dit wordt "pickling"
genoemd.[^25] Je kunt de hele data structuur in één keer in een bestand
wegschrijven door het bestand voor schrijven te openen in binaire modus,
en dan de functie `dump()` van de module `pickle` aan te roepen met de
data structuur als eerste argument, en de handle als tweede argument.

```python
from pickle import dump

kaaswinkel = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.pck", "wb" )
dump( kaaswinkel, fp )
fp.close()

print( "uitvoer gereed" )
```

Om de inhoud van een "pickle" bestand te lezen, gebruik je de functie
`load()` van de `pickle` module. `load()` krijgt de handle van het
bestand, geopend in binaire lees-modus, als argument.

```python
from pickle import load

fp = open( "pc_cheese.pck", "rb" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )
```

Je kunt zien dat `load()` de data structuur netjes opnieuw opbouwt.

Het werkt zelfs voor classes die je zelf definieert:

```python
from pickle import dump, load

class Punt:
    def __init__( self, x, y ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({},{})".format( self.x, self.y )

p = Punt( 2, 5 )
fp = open( "pc_point.pck", "wb" )
dump( p, fp )
fp.close()

fp = open( "pc_point.pck", "rb" )
q = load( fp )
fp.close()

print( type( q ) )
print( q )
```

[^25]: In het Nederlands betekent dit "conservering," maar ik denk dat
    niemand begrijpt waar je het over hebt als je voor Python deze
    techniek zo noemt. Een leukere vertaling zou "pekelen" zijn, maar
    aangezien pekelen met zout gebeurt terwijl "pickling" met zuur
    gebeurt (augurken heten bijvoorbeeld "pickles" in het Engels), is
    ook die vertaling te verwarrend. Net als "inmaken."
