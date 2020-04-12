Lists en dictionaries zijn de twee meest-gebruikte data structuren in
Python. Het is vaak duidelijk welk van de twee je moet gebruiken bij een
probleem, maar het kan nuttig zijn om iets te weten over hoe Python deze
data structuren verwerkt voor het geval je een keus hebt.

Stel je voor dat je een groot aantal getallen uit een bestand moet
lezen. De getallen zijn allemaal verschillend en kunnen willekeurig
groot zijn. Je moet later getallen van een andere lijst vergelijken met
de getallen die je uit het bestand hebt gelezen.

Moet je een list of een dictionary gebruiken om de getallen die je
inleest op te slaan? Omdat het alleen maar getallen zijn en geen extra
data, lijkt een list de beste optie. Er is echter een probleem dat
optreedt als je hier een list gebruikt. Bekijk de volgende code, die een
list creëert met 10000 getallen, en daarna bekijkt of 10000 andere
getallen in de list voorkomen (wat geldt voor geen van de getallen).

```python
from datetime import datetime

numlist = []
for i in range( 10000 ):
    numlist.append( i )

start = datetime.now()
teller = 0
for i in range( 10000, 20000 ):
    if i in numlist:
        teller += 1
eind = datetime.now()

print( "{}.{} seconden om {} nummers te vinden".format( 
    (eind-start).seconds, (eind-start).microseconds, teller ) )
```

Hier is code die hetzelfde doet, maar de getallen inleest in een
dictionary, waarbij simpelweg voor ieder ingelezen getal een waarde van
1 in de dictionary wordt opslagen.

```python
from datetime import datetime

numdict = {}
for i in range( 10000 ):
    numdict[i] = 1

start = datetime.now()
teller = 0
for i in range( 10000, 20000 ):
    if i in numdict:
        teller += 1
eind = datetime.now()

print( "{}.{} seconden om {} nummers te vinden".format( 
    (eind-start).seconds, (eind-start).microseconds, teller ) )
```

Als je deze code uitvoert, zul je zien dat voor de dictionary het
antwoord vrijwel onmiddellijk volgt, maar dat het voor een list wat
langer duurt. De reden is dat ik met behulp van de `in` operator
controleer of een getal voorkomt in de list of de dictionary. Voor een
list betekent dat dat Python de hele list sequentieel doorzoekt, totdat
het het getal vindt of het einde van de list bereikt wordt. Dit houdt in
dat Python 10000 keer 10000 getallen controleert (omdat het geen enkel
getal kan vinden), ofwel 100 miljoen getallen.

Voor een dictionary is het zoeken van een key veel sneller. Python kan
erg snel vaststellen of een key wel of niet in een dictionary zit.[^18]
Meestal is het controleren van een handjevol getallen genoeg. Daarom is
de dictionary code veel, veel sneller.

Je denkt misschien dat een paar seconden zoektijd voor de list nog
steeds erg weinig is, maar de zoektijd neemt kwadratisch toe met de
hoeveelheid data. Afhankelijk van het soort en de omvang van het
probleem, kan een dictionary zeer te prefereren zijn boven een list.

Lists nemen wel minder geheugen in beslag dan dictionaries, en als je
een list direct kunt benaderen via een index, kunnen lists zeker sneller
zijn dan dictionaries. Bijvoorbeeld, in bovenstaande probleem, als ik
zou weten dat de list gesorteerd is dan kan ik getallen op een veel
slimmere manier vinden dan via de `in` operator (ongeveer 14 getallen
controleren volstaat) – in dat geval is het gebruik van een list
misschien sneller dan het gebruik van een dictionary.

Onthoud hiervan dat een list snel is als je de elementen via hun index
kunt benaderen, terwijl een dictionary een betere keuze is als de enige
manier om iets te zoeken is de elementen te scannen. De `in` operator
lijkt gemakkelijk en is leesbaar, maar als je hem gebruikt om iets te
zoeken in een lange list, dan ben je verkeerd bezig.

[^18]: Python slaat de keys voor een dictionary op in een zogeheten
    "hash tabel." Ik leg de details daarvan niet uit, maar weet dat dit
    het mogelijk maakt om keys heel snel op te zoeken, ten koste van wat
    geheugengebruik.
