JavaScript Object Notation (JSON) is een bestandsformaat dat veel
gebruikt wordt in hedendaagse applicaties, vooral applicaties waarin via
web services gecommuniceerd wordt. Het wordt door veel programmeertalen
ondersteund (waaronder natuurlijk Javascript). JSON lijkt op pickling in
de zin dat het objecten die in het geheugen van het computer bestaan
opslaat in bestanden, waarbij de structuur bewaard blijft. Een verschil
tussen pickling en JSON is dat JSON objecten opslaat op een manier die
mensen kunnen lezen.

De `json` module werkt, net als de `pickle` module, met een `dump()`
functie die data structuren naar een bestand schrijft, en een `load()`
functie die data structuren inlaadt uit een bestand. Het bestand moet
een tekstbestand zijn, en geen binair bestand.

```python
from json import dump, load

kaaswinkel = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.json", "w" )
dump( kaaswinkel, fp )
fp.close()

fp = open( "pc_cheese.json", "r" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )
```

Alternatieven voor `dump()` en `load()` zijn de functies `dumps()` en
`loads()`, die geen handle als argument krijgen. In plaats daarvan
krijgt `dumps()` niks in de plaats van het handle argument, maar
retourneert een string die de data structuur in JSON formaat bevat,
terwijl `loads()` een string krijgt als argument in plaats van een
handle, en de data structuur laadt uit die string.

Deze functies kunnen een groot aantal optionele argumenten krijgen die
precies bepalen hoe de data wordt opgeslagen; bijvoorbeeld je kunt een
`indent=` argument aan `dump()` en `dumps()` geven die bepaalt hoe ver
wordt ingesprongen, en je kunt argumenten meegeven die de data in de
dump sorteren. Raadpleeg de Python documentatie als je hier meer van
wilt weten.

Een zwakte van de `json` module is dat alleen standaard Python data
structuren ondersteund worden. Als je eigengemaakte classes wilt
opslaan, moet je ze eerst converteren naar de standaard Python
structuren. De `json` module biedt speciale `JSONencoder` en
`JSONdecoder` classes die daarbij kunnen helpen. Het gaat te ver om die
hier te bediscussiëren.
