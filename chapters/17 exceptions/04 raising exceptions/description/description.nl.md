Je mag zelf in je code ook exceptions genereren. Daarvoor is het
gereserveerde woord `raise` bestemd. Je laat het volgen door één van de
bekende exceptions (je mag eventueel ook je eigen exceptions definiëren,
maar daarvoor moet je de hoofdstukken
21
tot en met
23
bestuderen). Je mag een exception die je genereert willekeurige
argumenten meegeven, en die zijn dan weer via het `args` attribuut te
benaderen.

Je vraagt je misschien af waarom je exceptions zou willen genereren. Het
antwoord is dat als je een module programmeert, en er een fout kan
optreden in een van de functies in de module (bijvoorbeeld omdat het
hoofdprogramma de verkeerde parameters meegeeft), het eigenlijk niet de
bedoeling is dat je foutmeldingen print. Het is veel netter om een
exception te genereren, en het hoofdprogramma deze exception af te laten
handelen. Hier is een voorbeeld:

```python
def getStringLenMax10( prompt ):
    s = input( prompt )
    if len( s ) > 10:
        raise ValueError( "Lengte groter dan 10", len( s ) )
    return s

print( getStringLenMax10( "Gebruik 10 tekens of minder: " ) )
```

Als je deze code uitvoert, zie je dat als je een string invoert die meer
dan 10 tekens bevat, een `ValueError` exception wordt gegenereerd. De
exception krijgt twee argumenten, die je als een tuple getoond ziet
worden als Python de exception op het scherm gooit. Je kunt deze
exception in de code afhandelen op dezelfde manier als je exceptions
afhandelt die door Python worden geproduceerd.

Het gereserveerde woord `raise` heeft een tweede functie: als je in de
afhandeling van een `except` zit, dan kun je, in plaats van de exception
meteen af te handelen, de exception doorgeven naar het "hoger gelegen
niveau" van het programma. Je doet dat door het command `raise` te
geven, zonder parameters, en de exception wordt dan als "nog niet
afgehandeld" beschouwd. Dit kan nuttig zijn als je een beetje extra
afhandeling wilt doen voordat het programma "crasht" op grond van de
exception, of de exception elders wordt opgevangen. Bijvoorbeeld:

```python
fp = open( "pc_rose.txt ")
try:
    buf = fp.read()
    print( buf )
except IOError:
    fp.close()
    raise
fp.close()
```

Deze code loopt waarschijnlijk goed, maar als er een `IOError` optreedt
tijdens het lezen van het bestand, dan wordt het bestand netjes gesloten
alvorens de exception wordt doorgegeven.
