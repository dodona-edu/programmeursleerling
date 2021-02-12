Scope (dat vertaald kan worden als "bereik," maar dat een zo'n
verwarrende vertaling dat hij niet gebruikt wordt) refereert aan
"zichtbaarheid." Specifiek, waar het variabelen betreft, refereert het
aan in welke delen van een programma een variabele zichtbaar is en
gewijzigd kan worden. Levensduur refereert aan hoe lang een variabele in
het geheugen van de computer blijft. Levensduur is gerelateerd aan
scope.

### Scope van variabelen

De scope van een variabele is het blok code waarin de variabele is
gecreëerd, en alle blokken code die genest zijn binnen dat blok code op
een dieper niveau van inspringing. Bijvoorbeeld:

```python
hallo = "Hallo!"
totziens = "Tot ziens!"

for i in range( 3 ):
    for j in range( 2 ):
        middag = "Goedemiddag"
        print( totziens )
    print( j )
    print( hallo )
    print( middag )

print( i )
print( j )
print( middag )
```

De variabelen `hallo` en `totziens` zijn gedefinieerd op het hoogste
niveau van inspringing van het programma, wat betekent dat hun scope het
hele programma is. De variabelen `i`, `j`, en `middag` zijn gedefinieerd
in blokken code op een dieper niveau van inspringing. In de meeste
programmeertalen zou dit betekenen dat hun scope beperkt is tot die
diepere niveaus, maar Python is vriendelijk op dit gebied en laat hun
scope verder reiken dan het blok code waarin de variabelen gecreëerd
zijn. Daarom zijn in dit programma de variabelen zichtbaar in het hele
programma, na hun creatie.

Hoe werkt dit met functies?

```python
dubbeltje = "dubbeltje"

def geboren():
    print( "Als je voor een", dubbeltje, "geboren wordt,",
        "dan word je nooit een", kwartje )

kwartje = "kwartje"
geboren()
print( "dubbeltje =", dubbeltje, "en kwartje =", kwartje )
```

Zowel `dubbeltje` als `kwartje` zijn zichtbaar in de functie
`geboren()`, omdat ze gedefinieerd zijn voordat de functie is
aangeroepen, en omdat het blok code van de functie op een dieper niveau
van inspringing zit. Maar kijk nu naar het volgende programma, dat een
kleine wijziging bevat ten opzichte van het vorige:

```python
dubbeltje = "dubbeltje"

def geboren():
    kwartje = "stuiver"
    print( "Als je voor een", dubbeltje, "geboren wordt,",
        "dan word je nooit een", kwartje )

kwartje = "kwartje"
geboren()
print( "dubbeltje =", dubbeltje, "en kwartje =", kwartje )
```

Voer dit programma uit, bestudeer de code en output, en vergelijk ze met
de code en output van het voorgaande programma. De variabele `kwartje`
lijkt een nieuwe waarde te krijgen in de functie `geboren()`, wat ertoe
leidt dat de functie nu claimt dat je na je geboorte niet minder waard
kunt worden. Maar als daarna in het hoofdprogramma de waarde van
`kwartje` wordt afgedrukt, zie je dat deze variabele nog steeds het
woord `"kwartje"` bevat.

De reden voor het verschil is dat de variabele `kwartje` in de functie
een andere is dan de variabele `kwartje` in het hoofdprogramma. Door in
een functie een waarde toe te kennen aan een variabele, wordt een
nieuwe, "lokale" variabele gecreëerd. En deze variabele wordt dan
gebruikt voor de rest van de functie. De originele variabele `kwartje`
bestaat nog steeds, maar is onzichtbaar geworden voor de functie omdat
de functie een eigen variabele `kwartje` heeft gemaakt.

De levensduur van de variabele `kwartje` in de functie is de periode
waarvoor het blok code van de functie wordt uitgevoerd. Zodra de functie
eindigt (bijvoorbeeld omdat er een `return` in de functie staat of omdat
de laatste regel van de functie is uitgevoerd), worden de lokale
variabelen van de functie vernietigd. Ze staan niet langer in het
geheugen van de computer, en kunnen niet meer benaderd worden.

```python
appel = "appel"
banaan = "banaan"
kers = "kers"
doerian = "doerian"

def printfruit_1():
    print( appel, banaan )

def printfruit_2( appel ):
    banaan = kers
    print( appel, banaan )

def printfruit_3( appel, banaan ):
    kers = "mango"
    banaan = kers
    print( appel, banaan )

printfruit_1()
printfruit_2( kers )
printfruit_3( kers, doerian )

print( "appel =", appel )
print( "banaan =", banaan )
print( "kers =", kers )
print( "doerian =", doerian )
```

Voer deze code uit en bestudeer hem nauwlettend.

De drie functies `printfruit_1()`, `printfruit_2()`, en
`printfruit_3()` printen de waardes van de variabelen `appel` en
`banaan`.

In `printfruit_1()` worden de variabelen `appel` en `banaan` geprint
die gedefinieerd zijn buiten de functie, aangezien de functie zelf geen
variabelen met deze namen definieert.

In `printfruit_2()`, is `appel` een parameter van de functie, wat
betekent dat de variabele lokaal is voor de functie en, omdat het een
parameter is, zijn waarde krijgt van buiten de functie. De waarde de de
parameter krijgt is de waarde van `kers`. `banaan` is een variabele die
zijn waarde krijgt in de functie. Dit is daarom een nieuwe, lokale
variabele `banaan`, die niks te maken heeft met de variabele `banaan` in
het hoofdprogramma. Deze variabele krijgt de waarde van de variabele
`kers`, die niet lokaal bekend is in de functie, dus wordt de variabele
`kers` van het hoofdprogramma gebruikt. Dus krijgt de lokale variabele
`banaan` de waarde "kers," en dat is dus de waarde die geprint wordt.

In `printfruit_3()` zijn `appel` en `banaan` beide parameters, dus
beide zijn lokaal voor de functie en krijgen hun initiële waarde bij de
aanroep van de functie. De functie creëert een lokale variabele `kers`,
die onafhankelijk is van de variabele `kers` uit het hoofdprogramma, en
geeft deze variabele de waarde `"mango"`. De variabele `banaan` krijgt
vervolgens de waarde van `kers`. Omdat al deze wijzigingen gemaakt
worden met lokale variabelen, hebben ze geen invloed op de waardes van
de variabelen in het hoofdprogramma.

Waar het hier vooral om gaat is het feit dat, na de aanroep van functies
die op allerlei manieren met de parameters spelen en die lokale
variabelen aanmaken met dezelfde namen als variabelen in het
hoofdprogramma, uit het afdrukken van de variabelen in het
hoofdprogramma blijkt dat die allemaal nog steeds dezelfde waarde hebben
als ze hadden voordat de functies werden aangeroepen. Zodra je probeert
in een functie een variabele die bestaat in het hoofdprogramma een
andere waarde te geven middels een assignment, wordt in plaats daarvan
een nieuwe, lokale variabele gecreëerd. Een dergelijke lokale variabele
is compleet onafhankelijk van het hoofdprogramma. De levensduur van zo'n
lokale variabele is de periode dat de functie wordt uitgevoerd.
Parameters kun je ook beschouwen als lokale variabelen.

Dit is een enorm krachtige eigenschap van functies: ze hoeven geen
rekening te houden met variabelen die bestaan buiten de functie,
aangezien iedere variabele die ze creëren lokaal is voor de functie.

### Globale variabelen

Ik liet hierboven zien dat variabelen die buiten een functie zijn
gecreëerd zichtbaar zijn in een functie zolang er maar niet een
variabele met dezelfde naam in de functie wordt gecreëerd. Variabelen
van het hoofdprogramma, die zichtbaar zijn in alle functies, worden wel
"globale" variabelen genoemd, als tegenhanger van "lokale" variabelen
die alleen binnen een functie zichtbaar zijn.

Het is een goede gewoonte om functies onafhankelijk te maken van het
hoofdprogramma, dat wil zeggen, ze geen gebruik te laten maken van
globale variabelen. Als je waardes van buiten een functie beschikbaar
wilt maken voor de functie, kun je dat doen middels parameters. Een
uitzondering kan gemaakt worden voor globale variabelen die als
constanten voor een programma gebruikt worden (zie hoofdstuk
<a href="#ch:variables" data-reference-type="ref" data-reference="ch:variables">5</a>).
Als je een functie aan een constante laat refereren, zorg er dan wel
voor dat het duidelijk is voor eenieder die de functie bekijkt dat het
inderdaad een constante is, dus dat de naam van de variabele volledig
uit hoofdletters bestaat.

Je vraagt je misschien af of het mogelijk is de waarde van globale
variabelen te wijzigen in een functie. Dat is mogelijk, maar dan moet je
in de functie expliciet duidelijk maken dat je wilt dat een wijziging
van een variabele effect moet hebben op een globale variabele. Daarvoor
is het gereserveerde woord `global` bedoeld. Het statement
`global <variabele>` geeft aan dat de variabele die je noemt een
variabele is die in het hoofdprogramma met de opgegeven naam
gedefinieerd is. Bijvoorbeeld:

```python
fruit = "appel"

def wijzigFruit():
    global fruit
    fruit = "banaan"

print( fruit )
wijzigFruit()
print( fruit )
```

Hoewel het mogelijk is de waarde van globale variabelen in functies te
wijzigen, raad ik deze constructie ten zeerste af aangezien het de
functie afhankelijk maakt van het hoofdprogramma (en dus is het niet
langer een "pure" functie). In essentie maak je op deze manier een
functie met neveneffecten, en (nu allen in koor:) *een functie mag geen
neveneffecten hebben*.

Het is nimmer nodig dat een functie globale variabelen gebruikt. Als je
wilt dat een functie globale variabelen wijzigt, laat de functie dan de
nieuwe waarde voor de globale variabele retourneren, zodat die aan de
globale variabele kan worden toegekend in het hoofdprogramma. Het
hoofdprogramma mag dan beslissen of het een variabele die van het
hoofdprogramma zelf is overschrijft. De enige reden dat ik het
gereserveerde woord `global` hier noem is dat ik soms zie dat studenten
er hun toevlucht toe nemen als ze onvoldoende begrip hebben van wat
`return` doet. Het ontkennen van het bestaan van `global` is geen
effectieve aanpak, ik geef liever toe dat het bestaat en waarschuw
studenten dat ze het niet moeten gebruiken.
