Stel dat je de gebruiker moet vragen om vijf getallen, ze moet optellen,
en dan het totaal moet laten zien. Met het materiaal dat tot nu toe
behandeld is, zou je dat als volgt coderen:

```python
from pcinput import getInteger

num1 = getInteger( "Nummer 1: " )
num2 = getInteger( "Nummer 2: " )
num3 = getInteger( "Nummer 3: " )
num4 = getInteger( "Nummer 4: " )
num5 = getInteger( "Nummer 5: " )

print( "Totaal is", num1 + num2 + num3 + num4 + num5 )
```

Maar wat als je om 500 nummers moet vragen? Ga je die regel code waar om
een getal wordt gevraagd 500 keer kopiëren? Dat moet toch op een
gemakkelijkere manier kunnen?

Natuurlijk kan dat gemakkelijker. Je kunt hiervoor een loop gebruiken.

De eerste loop die ik bespreek is de `while` loop. Een `while` statement
lijkt heel veel op een `if` statement. De syntax is:

```python
while <boolean expressie>:
    <acties>
```

Net als bij een `if` statement, test een `while` statement een boolean
expression, en als de expressie `True` oplevert, wordt het blok code
onder de `while` uitgevoerd. Echter, in tegenstelling tot een `if`
statement, gaat Python, wanneer het blok code uitgevoerd is, terug naar
de boolean expressie naast de `while`, en test die opnieuw. Als de
expressie nog steeds `True` oplevert, dan wordt het blok code nogmaals
uitgevoerd. En als het is uitgevoerd, keert Python wederom terug naar de
boolean expressie. Dit wordt steeds herhaald, totdat de boolean
expressie `False` oplevert. Pas op dat moment slaat Python het blok code
onder de `while` over en gaat eronder verder.

Merk op dat als de boolean expressie meteen `False` oplevert de eerste
keer dat Python hem ziet, dan wordt het blok code onder de `while`
onmiddellijk overgeslagen, net zoals gebeurt bij een `if` statement.

![loop](media/Loop.png "loop"){:width="70%"}

### `while` loop, eerste voorbeeld

Ik neem een eenvoudig voorbeeld: het printen van de nummers 1 tot en met
5\. Met een while loop kun je dat als volgt doen:

```python
num = 1
while num <= 5:
    print( num )
    num += 1
print( "Klaar" )
```

Deze code wordt ook weergegeven in het stroomdiagram in afbeelding
<a href="#f:chart4" data-reference-type="ref" data-reference="f:chart4">8.2</a>.

![while](media/Chart4en.png "while"){:width="60%" data-caption="Stroomdiagram dat een `while` loop weergeeft."}

Het is van essentieel belang dat je deze code snapt, dus ik neem hem
stap voor stap door.

De eerste regel initialiseert een variabele `num`. Dit is de variabele
die de code gaat afdrukken, dus hij wordt geïnitialiseerd op 1, omdat 1
de eerste waarde is die afgedrukt moet worden.

Dan start de `while` loop. De boolean expressie zegt `num <= 5`. Omdat
`num` 1 is, en 1 kleiner is dan 5, levert de expressie `True`. Dus wordt
het blok code onder de `while` uitgevoerd.

De eerste regel van het blok code print de waarde van `num`, dus 1. De
tweede regel telt 1 op bij de waarde van `num`, zodat `num` nu 2 is.
Python gaat daarna terug naar de boolean expressie. De laatste regel van
het programma, het printen van het woord "Klaar," wordt dus (nog) niet
uitgevoerd omdat hij niet in het code blok van de loop zit, en de loop
nog niet afgelopen is.

Omdat `num` 2 is, evalueert de boolean expressie nog steeds als `True`.
Het blok code wordt dus nogmaals uitgevoerd. 2 wordt afgedrukt, `num`
krijgt waarde 3, en de code keert terug bij de boolean expressie.

Omdat `num` 3 is, evalueert de boolean expressie nog steeds als `True`.
Het blok code wordt dus nogmaals uitgevoerd. 3 wordt afgedrukt, `num`
krijgt waarde 4, en de code keert terug bij de boolean expressie.

Omdat `num` 4 is, evalueert de boolean expressie nog steeds als `True`.
Het blok code wordt dus nogmaals uitgevoerd. 4 wordt afgedrukt, `num`
krijgt waarde 5, en de code keert terug bij de boolean expressie.

Omdat `num` 5 is, evalueert de boolean expressie nog steeds als `True`.
Het blok code wordt dus nogmaals uitgevoerd. 5 wordt afgedrukt, `num`
krijgt waarde 6, en de code keert terug bij de boolean expressie.

Omdat `num` 6 is, evalueert de boolean expressie als `False` (aangezien
6 niet kleiner dan of gelijk aan 5 is). Het blok code wordt
overgeslagen, en Python gaat verder met de eerste regel na het blok
code. Dat is de laatste regel van het programma. Het woord "Klaar" wordt
afgedrukt, en het programma eindigt.

Wijzig de code hierboven zodat de getallen 1, 3, 5, 7, en 9 afgedrukt
worden.

### `while` loop, tweede voorbeeld

Als je het eerste voorbeeld begrijpt, begrijp je waarschijnlijk ook hoe
je de gebruiker kunt vragen om vijf getallen, en dan de som van de vijf
te berekenen:

```python
from pcinput import getInteger

totaal = 0
teller = 0
while teller < 5:
    totaal += getInteger( "Geef een nummer: " )
    teller += 1

print( "Totaal is", totaal )
```

Bestudeer bovenstaande code. Er worden twee variabelen gebruikt.
`totaal` wordt gebruikt om de vijf getallen in op te tellen. `totaal`
begint op nul, omdat bij de start van het programma nog geen getallen
ingegeven zijn, dus het totaal is nul. `teller` wordt gebruikt om te
tellen hoe vaak de loop doorlopen is. Omdat de loop vijf keer uitgevoerd
moet worden, start `teller` op nul en de boolean expressie voor de loop
test of `teller` kleiner is dan 5. Dus teller moet iedere keer dat de
loop doorlopen wordt met 1 verhoogd worden, zodat na vijf keer doorlopen
de boolean expressie `False` is .

Je vraagt je misschien af waar ik `teller` liet starten bij 0 en de
boolean expressie liet testen of `teller < 5`. Waarom begon ik niet bij
`teller = 1` en heb ik niet `teller <= 5` getest? De reden is gewoonte:
programmeurs zijn gewend om indices bij 0 te laten beginnen en als ze
tellen, te tellen "tot maar niet inclusief." Als je verder gaat met
programmeren zul je ontdekken dat de meeste code deze gewoonte naleeft.
De meeste standaard programmeerconstructies die indices gebruiken, doen
het ook zo. Mijn advies is daarom dat je hieraan gewend raakt, want dat
zal code gemakkelijker leesbaar maken.

Opmerking: De variabele `teller` is wat programmeurs een "wegwerp
variabele" noemen. Het enige doel van deze variabele is te tellen hoe
vaak de loop doorlopen is. De variabele heeft geen echte betekenis voor
de loop, in de loop, of nadat de loop afgelopen is. Programmeurs kiezen
vaak één-letter namen voor dit soort variabelen, meestal `i` of `j` (ik
neem aan dat `i` ooit begonnen is als afkorting voor "integer," en `j`
gekozen is omdat het na `i` komt). In het voorbeeld heb ik voor de
duidelijkheid de naam `teller` gekozen, maar een `i` was acceptabel
geweest.

Wijzig de code hierboven zodat niet alleen het totaal maar ook het
gemiddelde wordt afgedrukt.

De eerste voorbeeldcode in dit hoofdstuk vroeg de gebruiker om vijf
getallen in te geven. In dat voorbeeld werd steeds de prompt "Geef
nummer `x`: " gebruikt, waarbij `x` een cijfer is. Kun je de code
hierboven, waarin een loop gebruikt wordt, zo veranderen dat ook steeds
een veranderende prompt wordt gebruikt voor de getallen?

### De `while` loop onder controle van de gebruiker

Stel je voor dat je in het tweede voorbeeld de gebruiker niet wilt
beperken tot slechts vijf getallen. Je wil de gebruiker zoveel getallen
laten ingeven als hij wil, inclusief helemaal geen getallen. Dat
betekent dat je niet weet hoe vaak de loop doorlopen moet worden. In
plaats daarvan bepaalt de gebruiker hoe vaak de loop doorlopen wordt. Je
moet dus de gebruiker de mogelijkheid geven om aan te geven dat hij
klaar is met getallen ingeven.

De code hieronder laat zien hoe je een `while` loop kunt opzetten die de
gebruiker zoveel getallen laat ingeven als gewenst. De gebruiker stopt
met het ingeven van getallen door een nul in te geven. Het totaal wordt
afgedrukt wanneer de loop beëindigd is.

```python
from pcinput import getInteger
    
num = -1
totaal = 0
while num != 0:
    num = getInteger( "Geef een nummer: " )
    totaal += num
print( "Totaal is", totaal )
```

Deze code functioneert, maar er zitten minimaal twee lelijke dingen in.
Op de eerste plaats wordt `num` geïnitialiseerd op -1. De -1 zelf is
betekenisloos, ik moest gewoon een waarde hebben die ervoor zou zorgen
dat de loop minstens één keer uitgevoerd zou worden. Ten tweede stopt de
loop niet meteen als de gebruiker nul ingeeft; in plaats daarvan wordt
de ingave van de gebruiker opgeteld bij `totaal`. Omdat die ingave nul
is, wijzigt `totaal` niet, maar als ik had gesteld dat de gebruiker de
loop eindigt door bijvoorbeeld een negatief getal in te geven, dan zou
`totaal` daarna de verkeerde waarde bevatten.

Vanwege deze lelijke kanten aan de code, prefereren sommige programmeurs
om het als volgt te schrijven:

```python
from pcinput import getInteger
    
num = getInteger( "Geef een nummer: " )
totaal = 0
while num != 0:
    totaal += num
    num = getInteger( "Geef een nummer: " )
print( "Totaal is", totaal )
```

Dit lost de twee hierboven genoemde lelijke zaken op, maar introduceert
iets anders lelijks, namelijk de herhaling van de `getInteger()`
functie. Hoe je dat kunt oplossen volgt later in dit hoofdstuk. Op dit
moment hoef je alleen te snappen hoe de `while` loop werkt.

Maak een loop die de gebruiker een aantal getallen laat ingeven, totdat
hij nul ingeeft, en dan het totaal en het gemiddelde afdrukt. Vergeet
niet te testen met nul getallen ingeven, en met een aantal keer
hetzelfde getal ingeven.

### Eindeloze loops

De code hieronder begint bij nummer 1, en telt nummers op, totdat het
een nummer tegenkomt dat, als het gekwadrateerd wordt, deelbaar is door
1000\. De loop bevat een fout. Kijk of je de fout weet te vinden (zonder
de code uit te voeren!).

```python
nummer = 1
totaal = 0
while (nummer * nummer) % 1000 != 0:
    totaal += nummer
print( "Totaal is", totaal )
```

De titel boven deze paragraaf gaf het antwoord natuurlijk al weg: deze
code bevat een loop die nooit eindigt. Als je hem uitvoert, lijkt het
alsof het programma "hangt," dus wel draait maar niks doet. Maar het
doet niet niks, het is zelfs hoogst actief, maar het is bezig een
nooit-eindigende optelling uit te voeren. `nummer` begint bij 1, maar
wordt in de loop niet gewijzigd. Daarom wordt de boolean expressie nooit
`False`. Dit is een "eindeloze loop." Dit soort loops zijn het grootste
gevaar als je `while` loops bouwt.

Als je deze code uitvoert in IDLE, kun je de uitvoering afbreken door
`Ctrl-C` te drukken. Andere editors hebben menu opties waarmee je de
uitvoering van code kunt onderbreken. In gebruikersonvriendelijke
omgevingen moet je soms het proces waarin Python draait via een systeem
commando of systeem programma afbreken.

Omdat iedere programmeur zo nu en dan per ongeluk een eindeloze loop
schrijft, is het een goed idee als je, wanneer je begint met het
schrijven van een `while` loop, onmiddellijk een regel code toevoegt die
een wijziging maakt in hetgeen getest wordt in de boolean expressie,
zodat je dat niet vergeet. Bijvoorbeeld, als je schrijft `while i < 10`,
dan schrijf je er meteen de regel `i += 1` onder, en daarna begin je de
rest van de code tussen deze twee regels toe te voegen.

Verbeter de code hierboven zodat het geen eindeloze loop meer is.

### `while` loop oefeningen

Je moet nu oefenen met een paar eenvoudige `while` loops.

Schrijf code die aftelt. Er wordt begonnen met een specifiek nummer,
bijvoorbeeld 10. Dan telt de code af naar nul, waarbij ieder nummer
geprint wordt (10, 9, 8, …). Nul wordt niet geprint, maar in plaats
daarvan drukt het programma de tekst "Start!" af.

De faculteit van een positief geheel getal is gelijk aan dat getal,
vermenigvuldigd met alle positieve gehele getallen die kleiner zijn
(exclusief nul). Je schrijft de faculteit als het getal met een
uitroepteken erachter. Bijvoorbeeld, de faculteit van 5 is
$$5! = 5 * 4 * 3 * 2 * 1 = 120$$. Schrijf code die de faculteit van een
getal berekent. Test het programma niet met getallen die hoog zijn, want
de faculteit stijgt exponentieel (het is meer dan genoeg om tot 10! te
testen). Hint: Om dit met een `while` loop te doen, moet je twee
variabelen gebruiken: één die aan het einde van de loop het antwoord
bevat, en één die de huidige factor bevat. In de loop vermenigvuldig je
het antwoord met de factor, alvorens 1 van de factor af te trekken.
Initialiseer deze variabelen met de juiste waardes voor de loop.
