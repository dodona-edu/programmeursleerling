De `datetime` module bevat functies die je berekeningen laten uitvoeren
met datum en tijd. De module bevat een aantal classes die daarbij
helpen, waarvan de meest belangrijke zijn: `datetime`, `timedelta`,
`date`, en `time`. `datetime` bevat attributen `year` (jaar), `month`
(maand), `day` (dag), `hour` (uur), `minute` (minuut), `second`
(seconde), `microsecond` (duizendste seconde), en `tzinfo` (tijdzone).
`date` en `time` bevatten een deelverzameling van deze attributen.
Objecten die instanties zijn van deze classes zijn onveranderbaar.

Ik beperk mij hier tot het bespreken van `datetime` en `timedelta`, maar
er bestaan equivalente functies en methodes voor de andere classes.

`datetime` objecten bevatten een datum en een tijd. Sommige van de
methodes in `datetime` objecten zijn:

-   `now()` creëert een `datetime` object dat de huidige datum en tijd
    bevat. Je roept deze methode typisch aan met een class call om een
    waarde voor `now()` te krijgen.

-   `datetime()` creëert een `datetime` object met de opgegeven
    argumenten. De eerste drie argumenten zijn niet optioneel, en
    bevatten in volgorde numerieke waardes voor jaar, maand, en dag. De
    andere attributen (uur, minuut, seconde, duizendste seconde, en
    tijdzone) zijn optioneel. Argumenten kun je ofwel in de voorgenoemde
    volgorde geven, of via de syntax `<argument>=<waarde>`, waarbij
    `<argument>` de naam van een attribuut is zoals hierboven
    beschreven.

```python
from datetime import datetime

print( datetime.now() )
```

Als je `datetime` objecten afdrukt krijg je een specifiek formaat als
uitvoer. Als je dit formaat wilt wijzigen (inclusief het afdrukken van
de naam van de dag in de week) dan kun je in de `datetime` module
functies vinden die dat mogelijk maken. Zie de Python handleiding voor
meer informatie.

Om met `datetime` objecten te rekenen, heb je `timedelta` nodig. Een
`timedelta` object specificeert het verschil tussen twee `datetime`
objecten. Een `timedelta` object bevat `days` (dagen), `seconds`
(seconden), en `microseconds` (duizendste seconden). Je kunt ook andere
attributen in een `timedelta` object vinden, die tijdverschil op andere
manieren uitdrukken, maar de enige drie die het opslaat zijn de drie die
ik hier noem; andere attributen worden uit deze drie berekend.

Je kunt allerlei berekeningen uitvoeren met `timedelta` objecten, maar
de meest nuttige behandelen het verschil tussen twee `datetime`
objecten. Je kunt dus een `timedelta` object optellen bij een `datetime`
object om een nieuw `datetime` object als uitkomst te krijgen, of je
kunt twee `datetime` objecten van elkaar aftrekken om het verschil te
krijgen als een `timedelta` object.

```python
from datetime import datetime, timedelta

ditjaar = datetime.now().year
xmasditjaar = datetime( ditjaar, 12, 25, 23, 59, 59 )
dezedag = datetime.now()
dagen = xmasditjaar - dezedag

if dagen.days < 0:
    print( "Kerst komt volgend jaar weer." )
elif dagen.days == 0:
    print( "Het is Kerst!" )
else:
    print( "Slechts", dagen.days, "dagen tot Kerst!" )
```
