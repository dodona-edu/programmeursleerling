Deze appendix bevat de antwoorden bij de meeste opgaves. Al deze
antwoorden zijn ook beschikbaar als bestanden, te downloaden via
<http://www.spronck.net/pythonbook>{:target="_blank"}.

Het is zinloos om deze antwoorden te bekijken als je niet zelf intensief
hebt geprobeerd de opgaves op te lossen. Je kunt alleen programmeren
leren door het te doen. Gebruik deze antwoorden alleen om ze te
vergelijken met je eigen oplossingen, of als een laatste redmiddel als
je geen idee hebt over hoe je een probleem moet aanpakken. Maar als je
een probleem niet kunt oplossen, is het meestal beter om er een eerder
deel van het boek op na te slaan om informatie op te zoeken die je niet
hebt begrepen of vergeten bent.

Vaak zijn de antwoorden die ik geef slechts één van vele mogelijkheden
om een opgave op te lossen. Als jij een andere manier hebt gevonden, kan
dat best correct zijn, maar zorg ervoor dat je je oplossingen uitgebreid
test om er zeker van te zijn dat ze correct zijn.

Bedenk dat, hoewel de antwoorden die ik geef meestal efficiënt zijn,
efficiëntie niet een hoofddoel is wanneer je code schrijft. Je hoofddoel
is om code te schrijven die een probleem oplost, en pas als dat gelukt
is, moet je overwegen of de oplossing efficiënter gemaakt kan worden.
Leesbaarheid en onderhoudbaarheid zijn veel belangrijker dan
efficiëntie.

### Hoofdstuk 2

#### Antwoord 1.1

Een recht-toe-recht-aan sortering die eerste de hoogste kaart zoekt, dan
de op-één-na-hoogste, etcetera, heeft zes vergelijkingen nodig. Je kunt
het bijvoorbeeld als volgt doen:

Nummer de kaarten van 1 tot 4, links naar rechts. Het nummer hoort bij
de positie waar de kaart ligt, dus als je twee kaarten omwisselt, dan
wissel je in feite hun nummers. Vergelijk kaarten 1 en 2 en verwissel ze
als 1 hoger is dan 2. Vergelijk kaarten 2 en 3 en verwissel ze als 2
hoger is dan 3. Vergelijk kaarten 3 en 4 en verwissel ze als 3 hoger is
dan 4. 4 is nu de kaart met het hoogste nummer. Vergelijk nu kaarten 1
en 2 weer, en verwissel ze als 1 hoger is dan 2. Vergelijk kaarten 2 en
3 weer, en verwissel ze als 2 hoger is dan 3. De op-één-na-hoogste kaart
is nu 3. Tenslotte vergelijk je kaarten 1 en 2, en verwisselt ze als 1
hoger is dan 2. Je hebt nu de kaarten gesorteerd, waarbij je zes
vergelijkingen nodig had.

Om het met minder vergelijkingen te doen, heb je een ietwat complexere
procedure nodig. Begin weer met het nummeren van de kaarten, van 1 tot
4. Vergelijk kaarten 1 en 2 en verwissel ze als 1 hoger is dan 2.
Vergelijk nu kaarten 3 en 4, en verwissel ze als 3 hoger is dan 4.
Vergelijk dan 1 met 3. Als 1 hoger is dan 3, verwissel je zowel kaart 1
en 3, als kaart 2 en 4. De laagste kaart ligt nu op plek 1, en je weet
ook dat kaart 3 lager is dan kaart 4. Vergelijk nu kaarten 2 en 3. Als 2
lager is dan 3 ben je klaar met slechts vier vergelijkingen, je hoeft
niks meer te vergelijken of te verwisselen. Als 2 echter hoger is dan 3,
moet je 2 en 3 omwisselen. Je moet dan nog steeds 3 en 4 vergelijken, en
omwisselen als 3 hoger is dan 4. Maar dan ben je klaar, met slechts vijf
vergelijkingen. Dus je kunt vier kaarten sorteren met minimaal vier en
maximaal vijf vergelijkingen.

Misschien denk je nu slim te zijn en, als je 1 en 2 vergeleken (en
misschien verwisseld) hebt, en 3 en 4 vergeleken (en misschien
verwisseld) hebt, je 2 en 3 moet vergelijken, want als op dat moment 2
lager is dan 3, dan ben je klaar met slechts 3 vergelijkingen. Echter,
als op dat moment 2 hoger blijkt te zijn dan 3, zou dat kunnen betekenen
dat je toch zes vergelijkingen nodig hebt.

Als programmeren nieuw voor je is, dan zal het lastig zijn de procedure
met maximaal vijf vergelijkingen te verzinnen. Raak dus niet ontmoedigd
als je daar niet opkomt. Het is belangrijker dat je een taak weet op te
lossen dan dat je hem op de meest efficiënte manier weet op te lossen.

#### Antwoord 1.2

Een goede aanpak is vier rechthoeken op een stuk papier te zetten en
deze te nummeren, en dan een kaart in iedere rechthoek te plaatsen. Zeg
tegen de persoon die de instructies gaat uitvoeren dat "vergelijk de
kaart in rechthoek $$x$$ met de kaart in rechthoek $$y$$" betekent dat hij
of zij aan de processor moet vragen die kaarten op te rapen, te
bekijken, en ze terug te leggen waar ze vandaan kwamen, en daarna aan te
geven welke de hoogste van de twee is. Dan kun je de volgende
instructies geven voor de simpele, zes-stappen procedure die ik
hierboven beschrijf:

1.  Vergelijk de kaart in rechthoek 1 met de kaart in rechthoek 2. Als
    de kaart in rechthoek 1 hoger is dan de kaart in rechthoek 2,
    verwissel ze dan.

2.  Vergelijk de kaart in rechthoek 2 met de kaart in rechthoek 3. Als
    de kaart in rechthoek 2 hoger is dan de kaart in rechthoek 3,
    verwissel ze dan.

3.  Vergelijk de kaart in rechthoek 3 met de kaart in rechthoek 4. Als
    de kaart in rechthoek 3 hoger is dan de kaart in rechthoek 4,
    verwissel ze dan.

4.  Vergelijk de kaart in rechthoek 1 met de kaart in rechthoek 2. Als
    de kaart in rechthoek 1 hoger is dan de kaart in rechthoek 2,
    verwissel ze dan.

5.  Vergelijk de kaart in rechthoek 2 met de kaart in rechthoek 3. Als
    de kaart in rechthoek 2 hoger is dan de kaart in rechthoek 3,
    verwissel ze dan.

6.  Vergelijk de kaart in rechthoek 1 met de kaart in rechthoek 2. Als
    de kaart in rechthoek 1 hoger is dan de kaart in rechthoek 2,
    verwissel ze dan.

Het idee om genummerde rechthoeken te gebruiken om aan kaarten te
refereren is vergelijkbaar met het gebruiken van variabelen in een
computerprogramma. Variabelen worden uitgelegd in hoofdstuk
5.
Het uitleggen van de meer efficiënte procedure die hierboven staat is
een stuk lastiger, omdat je er geneste condities voor nodig hebt.

### Hoofdstuk 3

#### Antwoord 2.1

Python draait nu op je computer. Gefeliciteerd!

#### Antwoord 2.2

Je ziet niets in de shell (behalve het woord `RESTART` dat je altijd
ziet als je een programma draait). $$7/4$$ is een correct Python commando,
dus het programma geeft geen foutmelding. Het programma rekent $$7/4$$
uit, maar toont geen resultaat, dus het programma laat niet $$1.75$$ zien.
De shell toont het resultaat van het draaien van het programma. Maar
omdat het programma zelf geen resultaat heeft, is er ook niks dat de
shell kan laten zien. Dus je ziet niets.

### Hoofdstuk 4

#### Antwoord 3.1

```python
print( 60 * (0.6 * 24.95 + 0.75) + (3 - 0.75) )
```

#### Antwoord 3.2

Alle regels moeten `print( "Een boodschap" )` zijn (of hetzelfde maar
met de string tussen enkele aanhalingstekens). De fout in de eerste
regel is dat er een punt achter staat. Die punt moet weg. De fout in de
tweede regel is dat er iets staat dat een string zou moeten zijn, maar
dat start met een dubbel aanhalingsteken en eindigt met een enkel
aanhalingsteken. Ofwel het dubbele aanhalingsteken moet een enkel
aanhalingsteken worden, of andersom. De derde regel is strict genomen
niet fout, maar waarschijnlijk was de bedoeling ervan dat de `f"` er
niet zou staan.

#### Antwoord 3.3


```python
print( 1/0 )
```

#### Antwoord 3.4

Het probleem is dat er een enkel sluithaakje ontbreekt op de eerste
regel code. Ik heb het haakje verwijderd dat ik origineel had geschreven
na de $$6$$, maar dat kun je niet meer weten; je kunt slechts de haakjes
tellen en zien dat er een sluithaakje ontbreekt.

Het verwarrende is dat de foutboodschap zegt dat er een fout is gevonden
op de tweede regel. De tweede regel is echter correct. De reden dat
Python de tweede regel aanduidt als fout, is dat Python dat laatste
sluithaakje niet heeft gevonden op de eerste regel, en dus verwacht dat
de regel doorloopt op de tweede regel. Daarna ontdekt Python dat er iets
mis is, en rapporteert de fout.

Dit kom je soms ook in je eigen code tegen: er wordt een fout
gerapporteerd op een bepaalde regel, maar de echte fout is al gemaakt op
een eerdere regel. Dit soort fouten betreffen vaak het ontbreken van
haakjes of aanhalingstekens. Houd daar rekening mee.

#### Antwoord 3.5

```python
print( str( (14 + 535) % 24 ) + ".00" )
```

### Hoofdstuk 5

#### Antwoord 4.1


```python
# Dit programma berekent het gemiddelde van 3 variabelen:
# var1, var2, en var3
var1 = 12.83
var2 = 99.99
var3 = 0.12
gemiddelde = (var1 + var2 + var3) / 3 # Berekening
print( gemiddelde ) # Ziet er wat lelijk uit, maar
# dat wordt beter na een discussie over formattering
```

#### Antwoord 4.2

```python
pi = 3.14159
straal = 12
print( "De oppervlakte van een cirkel met straal",
    straal, "is", pi * straal * straal )
```

#### Antwoord 4.3

```python
CENTEN_IN_DOLLAR = 100
CENTEN_IN_KWARTJE = 25
CENTEN_IN_DUBBELTJE = 10
CENTEN_IN_STUIVER = 5

bedrag = 1156
centen = bedrag

dollars = int( centen / CENTEN_IN_DOLLAR )
centen -= dollars * CENTEN_IN_DOLLAR
kwartjes = int( centen / CENTEN_IN_KWARTJE )
centen -= kwartjes * CENTEN_IN_KWARTJE
dubbeltjes = int( centen / CENTEN_IN_DUBBELTJE )
centen -= dubbeltjes * CENTEN_IN_DUBBELTJE
stuivers = int( centen / CENTEN_IN_STUIVER )
centen -= stuivers * CENTEN_IN_STUIVER
centen = int( centen )

print( bedrag / CENTEN_IN_DOLLAR, "bestaat uit:" )
print( "Dollars:", dollars )
print( "Kwartjes:", kwartjes )
print( "Dubbeltjes:", dubbeltjes )
print( "Stuivers:", stuivers )
print( "Centen:", centen )
```

#### Antwoord 4.4

```python
a = 17
b = 23
print( "a =", a, "en b =", b )
a += b
b = a - b
a -= b
print( "a =", a, "en b =", b )
```

### Hoofdstuk 6

#### Antwoord 5.1

```python
s = input( "Geef een string: " )
print( "Je hebt", len( s ), "letters ingegeven" )
```

#### Antwoord 5.2

```python
from pcinput import getFloat
from math import sqrt

zijde1 = getFloat( "Geef de lengte van de eerste zijde: " )
zijde2 = getFloat( "Geef de lengte van de tweede zijde: " )
zijde3 = sqrt( zijde1 * zijde1 + zijde2 * zijde2 )
print( "De lengte van de diagonaal is {:.3f}.".format( zijde3 ) )
```

#### Antwoord 5.3

```python
from pcinput import getFloat

num1 = getFloat( "Geef nummer 1: " )
num2 = getFloat( "Geef nummer 2: " )
num3 = getFloat( "Geef nummer 3: " )

print( "De grootste is", max( num1, num2, num3 ) )
print( "De kleinste is", min( num1, num2, num3 ) )
print( "Het gemiddelde is", round( (num1 + num2 + num3)/3, 2 ) )
```

#### Antwoord 5.4

```python
from math import exp

s = "e tot de macht {:2d} is {:>9.5f}"
print( s.format( -1, exp( -1 ) ) )
print( s.format( 0, exp( 0 ) ) )
print( s.format( 1, exp( 1 ) ) )
print( s.format( 2, exp( 2 ) ) )
print( s.format( 3, exp( 3 ) ) )
```

#### Antwoord 5.5

```python
from random import random

print( "Een toevalsgetal tussen 1 en 10 is",
    1 + int( random() * 10 ) )
```

### Hoofdstuk 7

#### Antwoord 6.1

```python
from pcinput import getFloat

grade = getFloat( "Geef een cijfer: " )
check = int( grade * 10 )
if grade < 0 or grade > 10:
    print( "Cijfers liggen tussen 0 en 10." )
elif check%5 != 0 or check != grade*10:
    print( "Cijfers zijn afgerond op halve punten." )
elif grade >= 8.5:
    print( "A" )
elif grade >= 7.5:
    print( "B" )
elif grade >= 6.5:
    print( "C" )
elif grade >= 5.5:
    print( "D" )
else:
    print( "F" )
```

#### Antwoord 6.2

De enig mogelijke antwoorden zijn "D" en "F," aangezien de tests in de
verkeerde volgorde zijn geplaatst. Bijvoorbeeld, als de score 85 is, dan
is dat niet alleen groter dan 80.0, maar ook groter dan 60.0, dus de
uitkomst zal dan "D" zijn.

#### Antwoord 6.3

```python
from pcinput import getString

s = getString( "Geef een string: " )
count = 0
if ("a" in s) or ("A" in s):
    count += 1
if ("e" in s) or ("E" in s):
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1

if count == 0:
    print( "Er zitten geen klinkers in de string." )
elif count == 1:
    print( "Er zit maar 1 verschillende klinker in de string." )
else:
    print( "Er zijn", count, "verschillende klinkers." )
```

#### Antwoord 6.4

```python
from pcinput import getFloat
from math import sqrt

a = getFloat( "A: " )
b = getFloat( "B: " )
c = getFloat( "C: " )

if a == 0:
    if b == 0:
        print( "Deze vergelijking heeft geen onbekende!" )
    else:
        print( "Er is 1 oplossing, namelijk", -c/b )
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print( "Er zijn geen oplossingen" )
    elif discriminant == 0:
        print( "Er is 1 oplossing, namelijk", -b/(2*a) )
    else:
        print( "Er zijn 2 oplossingen, namelijk",
                (-b+sqrt(discriminant))/(2*a), "en",
                (-b-sqrt(discriminant))/(2*a) )
```

### Hoofdstuk 8

#### Antwoord 7.1

```python
from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
i = 1
while i <= 10:
    print( i, "*", num, "=", i*num )
    i += 1
```

#### Antwoord 7.2

```python
from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
for i in range( 1, 11 ):
    print( i, "*", num, "=", i*num )
```

#### Antwoord 7.3

```python
from pcinput import getInteger

AANTAL = 10
grootste = 0
kleinste = 0
deelbaar3 = 0

for i in range( AANTAL ):
    num = getInteger( "Geef nummer "+str( i+1 )+": " )
    if num%3 == 0:
        deelbaar3 += 1
    if i == 0:
        kleinste = num
        grootste = num
        continue
    if num < kleinste:
        kleinste = num
    if num > grootste:
        grootste = num

print( "Kleinste is", kleinste )
print( "Grootste is", grootste )
print( "Deelbaar door 3 is", deelbaar3 )
```

#### Antwoord 7.4

```python
flessen = 10
s = "s"
while flessen != "geen":
    print( "{0} flesje{1} met bier op de muur, "\
        "{0} flesje{1} met bier.".format( flessen, s ) )
    flessen -= 1
    if flessen == 1:
        s = ""
    elif flessen == 0:
        s = "s"
        flessen = "geen"
    print( "Open er een, drink hem meteen, {} flesje{} "\
        "met bier op de muur.".format( flessen, s ) )
```

Als je een backslash (`\`) plaatst aan het einde van een regel code, dan
wordt de volgende regel aan de regel met de backslash geplakt. Als
hierdoor twee strings tegen elkaar aan komen te staan, dan worden die
samen als één string beschouwd. Ik gebruik dat hier om ervoor te zorgen
dat de code past binnen de breedte van de pagina. Ik vertel er meer over
in hoofdstuk
11.
Je hebt het zelf niet nodig: je kunt het hele `print()` statement op een
lange regel schrijven.

#### Antwoord 7.5

```python
num1 = 0
num2 = 1
print( 1, end=" " )
while True:
    num3 = num1 + num2
    if num3 > 1000:
        break
    print( num3, end=" " )
    num1 = num2
    num2 = num3
```

#### Antwoord 7.6

```python
from pcinput import getString

woord1 = getString( "Geef woord 1: " )
woord2 = getString( "Geef woord 2: " )
gemeen = ""
for letter in woord1:
    if (letter in woord2) and (letter not in gemeen):
        gemeen += letter

if gemeen == "":
    print( "De woorden hebben geen tekens gemeen." )
else:
    print( "De woorden delen de volgende tekens:", gemeen )
```

#### Antwoord 7.7

```python
from random import random

DARTS = 100000
raak = 0
for i in range( DARTS ):
    x = random()
    y = random()
    if x*x + y*y < 1:
        raak += 1

print( "Een redelijke benadering van pi is", 4 * raak / DARTS )
```

#### Antwoord 7.8

```python
from random import randint
from pcinput import getInteger

antwoord = randint( 1, 1000 )
teller = 0
while True:
    poging = getInteger( "Raad een getal: " )
    if poging < 1 or poging > 1000:
        print( "Je moet een getal tussen de 1 en 1000 noemen" )
        continue
    teller += 1
    if poging < antwoord:
        print( "Hoger" )
    elif poging > antwoord:
        print( "Lager" )
    else:
        print( "Je hebt het geraden!" )
        break

if teller == 1:
    print( "Je hoefde maar 1 keer te raden. Geluksvogel." )
else:
    print( "Je moest", teller, "keer raden." )
```

#### Antwoord 7.9

```python
from pcinput import getLetter
from sys import exit

teller = 0
laagste = 0
hoogste = 1001
print( "Denk aan een getal tussen 1 en 1000." )

while True:
    poging = int( (laagste + hoogste) / 2 )
    teller += 1
    prompt = "Ik raad "+str( poging )+". Is jouw getal"+\
        " (L)ager of (H)oger, of is dit (C)orrect? "
    antwoord = getLetter( prompt )
    if antwoord == "C":
        break
    elif antwoord == "L":
        hoogste = poging
    elif antwoord =="H":
        laagste = poging
    else:
        print( "Antwoord H, L, of C." )
        continue
    if laagste >= hoogste-1:
        print( "Je moet een fout gemaakt hebben,",
            "want je hebt gezegd dat het getal hoger is dan",
            laagste, "maar ook lager dan", hoogste )
        print( "Ik stop ermee" )
        exit()

if teller == 1:
    print( "In 1 keer geraden! Ik kan gedachten lezen!" )
else:
    print( "Ik moest", teller, "keer raden." )
```

#### Antwoord 7.10

```python
from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
if num < 2:
    print( num, "is niet priem" )
else:
    i = 2
    while i*i <= num:
        if num%i == 0:
            print( num, "is niet priem" )
            break
        i += 1
    else:
        print( num, "is priem" )
```

Ik heb in deze code een handigheidje gebruikt om de berekening veel
sneller te laten lopen. De code test de delers tot aan de wortel uit
`num` (dus het test tot het moment dat `i*i > num`). De reden is dat als
er een getal is dat groter is dan de grens van deze test, dat een deler
is van `num`, dan is er ook een getal dat kleiner is dan deze grens dat
een deler is. Bijvoorbeeld, als `num` 21 is, ligt de wortel tussen 4 en
5. Het algoritme test daarom alleen getallen tot en met 4. Er is een
deler voor 21 die groter is dan 4, namelijk 7. Maar dat betekent dat er
ook een deler is die kleiner dan (of gelijk aan) 4 is, en die is er
inderdaad, namelijk 3. Deze handigheid veroorzaakt een enorme
versnelling van het algoritme ten opzichte van het testen van alle
getallen tot `num`; bijvoorbeeld, als `num` in de buurt is van 1
miljoen, en het is priem, dan zou je ongeveer 1 miljoen getallen moeten
testen om te concluderen dat het priem is als je deze grens niet zou
aanhouden, terwijl mijn algoritme slechts duizend getallen test.

Als je deze handigheid gevonden hebt, geweldig! Zo niet, maar je geen
zorgen: als je code werkt, gaat het je tot nu toe prima af. Het
lastigste is code werkend te krijgen. Als je daarin slaagt, ben je op
weg een goed programmeur te worden.

Een laatste opmerking: zorg dat je je code uitgebreid test! Het is
gemakkelijk om fouten te maken met specifieke getallen. In dit geval,
zorg dat je in ieder geval een negatief getal test, nul, 1 (alledrie
geen priemgetallen), 2 (het eerste en enige even priemgetal), 3 (het
laagste oneven priemgetal), diverse niet-priemgetallen, diverse
priemgetallen, een paar grote priemgetallen, en getallen die een
kwadraat zijn van een priemgetal (bijvoorbeeld 25). Nog beter is als je
een loop schrijft rond je code die alle getallen test tussen,
bijvoorbeeld, -10 en 100. Dan ben je echt met een intensieve test bezig.

#### Antwoord 7.11

```python
num = 9
print( ". |", end="" )
for i in range( 1, num+1 ):
    print( "{:>3}".format( i ), end="" )
print()
for i in range( 3*(num+1) ):
    print( "-", end="" )
print()
for i in range( 1, num+1 ):
    print( i, "|", end="" )
    for j in range( 1, num+1 ):
        print( "{:>3}".format( i*j ), end="" )
    print()
```

#### Antwoord 7.12

```python
for i in range( 1, 101 ):
    for j in range( 1, i ):
        for k in range( j, i ):
            if j*j + k*k == i:
                print( "{} = {}**2 + {}**2".format( i, j, k ) )
```

Een meer efficiënte versie van dit algoritme is:

```python
from math import sqrt

for i in range( 1, 101 ):
    for j in range( 1, int( sqrt( i ) )+1 ):
        for k in range( j, int( sqrt( i ) )+1 ):
            if j*j + k*k == i:
                print( "{} = {}**2 + {}**2".format( i, j, k ) )
```

Deze reden dat dit een efficiënter algoritme is, en waarom het werkt, is
hierboven beschreven voor de priemgetallen opgave.

#### Antwoord 7.13

```python
from random import randint

POGINGEN = 10000
DOBBELSTENEN = 5

succes = 0

for i in range( POGINGEN ):
    laatste = 0
    for j in range( DOBBELSTENEN ):
        waarde = randint( 1, 6 )
        if waarde < laatste:
            break
        laatste = waarde
    else:
        succes += 1

print( "De waarschijnlijkheid van een oplopende serie van vijf",
    "dobbelsteen worpen is {:.3f}".format( succes/POGINGEN ) )
```

#### Antwoord 7.14

```python
for A in range( 1, 10 ):
    for B in range( 10 ):
        if B == A:
            continue
        for C in range( 10 ):
            if C == A or C == B:
                continue
            for D in range( 1, 10 ):
                if D == A or D == B or D == C:
                    continue
                num1 = 1000*A + 100*B + 10*C + D
                num2 = 1000*D + 100*C + 10*B + A
                if num1 * 4 == num2:
                    print( "A={}, B={}, C={}, D={}".format(
                        A, B, C, D ) )
```

Dit programma genereert alle combinaties van A, B, C, en D die de puzzel
oplossen. Er is er echter maar één. Het programma zoekt toch verder
totdat alle combinaties getest zijn. Dat is gelukkig een erg snel
proces. Als je het programma wilt afbreken als een oplossing gevonden
is, is de beste aanpak een functie te schrijven die deze code bevat, en
die functie af te breken als de oplossing gevonden is. Functies worden
besproken in het volgende hoofdstuk.

#### Antwoord 7.15

```python
PIRATES = 5
kokosnoten = 0
while True:
    kokosnoten += 1
    stapel = kokosnoten
    for i in range( PIRATES ):
        if stapel % PIRATES != 1:
            break
        stapel = (PIRATES-1) * int( (stapel - 1) / PIRATES )
    if stapel % PIRATES == 1:
        break
print( kokosnoten )
```

Deze oplossing start met nul kokosnoten en blijft kokosnoten aan de
stapel toevoegen totdat iedere piraat zijn deel kan nemen en 1 kokosnoot
overhoudt, steeds het deel van de piraat en die ene kokosnoot van de
stapel verwijderend. Om te testen of er een kokosnoot overblijft na de
verdeling wordt de modulo operator gebruikt. Nadat alle piraten hun deel
hebben genomen, is het probleem opgelost als er 1 kokosnoot overblijft
na een eerlijke verdeling van de overgebleven stapel.

Vind je het niet verbazend dat je een probleem met zo'n lange
beschrijving kunt oplossen met zo weinig code?

#### Antwoord 7.16

Ik geef eerst een oplossing die iedere Driehoekkruiper apart simuleert.
Deze oplossing is gemakkelijk te begrijpen:

```python
from random import randint

NUMKRUIPERS = 100000
leeftijd = NUMKRUIPERS # Ze leven minstens een dag

for i in range( NUMKRUIPERS ):
    if randint( 0, 2 ): # Sterf niet op dag 1
        leeftijd += 1
        while randint( 0, 1 ): # Sterf niet
            leeftijd += 1

print( "{:.2f}".format( leeftijd / NUMKRUIPERS ) )
```

De tweede oplossing beschouwt de populatie als een geheel, en verdeelt
hem in groepen. Op de eerste dag wordt een-derde van de groep afgehaald,
en het programma telt 1 dag op bij de totale leeftijd voor ieder van de
Kruipers in die groep. Op de tweede dag wordt de helft van de
overgeblevenen afgehaald, en wordt 2 dagen voor ieder van hen opgeteld
bij de totale leeftijd. De derde dag wordt weer de helft eraf gehaald,
en bij de totale leeftijd wordt opgeteld dat zij drie dagen leefden. Dit
gaat door totdat de populatie op is. Soms blijft er een enkele Kruiper
over omdat de groep niet netjes verdeeld kan worden (omdat een Kruiper
leeft of sterft, maar niet Schrödinger's Kat kan zijn). Zo'n Kruiper
wordt per toeval aan de levenden of de stervenden toebedeeld. Je ziet
dat deze code kan omgaan met enorm grote aantallen Driehoekkruipers
zonder problemen.

```python
from random import randint

NUMKRUIPERS = 1000000000
num = NUMKRUIPERS
dood = int( num / 3 )
if NUMKRUIPERS % 3:
    if randint( 0, NUMKRUIPERS % 3 ): # Kruiper over op dag 1
        dood += 1
leeftijd = dood # Dag-1 doden leven 1 dag
num -= dood

dag = 2
while num > 0:
    dood = int( num / 2 )
    num -= dood # Dood de helft
    if dood != num: # Er is er 1 over
        if randint( 0, 1 ): # Besluit of 1 sterft
            dood, num = num, dood # Verwissel waardes
    leeftijd += dood * dag
    dag += 1

print( "{:.2f}".format( leeftijd / NUMKRUIPERS ) )
```

Tenslotte geef ik hier een oplossing die ik niet suggereerde, maar die
geweldig werkt. Hij is erg kort, ongelofelijk snel, en geeft een vrijwel
exact antwoord. De oplossing berekent eenvoudigweg een benadering van

$$\frac{1}{3} + \frac{2}{3}(\frac{1}{2}(2 + \frac{1}{2}(3 + \frac{1}{2}(4 + \frac{1}{2}(5 + \hellip) ) ) ) )$$

Het gebruikt slechts 100 termen van deze berekening, maar dat is meer
dan genoeg om een zeer nauwkeurige benadering van het antwoord te
krijgen. Dit is natuurlijk een berekening en geen simulatie, maar het is
de wiskundige expressie die je feitelijk werd gevraagd op te lossen.

```python
schatting = 1/3
rest = 2/3
for dagen in range( 2, 101 ):
    rest /= 2
    schatting += rest * dagen
print( "{:.2f}".format( schatting ) )
```

Het exacte antwoord is overigens $$2\frac{1}{3}$$ dagen; een benadering
moet 2.33 of 2.34 geven.

### Hoofdstuk 9

#### Antwoord 8.1

```python
from pcinput import getInteger

# tafel krijgt een integer als parameter. Het drukt de
# tafel van vermenigvuldiging voor deze integer af.
def tafel( n ):
    i = 1
    while i <= 10:
        print( i, "*", n, "=", i*n )
        i += 1

num = getInteger( "Geef een getal: " )
tafel( num )
```

#### Antwoord 8.2

```python
from pcinput import getString

# gemeen krijgt twee strings als parameters. Het retourneert
# het aantal tekens dat de strings gemeen hebben.
def gemeen( w1, w2 ):
    tekens = ""
    for letter in w1:
        if (letter in w2) and (letter not in tekens):
            tekens += letter
    return len( tekens )

woord1 = getString( "Geef woord 1: " )
woord2 = getString( "Geef woord 2: " )

num = gemeen( woord1, woord2 )
if num <= 0:
    print( "De woorden delen geen tekens." )
elif num == 1:
    print( "De woorden hebben 1 teken gemeen" )
else:
    print( "De woorden hebben", num, "tekens gemeen" )
```

#### Antwoord 8.3

```python
# gregoryLeibnitz benadert pi middels de Gregory-Leibnitz
# reeks. Hij krijgt 1 parameter, een integer, die aangeeft
# hoeveel termen berekend worden. De benadering wordt als
# float geretourneerd.
def gregoryLeibnitz( num ):
    appr = 0
    for i in range( num ):
        if i%2 == 0:
            appr += 1/(1 + i*2)
        else:
            appr -= 1/(1 + i*2)
    return 4*appr

print( gregoryLeibnitz( 50 ) )
```

#### Antwoord 8.4

```python
from pcinput import getFloat
from math import sqrt

# Deze functie lost een kwadratische vergelijking op.
# De parameters zijn numerieke waardes voor A, B, and C in de
# vergelijking Ax**2 + Bx + C = 0. Het retourneert drie waardes.
# De eerste is een integer 0, 1, of 2, die aangeeft hoeveel
# oplossingen er zijn. Daarna volgen de oplossingen.
# Zonder oplossingen zijn beide 0. 1 oplossing wordt geretourneerd
# als de eerste van de twee, en de tweede is 0.
def wortelformule( a, b, c ):
    if a == 0:
        if b == 0:
            return 0, 0, 0
        return 1, -c/b, 0
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0, 0, 0
    elif discriminant == 0:
        return 1, -b/(2*a), 0
    else:
        return 2, (-b+sqrt(discriminant))/(2*a), \
            (-b-sqrt(discriminant))/(2*a)

num, opl1, opl2 = wortelformule( getFloat( "A: " ),
    getFloat( "B: " ), getFloat( "C: " ) )
if num == 0:
    print( "Er zijn geen oplossingen" )
elif num == 1:
    print( "Er is 1 oplossing, namelijk", opl1 )
else:
    print( "Er zijn 2 oplossingen, namelijk:", opl1, "en", opl2 )
```

#### Antwoord 8.5

```python
from pcinput import getInteger

def getNummer( prompt ):
    while True:
        num = getInteger( prompt )
        if num < 0 or num > 1000:
            print( "Geef een getal tussen 1 en 1000" )
            continue
        return num

def main():
    while True:
        x = getNummer( "Geef nummer 1: " )
        if x == 0:
            break
        y = getNummer( "Geef nummer 2: " )
        if y == 0:
            break
        if x%y == 0 or y%x == 0:
            print( "Fout: de nummers mogen geen delers zijn" )
            return
        print( "Vermenigvuldiging van",x,"met",y,"geeft",x*y )
    print( "Tot ziens!" )

if __name__ == '__main__':
    main()
```

#### Antwoord 8.6

```python
# Berekent de faculteit van de paremeter n, een integer.
# Retourneert de uitkomst als integer.
def faculteit( n ):
    waarde = 1
    for i in range( 2, n+1 ):
        waarde *= i
    return waarde

# Berekent n boven k; n en k zijn integer parameters;
# Retourneert n boven k als integer (want dat is het altijd).
def binomiaalcoefficient( n, k ):
    if k > n:
        return 0
    return int( faculteit( n ) /
        (faculteit( k )*faculteit( n - k )) )

def main():
    print( faculteit( 5 ) )
    print( binomiaalcoefficient( 8, 3 ) )

if __name__ == '__main__':
    main()
```

#### Antwoord 8.7

De code probeert de retourwaarde van de functie te printen, maar omdat
de functie geen retourwaarde heeft, wordt het woord `None` afgedrukt.
Als je een functie maakt waarvan je de output wilt tonen, kun je ofwel
de output in de functie printen en de functie aanroepen zonder de
retourwaarde te gebruiken, ofwel je laat de functie de waarde
retourneren en je print het in het hoofdprogramma. Niet allebei. Het
geniet meestal de voorkeur om functies niet zelf te laten printen, want
als ze een waarde retourneren maakt dat ze meer algemeen bruikbaar
(bijvoorbeeld, als de gegeven functie de waarde retourneert, kan de
oppervlakte van een driehoek vanaf dat moment elders in het programma in
berekeningen gebruikt worden). Als je deze uitleg niet begrijpt, lees
dan nogmaals hoofdstuk
6.

### Hoofdstuk 10

#### Antwoord 9.1

```python
def fib( n ):
    if n <= 2:
        return 1
    return fib( n-1 ) + fib( n-2 )

print( fib( 20 ) )
```

#### Antwoord 9.2

```python
def fib( n, depth ):
    indent = 6 * depth * " "
    print( "{}fib({})".format( indent, n ) )
    if n <= 2:
        print( "{}return {}".format( indent, 1 ) )
        return 1
    value = fib( n-1, depth+1 ) + fib( n-2, depth+1 )
    print( "{}return {}".format( indent, value ) )
    return value

print( fib( 5, 0 ) )
```

#### Antwoord 9.3

Aangezien de reeks van Fibonacci net zo goed als iteratieve functie
geïmplementeerd kan worden (dat heb je al in het vorige hoofdstuk
gedaan), is het geen goed idee om er een recursieve functie van te
maken. De redenen zijn dezelfde als voor de faculteit, wat in het
hoofdstuk is uitgelegd. Een bijkomende reden is dat de recursieve
definitie feitelijk alle termen van de sequentie meerdere keren
berekent, wat je kunt zien als je naar de output van de tweede opgave
kijkt, terwijl eenmalig berekenen voldoende kan zijn.

#### Antwoord 9.4

```python
def gcd( m, n ):
    if m % n == 0:
        return n
    return gcd( n, m%n )

print( gcd( 7*5*13, 2*3*7*11 ) )
```

De recursieve definitie spreekt over een kleinste en een grootste getal,
maar het grappige is dat je daar geen rekening mee hoeft te houden bij
het schrijven van de functie. Als je de functie aanroept met eerst de
kleinste en dan de grootste, dan betekent dat alleen maar dat de functie
een extra keer wordt aangeroepen. Verder geeft hij gewoon de juiste
uitkomst.

#### Antwoord 9.5

Het probleem met deze code is dat als ik een string ingeef met twee
foute tekens, dat het zichzelf twee keer recursief zal aanroepen,
namelijk voor ieder fout teken een keer. Bijvoorbeeld, als de gebruiker
`"route67"` ingeeft, volgt eerst een recursieve aanroep voor de `"6"`.
Als de gebruiker dan een correcte string ingeeft, zou de functie moeten
eindigen. Maar dat doet de functie niet. In plaats daarvan gaat de
functie door met het controleren van de originele string, komt de `"7"`
tegen, en roept dan zichzelf nogmaals aan voor weer een andere string.

Ik kan uitleggen hoe je dit probleem kunt oplossen door de code te
wijzigen, maar de echte oplossing is dat je geen recursieve functies
moet schrijven die interactie hebben met de gebruiker.

#### Antwoord 9.6

```python
GROOTTE = 4

def hanoi( p_van, p_tmp, p_naar, grootte ):
    if grootte == 1:
        print( "Schijf 1 van", p_van, "naar", p_naar )
        return 1
    stappen = hanoi( p_van, p_naar, p_tmp, grootte-1 )
    print( "Schijf", grootte, "van", p_van, "naar", p_naar )
    stappen += 1+hanoi( p_tmp, p_van, p_naar, grootte-1 )
    return stappen

stappen = hanoi( 'A', 'B', 'C', GROOTTE )
print( stappen, "stappen gedaan" )
```

Er is een iteratieve manier om deze puzzel op te lossen, namelijk de
volgende. Herhaal deze twee stappen totdat de puzzel is opgelost: (1)
Verplaats schijf 1 naar de volgende paal; (2) Verplaats een schijf die
*niet* schijf 1 is naar een andere paal (er is altijd precies één schijf
waarvoor dit kan). Het enige probleem dat overblijft is te bepalen of je
schijf 1 "met de klok mee" of "tegen de klok in" moet verplaatsen. Als
de grootte van de grootste schijf even is, moet je met de klok mee gaan
(van A naar B, van B naar C, of van C naar A), en anders tegen de klok
in (van A naar C, van C naar B, of van B naar A). Deze oplossing is snel
en vermijdt recursie, wat betekent dat hij bruikbaar is voor grotere
schijven dan de recursieve oplossing toestaat. Hij is echter complexer
om te implementeren omdat je iedere paal moet representeren als een list
(lists volgen in hoofdstuk
13),
en je moet een manier bedenken om te bepalen dat de puzzel is opgelost
(dat kan door simpelweg de stappen te tellen, dat wil zeggen, te tellen
tot $$2^N-1$$).

### Hoofdstuk 11

#### Antwoord 10.1

```python
text = """En Sint Atilla hief de handgranaat ten hemel, en
zeide, "O Here, zegen deze handgranaat, zodat daarmee u uw
vijanden tot kleine stukjes kunt blazen, in uwer genade."
En de Here grinnikte. En het volk laafde zich aan lammeren,
en luiaards, en karpers, en anchovis, en orang oetans, en
cornflakes, en fruitvliegjes, en grote stu..."""

tela, tele, teli, telo, telu = 0, 0, 0, 0, 0
for c in text:
    if c.upper() == "A":
        tela += 1
    elif c.upper() == "E":
        tele += 1
    elif c.upper() == "I":
        teli += 1
    elif c.upper() == "O":
        telo += 1
    elif c.upper() == "U":
        telu += 1

print( "tels: a={}, e={}, i={}, o={}, u={}".format(
    tela, tele, teli, telo, telu ) )
```

#### Antwoord 10.2

```python
tekst = """En ze stu[re]n [i]ngekleurde prentbriefkaarten van
plekken waarvan ze zich niet reali[s]eren dat ze er nooit
geweest zijn [a]an 'Iedereen op nummer 22, weer is prachti[g],
onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s]
vettig, maar we hebben een geweldig leuk restaurantje gevonden
in de achterstraatjes waar ze Heine[ke]n hebben en kaas en
uien chips en iemand die "Een beetje verliefd" speel[t] op een
a[c]cordeon' en je zit vier dagen vast op Schip[h]ol voor je
vijfdaagse vliegvakantie met niks anders te eten dan
uitgedroogde voorverpakte boterhammen..."""

start = -1
while True:
    start = tekst.find( "[", start+1 )
    if start < 0:
        break
    eind = tekst.find( "]", start )
    if eind < 0:
        break
    print( tekst[start+1:eind], end="" )
    start = eind
print()
```

#### Antwoord 10.3

```python
ch = "A"
while ch <= "Z":
    print( ch, end=" " )
    ch = chr( ord( ch )+1 )
print()

for i in range( 26 ):
    rotr13 = (i + 13)%26
    ch = chr( ord( "A" ) + rotr13 )
    print( ch, end=" " )
```

#### Antwoord 10.4

```python
tekst = """Kapper Knap, de knappe kapper, knipt en kapt heel
knap, maar de knecht van kapper Knap, de knappe kapper,
knipt en kapt nog knapper dan kapper Knap, de knappe kapper."""

def schoon( s ):
    ns = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            ns += c
        else:
            ns += " "
    return ns

tel = 0
for woord in schoon( tekst ).split():
    if woord == "knap":
        tel += 1

print( "Aantal keren dat het woord \"knap\" voorkomt:", tel )
```

#### Antwoord 10.5

```python
tekst = "Hello, world!"
ntekst = ""
while len( tekst ) > 0:
    i = 0
    ch = tekst[i]
    j = 1
    while j < len( tekst ):
        if tekst[j] < ch:
            ch = tekst[j]
            i = j
        j += 1
    tekst = tekst[:i] + tekst[i+1:]
    ntekst += ch
print( ntekst )
```

#### Antwoord 10.6

```python
from sys import exit

zin = "en zo gebeurde het dat dat onze toevallige ontmoeting \
met de EErwaarde aRTHUR BElling een ommekeer betekende in ons \
leven, en vanaf dat moment gingen we iedere zondag naar \
de kerk van Sint sIMPEL bij Roombroodje MEt Jam."

# Test of het echt wel een zin is
if len( zin  ) <= 0:
    exit()

# Eerste letter hoofdletter
nieuwezin = zin[0].upper() + zin[1:]

woordlijst = nieuwezin.split()
laatstewoord = ""
nieuwezin = ""

for w in woordlijst:

    # Dubbele hoofdletters correctie
    if len( w ) > 2 and w[0] >= "A" and w[0] <= "Z" and \
        w[1] >= "A" and w[1] <= "Z" and w[2] >= "a" and \
        w[2] <= "z":
        w = w[0] + w[1].lower() + w[2:]

    # Dagen met een hoofdletter
    dag = w.lower()
    if dag == "zondag" or dag == "maandag" or dag == "dinsdag" \
        or dag == "woensdag" or dag == "donderdag" or \
        dag == "vrijdag" or dag == "zaterdag":
        w = dag[0].upper() + dag[1:]

    # CAPS LOCK correctie
    if w[0] >= "a" and w[0] <= "z":
        hoofdletters = True
        for c in w[1:]:
            if not (c >= "A" and c <= "Z"):
                hoofdletters = False
                break
        if hoofdletters:
            w = w[0].upper() + w[1:].lower()

    # Duplicaten verwijderen
    if w == laatstewoord:
        continue

    nieuwezin += w + " "
    laatstewoord = w

nieuwezin = nieuwezin.strip()
print( nieuwezin )
```

### Hoofdstuk 12

#### Antwoord 11.1

De functie `toon_complex()` heb ik gemaakt om complexe getallen op een
nette manier te tonen, en dat neemt de meeste code in beslag. Ik had
niet gevraagd of je zo'n functie zou willen maken, en het is ook niet
nodig.

```python
def plus_complex( c1, c2 ):
    return (c1[0] + c2[0], c1[1] + c2[1])

def toon_complex( c ):
    s = "("
    if c[1] == 0:
        return str( c[0] )
    elif c[0] != 0:
        s += str( c[0] )
        if c[1] > 0:
            s += "+"
    if c[1] != 1:
        if c[1] == -1:
            s += "-"
        else:
            s += str( c[1] )
    s += "i)"
    return s

num1 = (2,1)
num2 = (0,2)
print( toon_complex( num1 ), "+", toon_complex( num2 ), "=",
     toon_complex( plus_complex( num1, num2 ) ) )
```

#### Antwoord 11.2

Voor deze oplossing heb ik een minimalistische versie van
`toon_complex()` gebruikt.

```python
def maal_complex( c1, c2 ):
    return (c1[0]*c2[0] - c2[1]*c1[1], c1[0]*c2[1] + c1[1]*c2[0])

def toon_complex( c ):
    return "({},{}i)".format( c[0], c[1] )

num1 = (2,1)
num2 = (0,2)
print( toon_complex( num1 ), "*", toon_complex( num2 ), "=",
     toon_complex( maal_complex( num1, num2 ) ) )
```

#### Antwoord 11.3

```python
inttuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12,
    13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )

def toon_inttuple( it ):
    for element in it:
        if isinstance( element, int ):
            print( element, end=" ")
        else:
            toon_inttuple( element )

toon_inttuple( inttuple )
```

### Hoofdstuk 13

#### Antwoord 12.1

```python
from random import choice

antwoord = [ "Dat is zeker", "Het is zeker zo", "Zonder twijfel",
"Ja, zeker", "Je kunt erop vertrouwen", "Zoals ik het zie, ja",
"Waarschijnlijk", "Ziet er goed uit", "Ja", "Lijkt van wel",
"Vaag, probeer het nog eens", "Vraag later nog eens", "Kan ik \
beter niet zeggen", "Kan ik nu niet voorspellen", "Concentreer \
je en vraag nog eens", "Reken er maar niet op", "Ik zeg van \
niet", "Mijn bronnen zeggen van niet", "Lijkt er niet op",
"Zeer twijfelachtig" ]

input( "Stel je vraag aan de magische bol: " )
print( "De magische bol zegt:", choice( antwoord ) )
```

De `choice()` functie uit de `random` module selecteert een element van
een list per toeval. Je kunt ook `randint()` gebruiken, waarbij je een
index per toeval selecteert.

#### Antwoord 12.2

```python
from random import randint

stok = []
for value in ("Aas", "2", "3", "4", "5", "6", "7", "8",
    "10", "Boer", "Vrouw", "Heer"):
    for kleur in ("Harten", "Schoppen", "Klaveren", "Ruiten"):
        stok.append( kleur + ' ' + value )

for i in range( len( stok ) ):
    j = randint( i, len( stok )-1 )
    stok[i], stok[j] = stok[j], stok[i]

for kaart in stok:
    print( kaart )
```

#### Antwoord 12.3

```python
fifo = []
while True:
    k = input( "> " )
    if k == "":
        break
    if k != "?":
        fifo.append( k )
    elif len( fifo ) > 0:
        print( fifo.pop(0) )
    else:
        print( "Lijst is leeg" )
```

#### Antwoord 12.4

```python
tekst = """Let op, het is heel eenvoudig om je te verdedigen
tegen een man die gewapend is met een banaan. Eerst dwing je
hem de banaan te laten vallen; dan ontwapen je hem door de
banaan op te eten. Dat maakt hem onschadelijk."""

def tel_letter( x ):
    return x[0], -ord(x[1])

tellist = []
for i in range( 26 ):
    tellist.append( [0, chr(ord("a")+i)] )

for letter in tekst.lower():
    if letter >= "a" and letter <= "z":
        tellist[ord(letter)-ord("a")][0] += 1

tellist.sort( reverse=True, key=tel_letter )

for tel in tellist:
    print( "{:3}: {}".format( tel[0],tel[1] ) )
```

#### Antwoord 12.5

Er zijn twee manieren om dit probleem aan te pakken: ofwel je begint met
een list met nummers, of je begint met een list met booleans en je
beschouwt de index van een boolean als nummer. In de oplossing hier
direct onder gebruik ik de methode met booleans. Ik laat de list met nul
starten, omdat dat een hoop aftrekkingen scheelt, terwijl het slechts
één boolean meer dan nodig in het geheugen plaatst. De methode is erg
snel omdat ik met indices kan werken.

```python
nummers = 101 * [True]
nummers[1] = False
for i in range( 1, len( nummers ) ):
    if not nummers[i]:
        continue
    print( i, end=" " )
    j = 2
    while j*i < len( nummers ):
        nummers[j*i] = False
        j += 1
```

Hier is de alternatieve oplossingsmethode, waarbij ik de functie
`range()` gebruik om de list te bouwen. Ik verwijder items van de list
wanneer ik weet dat ze niet priem zijn. Omdat er erg veel list
manipulaties nodig zijn, is deze methode iets trager dan de vorige, maar
de snelheid neemt toe naarmate er meer en meer getallen van de list
verwijderd worden.

```python
MAXNUM = 100
nummers = list( range(2,MAXNUM+1) )
i = 0
while i < len( nummers ):
    j = i+1
    while j < len( nummers ):
        if nummers[j]%nummers[i]:
            j += 1
        else:
            nummers.pop(j)
    i += 1
for i in nummers:
    print( i, end=" " )
```

#### Antwoord 12.6

```python
from pcinput import getInteger

LEEG = "-"
SPELERX = "X"
SPELERO = "O"
MAXZET = 9

def toon_bord( b ):
    print( "  1 2 3" )
    for rij in range( 3 ):
        print( rij+1, end=" ")
        for kol in range( 3 ):
            print( b[rij][kol], end=" " )
        print()

def opponent( p ):
    if p == SPELERX:
        return SPELERO
    return SPELERX

def neemRowKolom( speler, wat ):
    while True:
        num = getInteger( "Speler "+speler+", welke "+wat+
            " kies je? " )
        if num < 1 or num > 3:
            print( "Geef 1, 2, of 3" )
            continue
        return num

def winnaar( b ):
    for rij in range( 3 ):
        if b[rij][0] != LEEG and b[rij][0] == b[rij][1] \
            and b[rij][0] == b[rij][2]:
            return True
    for kol in range( 3 ):
        if b[0][kol] != LEEG and b[0][kol] == b[1][kol] \
            and b[0][kol] == b[2][kol]:
            return True
    if b[1][1] != LEEG:
        if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
            return True
        if b[1][1] == b[0][2] and b[1][1] == b[2][0]:
            return True
    return False

bord = [[LEEG,LEEG,LEEG],[LEEG,LEEG,LEEG],[LEEG,LEEG,LEEG]]
speler = SPELERX

toon_bord( bord )
zet = 0
while True:
    rij = neemRowKolom( speler, "rij" )
    kol = neemRowKolom( speler, "kolom" )
    if bord[rij-1][kol-1] != LEEG:
        print( "Rij", rij, "en kolom", kol, "is niet leeg" )
        continue
    bord[rij-1][kol-1] = speler
    toon_bord( bord )
    if winnaar( bord ):
        print( "Speler", speler, "wint!" )
        break
    zet += 1
    if zet == MAXZET:
        print( "Het is gelijkspel." )
        break
    speler = opponent( speler )
```

#### Antwoord 12.7

```python
from pcinput import getString
from random import randint

LEEG = "."
SCHIP = "X"
SCHEPEN = 3
BREEDTE = 4
HOOGTE = 3

def toonBord( b ):
    print( "  ", end="" )
    for kol in range( BREEDTE ):
        print( chr( ord("A")+kol ), end=" " )
    print()
    for rij in range( HOOGTE ):
        print( rij+1, end=" ")
        for kol in range( BREEDTE ):
            print( b[rij][kol], end=" " )
        print()

def plaatsSchepen( b ):
    for i in range( SCHEPEN ):
        while True:
            x = randint( 0, BREEDTE-1 )
            y = randint( 0, HOOGTE-1 )
            if b[y][x] == SCHIP:
                continue
            if x > 0 and b[y][x-1] == SCHIP:
                continue
            if x < BREEDTE-1 and b[y][x+1] == SCHIP:
                continue
            if y > 0 and b[y-1][x] == SCHIP:
                continue
            if y < HOOGTE-1 and b[y+1][x] == SCHIP:
                continue
            break
        b[y][x] = SCHIP

def neemDoel():
    while True:
        cel = getString( "Welke cel kies je? " ).upper()
        if len( cel ) != 2:
            print( "Geef een cel in als XY,",
                "met X een letter en Y een cijfer" )
            continue
        if cel[0] not in "ABCD":
            print( "De letter moet tussen A en",
                chr( ord("A")+BREEDTE-1 ), "liggen" )
            continue
        if cel[1] not in "123":
            print( "Cijfer moet tussen 1 en", HOOGTE, "liggen" )
            continue
        return ord(cel[0])-ord("A"), ord(cel[1])-ord("1")

bord = []
for i in range( HOOGTE ):
    rij = BREEDTE * [LEEG]
    bord.append( rij )
plaatsSchepen( bord )
toonBord( bord )

raak = 0
zetten = 0
while raak < SCHEPEN:
    x, y = neemDoel()
    if bord[y][x] == SCHIP:
        print( "Raak!" )
        bord[y][x] = LEEG
        raak += 1
    else:
        print( "Mis!" )
    zetten += 1

print( "Je had", zetten, "zetten nodig om mij te verslaan." )
```

#### Antwoord 12.8

```python
# Recursieve functie die bepaalt of intlist (integer-list) een
# subset heeft die optelt tot totaal. Het retourneert de
# subset, of een lege list als er geen subset is die werkt.
def subset_telt_op_tot( intlist, totaal ):
    for num in intlist:
        if num == totaal:
            return [num]
        nlist = intlist[:]
        nlist.remove( num )
        retlist = subset_telt_op_tot( nlist, totaal-num )
        if len( retlist ) > 0:
            retlist.insert( 0, num )
            return( retlist )
    return []

numlist = [ 3, 8, -1, 4, -5, 6 ]
oplossing = subset_telt_op_tot( numlist, 0 )
if len( oplossing ) <= 0:
    print( "Geen subset telt op tot nul" )
else:
    for i in range( len( oplossing ) ):
        if oplossing[i] < 0 or i == 0:
            print( oplossing[i], end="" )
        else:
            print( "+{}".format( oplossing[i] ), end="" )
    print( "=0" )
```

De recursieve functie doorloopt alle getallen in `intlist`. Als het
huidige getal gelijk is aan `totaal`, dan is een oplossing gevonden en
wordt een list geretourneerd met daarin alleen het huidige nummer.
Anders roept het zichzelf aan met een kopie van de list, waarbij het
huidige nummer verwijderd is, met een totaal waarvan het huidige nummer
is afgetrokken (bijvoorbeeld, als het huidige nummer 3 is en het totaal
is 5, dan wordt 3 van de list verwijderd en wordt gecontroleerd of met
de nieuwe list een totaal van 2 bereikt kan worden; immers, dan kan 5
bereikt worden door 3 op te tellen bij de deelverzameling die optelt tot
2). Als de recursieve aanroep een niet-lege list teruggeeft, dan is een
oplossing gevonden, en wordt het huidige nummer aan de retourlist
toegevoegd, en de retourlist geretourneerd. Anders wordt een lege list
geretourneerd als alle nummers gecontroleerd zijn.

Merk op: De oplossing voor dit probleem test alle mogelijke
deelverzamelingen totdat een oplossing is gevonden of alle
deelverzamelingen getest zijn. Je vraagt je misschien af of dit slimmer
kan, gezien het feit dat het aantal deelverzamelingen exponentieel
toeneemt met de grootte van de list. Het antwoord is dat er oplossingen
kunnen zijn die een verbetering zijn op de huidige oplossing
(bijvoorbeeld, als ik er rekening mee houd dat een getal meermalen op de
list kan voorkomen dan kan ik sommige deelverzamelingen uitsluiten omdat
ze equivalent zijn met andere), maar dat over het algemeen geldt dat
voor een willekeurige list van getallen, er geen algoritme bekend is dat
het probleem oplost zonder alle deelverzamelingen te testen als er geen
oplossing is. Voor degenen die iets weten van complexiteitstheorie: het
subset som probleem is "NP-hard."

### Hoofdstuk 14

#### Antwoord 13.1

```python
tekst = """Kapper Knap, de knappe kapper, knipt en kapt heel
knap, maar de knecht van kapper Knap, de knappe kapper, knipt
en kapt nog knapper dan kapper Knap, de knappe kapper."""

def schoon( s ):
    ns = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            ns += c
        else:
            ns += " "
    return ns

wdict = {}
for woord in schoon( tekst ).split():
    wdict[woord] = wdict.get( woord, 0 ) + 1

keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )
```

#### Antwoord 13.2

```python
movies = {  "Monty Python and the Holy Grail":
            [ 9, 10, 9.5, 8.5, 3, 7.5,8 ],
            "Monty Python's Life of Brian":
            [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ],
            "Monty Python's Meaning of Life":
            [ 7, 6, 5 ],
            "And Now For Something Completely Different":
            [ 6, 5, 6, 6 ] }

keylist = list( movies.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, round(
        sum( movies[key] )/len( movies[key] ), 1 ) ) )
```

#### Antwoord 13.3

Veel verschillende antwoorden zijn mogelijk. Het eenvoudigste antwoord
is waarschijnlijk om een dictionary te gebruiken waarvan de keys tuples
zijn, die de schrijvers' achter- en voornamen bevatten. De waarde bij
een key is een list, die de boeken van de corresponderende schrijver
bevat. Een boek is een tuple bestaande uit een titel en een locatie. Om
alle boeken van een schrijver uit te lijsten, kun je de list met boeken
zoeken met de schrijver's naam. Om de locatie van een specifiek boek te
vinden, zoek je op dezelfde manier de list met boeken van de schrijver,
en zoekt dan in de list naar het juiste boek om de locatie vast te
stellen. Je zou in plaats van een list van boeken ook een dictionary
kunnen bouwen met de boek titel als key en de locatie als waarde, maar
schrijvers produceren over het algemeen niet zoveel boeken dat dat nodig
is. Het is natuurlijk zowiezo geen geweldig idee om namen en titels als
keys te gebruiken, omdat ze lang zijn en het gemakkelijk is spelfouten
te maken. Maar dit waren de enige identificerende elementen die ik
noemde. Ik zal er echter niet over klagen als je gemakkelijke en minder
dubbelzinnige keys introduceert in de data structuur (maar over het
algemeen geldt dat je beter een database systeem kunt gebruiken om een
bibliotheek in op te slaan).

### Hoofdstuk 15

#### Antwoord 14.1

```python
alles = { "Socrates", "Plato", "Eratosthenes", "Zeus", "Hera",
    "Athene", "Acropolis", "Kat", "Hond" }
mensen = { "Socrates", "Plato", "Eratosthenes" }
sterfelijken = { "Socrates", "Plato", "Eratosthenes", "Kat",
    "Hond" }

print( mensen.issubset( sterfelijken ) ) # (a)
print( "Socrates" in mensen ) # (b)
print( "Socrates" in sterfelijken ) # (c)
print( len( sterfelijken.difference( mensen ) ) > 0 ) # (d)
print( len( alles.difference( sterfelijken ) ) > 0 ) # (e)
```

#### Antwoord 14.2

```python
set3 = set( [3*x for x in range( 1, int( 1001/3 ) )] )
set7 = set( [7*x for x in range( 1, int( 1001/7 ) )] )
set11 = set( [11*x for x in range( 1, int( 1001/11 ) )] )

seta = set3 & set7 & set11
setb = (set3 & set7) - set11
setc = set( range( 1, 1001 ) ) - set3 - set7 - set11
```

Je kunt de sets afdrukken om te zien dat ze correct zijn.

### Hoofdstuk 16

#### Antwoord 15.1

```python
from os import listdir, getcwd

flist = listdir( "." )
for name in flist:
    print( getcwd() + "/" + name )
```

### Hoofdstuk 17

#### Antwoord 16.1

Hopelijk herinnerde je je dat je iets soortgelijks hebt gedaan in
hoofdstukken
11
en
14.
De code hieronder is voor het grootste deel een kopie van de code die je
eerder geschreven hebt. Het enige verschil met de code die je schreef in
hoofdstuk
14
is dat de tekst niet aangeleverd is als een string, maar gelezen wordt
uit een bestand.

```python
def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

fp = open( "pc_woodchuck.txt" )
tekst = fp.read()
fp.close()

wdict = {}
for woord in schoon( tekst ).split():
    wdict[woord] = wdict.get( woord, 0 ) + 1

keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )
```

#### Antwoord 16.2

```python
def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

wdict = {}
fp = open( "pc_woodchuck.txt" )
while True:
    regel = fp.readline()
    if regel == "":
        break
    for woord in schoon( regel ).split():
        wdict[woord] = wdict.get( woord, 0 ) + 1
fp.close()

keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )
```

#### Antwoord 16.3

```python
from os.path import join
from os import getcwd

def verwijderklinkers( regel ):
    nieuweregel = ""
    for c in regel:
        if c not in "aeiouAEIOU":
            nieuweregel += c
    return nieuweregel

inputnaam = join( getcwd(), "pc_woodchuck.txt" )
outputnaam = join( getcwd(), "pc_woodchuck.tmp" )

fpi = open( inputnaam )
fpo = open( outputnaam, "w" )

telread = 0
telwrite = 0

while True:
    regel = fpi.readline()
    if regel == "":
        break
    telread += len( regel )
    regel = verwijderklinkers( regel )
    fpo.write( regel )
    telwrite += len( regel )

fpo.close()
fpi.close()

print( "Gelezen:", telread )
print( "Geschreven:", telwrite )
```

#### Antwoord 16.4

De oplossing die ik hieronder geef maakt gebruik van sets. Er wordt een
set gebouwd voor ieder bestand, dat alle woorden bevat uit het bestand
die 3 of meer letters hebben. Je kunt de lengte van de gezochte woorden
veranderen door `LEN` aan te passen. Om het programma flexibel te maken,
heb ik het niet gelimiteerd tot slechts drie bestanden en sets, maar
gebruik ik zoveel sets als er namen in de list van bestanden zijn. Het
programma neemt de doorsnede van de sets om de oplossing te bepalen.

```python
from os.path import join
from os import getcwd

LEN = 3

def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

lijst = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
setlist = []

for naam in lijst:
    bestandnaam = join( getcwd(), naam )
    woordset = set()
    setlist.append( woordset )
    fp = open( bestandnaam )
    while True:
        regel = fp.readline()
        if regel == "":
            break
        woordlist = schoon( regel ).split()
        for woord in woordlist:
            if len( woord ) >= LEN:
                woordset.add( woord )
    fp.close()

combinatie = setlist[0].copy()
i = 1
while i < len( setlist ):
    combinatie = combinatie & setlist[i]
    i += 1

for woord in combinatie:
    print( woord )
```

#### Antwoord 16.5

Wederom heb ik een oplossing gekozen die flexibel is wat betreft het
aantal bestanden dat verwerkt wordt. Het programma is gemakkelijker te
schrijven als je ervan uit gaat dat er slechts drie bestanden zijn, en
niet meer. Als je een dergelijke oplossing gekozen hebt is dat prima
(zolang het programma verder de juiste uitvoer geeft), aangezien het
werken met een variabel aantal bestanden meer een oefening is voor het
hoofdstuk over iteraties. Maar op dit moment zou je gewend moeten zijn
aan het gebruik van iteraties, dus probeer ze toe te passen als dat
leidt tot een superieure oplossing.

```python
from os.path import join
from os import getcwd

lijst = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
letterlist = [ len( lijst )*[0] for i in range( 26 ) ]
totaallist = len( lijst ) * [0]

# Verwerk de invoerlijst regel voor regel, maak kleine letters
# en tel de letters in letterlist, en houd totaaltellingen
# bij in totaallist.
aantal = 0
for naam in lijst:
    bestandnaam = join( getcwd(), naam )
    fp = open( bestandnaam )
    while True:
        regel = fp.readline()
        if regel == "":
            break
        regel = regel.lower()
        for c in regel:
            if c >= 'a' and c <= 'z':
                totaallist[aantal] += 1
                letterlist[ord(c)-ord("a")][aantal] += 1
    fp.close()
    aantal += 1

# Schrijf tellingen in CSV formaat.
uitvoerbestand = join( getcwd(), "pc_writetest.csv" )
fp = open( uitvoerbestand, "w" )
for i in range( len( letterlist ) ):
    s = "\"{}\"".format( chr( ord("a")+i ) )
    for j in range( len( lijst ) ):
        s += ",{:.5f}".format( letterlist[i][j]/totaallist[j] )
    fp.write( s+"\n" )
fp.close()

# Laat de inhoud van de CSV zien ter controle.
fp = open( uitvoerbestand )
print( fp.read() )
fp.close()
```

### Hoofdstuk 18

#### Antwoord 17.1

De code kan een `ValueError` genereren als je iets ingeeft dat geen
integer is, een `IndexError` als je een index ingeeft buiten het bereik
`{-5,4}`, een `ZeroDivisionError` als je index 2 ingeeft, en een
`TypeError` als je index 3 ingeeft. De code hieronder doet een simpele
afhandeling door een foutmelding te geven, maar je kunt ook een loop
bouwen om de code zodat de gebruiker om een nieuwe invoer wordt
gevraagd.

```python
numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Geef een index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "Je gaf geen geheel getal" )
except IndexError:
    print( "De index moet tussen -5 en 4 liggen" )
except ZeroDivisionError:
    print( "Het lijkt erop dat de list een 0 bevat" )
except TypeError:
    print( "Het lijkt erop er een niet-numeriek element is" )
except:
    print( "Iets onverwachts is gebeurd" )
    raise
```

### Hoofdstuk 19

#### Antwoord 18.1

Ik gebruik een kopie van "pc_rose.txt" die ik "pc_rose_copy.txt"
noem.

```python
NAAM = "pc_rose_copy.txt"

def toon_inhoud( filename ):
    fp = open( filename, "rb" )
    print( fp.read() )
    fp.close()

def encryptie( filename ):
    fp = open( filename, "r+b" )
    buffer = fp.read()
    fp.seek(0)
    for c in buffer:
        if c >= 128:
            fp.write( bytes( [c-128] ) )
        else:
            fp.write( bytes( [c+128] ) )
    fp.close()

toon_inhoud( NAAM )
encryptie( NAAM )
toon_inhoud( NAAM )
```

#### Antwoord 18.2

```python
letters = "etaoinshrdlcum "
ongecodeerd = "Hello, world!"

# Toon de string zonder codering, ter controle
print( ongecodeerd, len( ongecodeerd ) )

# Creeer een half-byte-list als basis voor codering
halfbytelist = []
for c in ongecodeerd:
    if c in letters:
        halfbytelist.append( letters.index( c )+1 )
    else:
        byte = ord( c )
        halfbytelist.extend( [0, int( byte/16 ), byte%16 ] )
if len( halfbytelist )%2 != 0:
    halfbytelist.append( 0 )

# Maak van de half-byte-list een bytelist.
bytelist = []
for i in range( 0, len( halfbytelist ), 2 ):
    bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )

# Maak van de bytelist een bytestring en toon die ter controle.
gecodeerd = bytes( bytelist )
print( gecodeerd, len( gecodeerd ) )
```

Dit programma is 25 regels, waarvan 4 commentaar, 4 leeg, en 3 slechts
voor testdoeleinden zijn. Dit kan dus met 14 regels code. Dat was niet
al te erg, toch?

#### Antwoord 18.3

```python
letters = "etaoinshrdlcum "
gecodeerd = b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'

# Toon de gecodeerde byte string ter controle.
print( gecodeerd, len( gecodeerd ) )

# Creeer een half-byte-list op basis van de byte string.
halfbytelist = []
for c in gecodeerd:
    halfbytelist.extend( [ int( c/16 ), c%16 ] )
if halfbytelist[-1] == 0:
    del halfbytelist[-1]

# Maak van de half-byte-string een string.
gedecodeerd = ""
while len( halfbytelist ) > 0:
    num = halfbytelist.pop(0)
    if num > 0:
        gedecodeerd += letters[num-1]
        continue
    num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
    gedecodeerd += chr( num )

# Toon de string, ter controle.
print( gedecodeerd, len( gedecodeerd ) )
```

#### Antwoord 18.4

Dit programa lijkt lang, maar is eenvoudig. `comprimeer()` en
`decomprimeer()` werden eerder gebouwd. Ik heb alleen de invoer en
uitvoer in byte strings gewijzigd. De rest bestaat vooral uit het
afhandelen van mogelijke fouten die kunnen optreden bij
bestandsmanipulatie. De basis-functionaliteit van een programma kun je
vaak in een paar regels schrijven, terwijl foutafhandeling drie keer zo
lang is.

```python
from pcinput import getString, getLetter
from os.path import exists, getsize

LETTERS = b"etaoinshrdlcum "

# Comprimeer byte string ongecodeerd, retourneer gecomprimeerd
def comprimeer( ongecodeerd ):
    halfbytelist = []
    for c in ongecodeerd:
        if c in LETTERS:
            halfbytelist.append( LETTERS.index( c )+1 )
        else:
            halfbytelist.extend( [0, int( c/16 ), c%16 ] )
    if len( halfbytelist )%2 != 0:
        halfbytelist.append( 0 )
    bytelist = []
    for i in range( 0, len( halfbytelist ), 2 ):
        bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )
    return bytes( bytelist )

# Decomprimeer byte string gecodeerd, retourneer gedecomprimeerd
def decomprimeer( gecodeerd ):
    halfbytelist = []
    for c in gecodeerd:
        halfbytelist.extend( [ int( c/16 ), c%16 ] )
    if halfbytelist[-1] == 0:
        del halfbytelist[-1]
    bytelist = []
    while len( halfbytelist ) > 0:
        num = halfbytelist.pop(0)
        if num > 0:
            bytelist.append( LETTERS[num-1] )
            continue
        num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
        bytelist.append( num )
    return bytes( bytelist )

# Vraag om input bestand en lees de inhoud
while True:
    filein = getString( "Geef input bestand: " )
    if not exists( filein ):
        print( filein, "bestaat niet" )
        continue
    try:
        fp = open( filein, "rb" )
        buffer = fp.read()
        fp.close()
    except IOError as ex:
        print( filein, "kan niet verwerkt worden, kies andere" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Vraag om output bestand en creeer het
while True:
    fileout = getString( "Geef output bestand: " )
    if exists( fileout ):
        print( fileout, "bestaat al" )
        continue
    try:
        fp = open( fileout, "wb" )
    except IOError as ex:
        print( fileout, "kan niet aangemaakt worden,",
            "kies een andere naam" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Vraag of de gebruiker wil comprimeren of decomprimeren.
while True:
    dc = getLetter( "Wil je (C)omprimeren of (D)ecomprimeren? " )
    if dc != 'C' and dc != 'D':
        print( "Kies C of D" )
        continue
    break

# Comprimeer of decomprimeer de buffer.
if dc == 'C':
    buffer = comprimeer( buffer )
else:
    buffer = decomprimeer( buffer )

# Sla de verwerkte buffer op in het output bestand.
try:
    fp.write( buffer )
    fp.close()
except IOError as ex:
    print( "Het schrijven lukte niet" )
    print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))

# Rapporteer de groottes van input en output.
print( getsize( filein ), "bytes gelezen" )
print( getsize( fileout ), "bytes geschreven" )
```

### Hoofdstuk 20

#### Antwoord 19.1

```python
s = "Hello, world!"
mask = (1<<5) | (1<<3) | (1<<1)    # 00101010

codering = ""
for c in s:
    codering += chr(ord(c)^mask)
print( codering )

decodering = ""
for c in codering:
    decodering += chr(ord(c)^mask)
print( decodering )
```

#### Antwoord 19.2

```python
def setBit( opslag, index, value ):
    masker = 1<<index
    if value:
        opslag |= masker
    else:
        opslag &= ~masker
    return opslag

# getBit() retourneert 0 als de bit behorende bij de index op 1
# staat, en anders retourneert het iets anders. Omdat alleen 0
# als False wordt beschouwd, kun je deze functie gebruiken om de
# waarde van een bit te testen.
def getBit( opslag, index ):
    masker = 1<<index
    return opslag & masker

def toonBits( opslag ):
    for i in range( 8 ):
        index = 7 - i
        if getBit( opslag, index ):
            print( "1", end="" )
        else:
            print( "0", end="" )
    print()

opslag = 0
opslag = setBit( opslag, 0, True )
opslag = setBit( opslag, 1, True )
opslag = setBit( opslag, 2, False )
opslag = setBit( opslag, 3, True )
opslag = setBit( opslag, 4, False )
opslag = setBit( opslag, 5, True )
toonBits( opslag )

opslag = setBit( opslag, 1, False )
toonBits( opslag )
```

### Hoofdstuk 21

#### Antwoord 20.1

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
        self.breedte = abs( breedte )
        self.hoogte = abs( hoogte )
        if self.breedte == 0:
            self.breedte = 1
        if self.hoogte == 0:
            self.hoogte = 1
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.punt,
            self.breedte, self.hoogte )
    def oppervlakte( self ):
        return self.breedte * self.hoogte
    def omtrek( self ):
        return 2*(self.breedte + self.hoogte)
    def rechtsonder( self ):
        return Punt( self.punt.x + self.breedte,
            self.punt.y + self.hoogte )
    def overlap( self, r ):
        r1, r2 = self, r
        if self.punt.x > r.punt.x or \
            (self.punt.x == r.punt.x and \
            self.punt.y > r.punt.y):
            r1, r2 = r, self
        if r1.rechtsonder().x <= r2.punt.x or \
            r1.rechtsonder().y <= r2.punt.y:
            return None
        return Rechthoek( r2.punt,
            min( r1.rechtsonder().x - r2.punt.x, r2.breedte ),
            min( r1.rechtsonder().y - r2.punt.y, r2.hoogte ) )

r1 = Rechthoek( Punt( 1, 1 ), 8, 5 )
r2 = Rechthoek( Punt( 2, 3 ), 9, 2 )

print( r1.oppervlakte() )
print( r1.omtrek() )
print( r1.rechtsonder() )
r = r1.overlap( r2 )
if r:
    print( r )
else:
    print( "De rechthoeken overlappen niet" )
```

#### Antwoord 20.2

Vanwege de lijst die je moet tonen, kun je het beste de methode
`inschrijven()` in de student plaatsen. Voor de geboortedatum gebruik ik
de `datetime` module; omdat je de leeftijd van de student moet
berekenen, heb je ook de dag van vandaag nodig, waarvoor je een functie
in de `datetime` module vindt.

```python
from datetime import date
from random import random

class Cursus:
    def __init__( self, naam, nummer ):
        self.naam = naam
        self.nummer = nummer
    def __repr__( self ):
        return "{}: {}".format( self.nummer, self.naam )

class Student:
    def __init__( self, achternaam, voornaam, geb_datum, anr):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.geboortedatum = geb_datum
        self.anr = anr
        self.cursussen = []
    def __str__( self ):
        return self.voornaam+" "+self.achternaam
    def age( self ):
        vandaag = date.today()
        jaren = vandaag.year - self.geboortedatum.year
        if vandaag.month < self.geboortedatum.month or \
            (vandaag.month == self.geboortedatum.month \
            and vandaag.day < self.geboortedatum.day):
            jaren -= 1
        return jaren
    def inschrijven( self, cursus ):
        if cursus not in self.cursussen:
            self.cursussen.append( cursus )

studenten = [
    Student( "Alikruik", "Adrie", date( 1989, 10, 3 ), 453211 ),
    Student( "Bonzo", "Beatrijs", date( 1991, 12, 29 ), 476239 ),
    Student( "Continuum", "Carola", date( 1992, 3, 7 ), 784322 ),
    Student( "Domoor", "Dirk", date( 1993, 7, 11 ), 995544 ) ]
cursussen =[
    Cursus( "Vinologie", 787656 ),
    Cursus( "Lepelbuigen voor gevorderden", 651121 ),
    Cursus( "Onderzoeksvaardigheden: Babbelen", 433231 )]

for student in studenten:
    for cursus in cursussen:
        if random() > 0.3:
            student.inschrijven( cursus )

for student in studenten:
    print( "{}: {} {} ({})".format( student.anr,
        student.voornaam, student.achternaam, student.age() ) )
    if len( student.cursussen ) == 0:
        print( "\tNo cursussen" )
    for cursus in student.cursussen:
        print( "\t{}".format( cursus ) )
```

### Hoofdstuk 22

#### Antwoord 21.1

```python
KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur # index in KLEUR list
        self.rang = rang # index in RANG list
    def __repr__( self ):
        return "({},{})".format( self.kleur, self.rang )
    def __str__( self ):
        return "{} {}".format(KLEUR[self.kleur],RANG[self.rang])
    def __eq__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang == c.rang
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang > c.rang
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang >= c.rang
        return NotImplemented

k5 = Kaart( 2, 3 )
r5 = Kaart( 3, 3 )
sh = Kaart( 1, 11 )
print( "{}, {}, {}".format( k5, r5, sh ) )
print( k5 == r5 )
print( k5 == sh )
print( k5 > sh )
print( k5 >= sh )
print( k5 < sh )
print( k5 <= sh )
```

{:class="callout callout-info"}
> #### Opmerking
> Je hoeft de `__ne__()`, `__lt__()`, en `__le__()` niet te
> implementeren, aangezien die automatisch worden gewijzigd in aanroepen
> van andere methodes die je implementeert.

#### Antwoord 21.2

Om de leesbaarheid te vergroten heb ik de methodes die niet nodig zijn
uit `Kaart` verwijderd voor dit programma.

```python
KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur
        self.rang = rang
    def __str__( self ):
        return "{} {}".format(KLEUR[self.kleur],RANG[self.rang])

class Trekstapel:
    def __init__( self, stapel=[] ):
        self.stapel = stapel
    def __len__( self ):
        return len( self.stapel )
    def __getitem__( self, n ):
        return self.stapel[n]
    def voegtoe( self, c ):
        self.stapel.append( c )
    def trek( self ):
        if len( self ) <= 0:
            return None
        return self.stapel.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.stapel:
            s += sep + str( c )
            sep = ", "
        return s

ts1 = Trekstapel( [Kaart(0,1),Kaart(0,5),Kaart(2,4),Kaart(1,12)])
print( ts1 )
print( ts1[1] )
ts1.voegtoe( Kaart(3,12) )
print( ts1 )
print( ts1.trek() )
print( ts1 )
```

#### Antwoord 21.3

```python
KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur
        self.rang = rang
    def __repr__( self ):
        return "({},{})".format( self.kleur, self.rang )
    def __str__( self ):
        return "{} {}".format(KLEUR[self.kleur],RANG[self.rang])
    def __eq__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang == c.rang
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang > c.rang
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang >= c.rang
        return NotImplemented

class Trekstapel:
    def __init__( self, stapel=[] ):
        self.stapel = stapel
    def __len__( self ):
        return len( self.stapel )
    def __getitem__( self, n ):
        return self.stapel[n]
    def voegtoe( self, c ):
        self.stapel.append( c )
    def trek( self ):
        if len( self ) <= 0:
            return None
        return self.stapel.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.stapel:
            s += sep + str( c )
            sep = ", "
        return s

ts1 = Trekstapel( [Kaart(3,0), Kaart(0,11), Kaart(2,5)] )
ts2 = Trekstapel( [Kaart(3,2), Kaart(3,1), Kaart(1,6)] )

i = 1
while len( ts1 ) > 0 and len( ts2 ) > 0:
    print( "Ronde", i )
    print( "Stapel1:", ts1 )
    print( "Stapel2:", ts2 )
    c1 = ts1.trek()
    c2 = ts2.trek()
    if c1 > c2:
        ts1.voegtoe( c1 )
        ts1.voegtoe( c2 )
    else:
        ts2.voegtoe( c2 )
        ts2.voegtoe( c1 )
    i += 1

print( "Het spel is uit" )
if len( ts1 ) > 0:
    print( "Stapel1:", ts1 )
    print( "De eerste stapel wint!" )
else:
    print( "Stapel2:", ts2 )
    print( "De tweede stapel wint!" )
```

#### Antwoord 21.4

Vergeet niet dat je in de `__add__()` en `__sub__()` methodes (diepe)
kopieën moet creëren van de fruitmand, die je dan aanpast en
retourneert. Als je in plaats daarvan de `fruitmand` zelf wijzigt in
plaats van een diepe kopie, dan zou een statement als
`nieuwemand = fruitmand + "appel"` leiden tot `nieuwemand` als alias
voor `fruitmand`. Het is niet waarschijnlijk dat een programmeur die de
class gebruikt dat wil. Degene die het hoofdprogramma schrijft moet zelf
beslissen of hij of zij de fruitmand wil wijzigen, of alleen een
gewijzigde versie van de fruitmand wil zien.

In de `__iadd__()` en `__isub__()` methodes daarentegen wordt je geacht
om de fruitmand te wijzigen, en `self` te retourneren. Want een
statement als `fruitmand += "appel"` is duidelijk bedoeld om `fruitmand`
te veranderen.

De rest van de class is erg eenvoudig te begrijpen, zolang je er maar
voor zorgt dat je fruit uit de mand verwijderd met `del` wanneer er nul
of minder stuks in de mand zitten.

```python
from copy import deepcopy

class Fruitmand:

    def __init__( self, stukken={} ):
        self.stukken = stukken

    def __repr__( self ):
        s = ""
        sep = "["
        for fruit in self.stukken:
            s += sep+fruit+":"+str( self.stukken[fruit] )
            sep = ", "
        s += "]"
        return s

    def __contains__( self, fruit ):
        return fruit in self.stukken

    def __add__( self, fruit ):
        fmcopy = deepcopy( self )
        fmcopy.stukken[fruit] = fmcopy.stukken.get( fruit, 0 )+1
        return fmcopy

    def __iadd__( self, fruit ):
        self.stukken[fruit] = self.stukken.get( fruit, 0 )+1
        return self

    def __sub__( self, fruit ):
        if fruit not in self.stukken:
            return self
        fmcopy = deepcopy( self )
        fmcopy.stukken[fruit] = fmcopy.stukken.get( fruit, 0 )-1
        if fmcopy.stukken[fruit] <= 0:
            del fmcopy.stukken[fruit]
        return fmcopy

    def __isub__( self, fruit ):
        self.stukken[fruit] = self.stukken.get( fruit, 0 )-1
        if self.stukken[fruit] <= 0:
            del self.stukken[fruit]
        return self

    def __len__( self ):
        return len( self.stukken )

    def __getitem__( self, fruit ):
        return self.stukken.get( fruit, 0 )

    def __setitem__( self, fruit, n ):
        if n <= 0:
            if fruit in self.stukken:
                del self.stukken[fruit]
        else:
            self.stukken[fruit] = n

fm = Fruitmand()
fm += "appel"
fm += "appel"
fm += "banaan"
fm = fm + "kers"
fm["mango"] = 20
print( len( fm ) )
print( fm )
print( "banaan" in fm )
print( "doerian" in fm )
fm -= "appel"
fm -= "banaan"
fm = fm - "kers"
fm -= "doerian"
print( fm )
print( "banaan" in fm )
fm["mango"] = 0
print( fm )
```

### Hoofdstuk 23

#### Antwoord 22.1

```python
class Rechthoek:
    def __init__( self, x, y, b, h ):
        self.x, self.y, self.b, self.h = x, y, b, h
    def __repr__( self ):
        return "[({},{}),b={},h={}]".format( self.x, self.y,
          self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)

class Vierkant( Rechthoek ):
    def __init__( self, x, y, b ):
        super().__init__( x, y, b, b )

s = Vierkant( 1, 1, 4 )
print( s, s.oppervlakte(), s.omtrek() )
```

#### Antwoord 22.2

```python
from math import pi

class Vorm:
    def oppervlakte( self ):
        return NotImplemented
    def omtrek( self ):
        return NotImplemented

class Cirkel( Vorm ):
    def __init__( self, x, y, s ):
        self.x, self.y, self.s = x, y, s
    def __repr__( self ):
        return "[({},{}),r={}]".format( self.x, self.y, self.s )
    def oppervlakte( self ):
        return pi * self.s * self.s
    def omtrek( self ):
        return 2 * pi * self.s

class Rechthoek( Vorm ):
    def __init__( self, x, y, b, h ):
        self.x, self.y, self.b, self.h = x, y, b, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y,
            self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)

class Vierkant( Rechthoek ):
    def __init__( self, x, y, b ):
        super().__init__( x, y, b, b )

v = Vierkant( 1, 1, 4 )
print( v, v.oppervlakte(), v.omtrek() )
c = Cirkel( 1, 1, 4 )
print( c, c.oppervlakte(), c.omtrek() )
```

#### Antwoord 22.3

`GeheugenStrategie` is gedefinieerd om `OogOmOog`, `OogOmTweeOgen`, en
`Meerderheid` van af te leiden. `GeheugenStrategie` houdt alle rondes in
het spel bij. Dat is overdreven, aangezien `OogOmOog` alleen de laatste
zet hoeft te kennen, `OogOmTweeOgen` alleen de laatste twee zetten, en
`Meerderheid` kan volstaan met een totaaltelling. Maar voor
uitgebreidere strategieën kan de `GeheugenStrategie` een goed startpunt
zijn.

Een interessant resultaat van de competities tussen de strategieën is
dat `AltijdD` per definitie nooit een lagere score heeft dan zijn
tegenstander, maar dat als je iedere strategie tegen iedere andere
strategie laat spelen en dan de scores optelt, de enige strategie die
slechter scoort dan `AltijdD` de `Random` strategie is. Als je wilt
snappen hoe dat komt, volg dan een cursus speltheorie.

```python
from random import random

COOPERATIE = 'C'
DEFECTIE = 'D'
RONDES = 100

class Strategie:
    def __init__( self, naam="" ):
        self.naam = naam
        self.score = 0
    def keuze( self ):
        # Moet COOPERATIE of DEFECTIE retourneren
        return NotImplemented
    def laatstezet( self, mijnzet, tegenstanderzet ):
        # Krijgt de laatste zet die gedaan is, na keuze()
        pass
    def plusscore( self, n ):
        self.score += n

class AltijdD( Strategie ):
    def keuze( self ):
        return DEFECTIE

class Random( Strategie ):
    def keuze( self ):
        if random() >= 0.5:
            return COOPERATIE
        return DEFECTIE

class GeheugenStrategie( Strategie ):
    def __init__( self, naam="" ):
        super().__init__( naam )
        self.historie = []
    def laatstezet( self, mijnzet, tegenstanderzet ):
        self.historie.append( (mijnzet, tegenstanderzet) )

class OogOmOog( GeheugenStrategie ):
    def keuze( self ):
        if len( self.historie ) < 1:
            return COOPERATIE
        return self.historie[-1][1]

class OogOmTweeOgen( GeheugenStrategie ):
    def keuze( self ):
        if len( self.historie ) < 2:
            return COOPERATIE
        if self.historie[-1][1] == DEFECTIE and \
            self.historie[-2][1] == DEFECTIE:
            return DEFECTIE
        return COOPERATIE

class Meerderheid( GeheugenStrategie ):
    def keuze( self ):
        telD = 0
        for i in range( len( self.historie ) ):
            if self.historie[i][1] == DEFECTIE:
                telD += 1
        if telD > len( self.historie ) / 2:
            return DEFECTIE
        return COOPERATIE

strategie1 = AltijdD( "Altijd Defectie" )
strategie2 = Meerderheid( "Meerderheid" )

for i in range( RONDES ):
    c1 = strategie1.keuze()
    c2 = strategie2.keuze()
    if c1 == c2:
        strategie1.plusscore( 3 if c1 == COOPERATIE else 1 )
        strategie2.plusscore( 3 if c2 == COOPERATIE else 1 )
    else:
        strategie1.plusscore( 0 if c1 == COOPERATIE else 6 )
        strategie2.plusscore( 0 if c2 == COOPERATIE else 6 )
    strategie1.laatstezet( c1, c2 )
    strategie2.laatstezet( c2, c1 )

print( "Score van", strategie1.naam, "is", strategie1.score )
print( "Score van", strategie2.naam, "is", strategie2.score )
```

### Hoofdstuk 24

#### Antwoord 23.1

```python
from pcinput import getInteger

class NietDeelbaarDoor:
    def __init__( self ):
        self.seq = list( range( 1, 101 ) )
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
    def verwerk( self, num ):
        i = len( self.seq )-1
        while i >= 0:
            if self.seq[i]%num == 0:
                del self.seq[i]
            i -= 1
    def __len__( self ):
        return len( self.seq )

ndd = NietDeelbaarDoor()
while True:
    num = getInteger( "Geef een getal: " )
    if num < 0:
        print( "Negatieve getallen worden overgeslagen" )
        continue
    if num == 0:
        break
    ndd.verwerk( num )

if len( ndd ) <= 0:
    print( "Er zijn geen getallen meer" )
else:
    for num in ndd:
        print( num, end=" " )
```

#### Antwoord 23.2

```python
def faculteit():
    totaal = 1
    for i in range( 1, 11 ):
        totaal *= i
        yield totaal

fseq = faculteit()
for n in fseq:
    print( n, end=" " )
```

#### Antwoord 23.3

```python
from itertools import permutations

woord = input( "Geef een woord: " )
seq = permutations( woord )
for item in seq:
    print( "".join( item ) )
```

#### Antwoord 23.4

De enige wijziging tussen deze code en het antwoord op de vorige opgave
is dat ik van de iterabele een set heb gemaakt.

```python
from itertools import permutations

woord = input( "Geef een woord: " )
seq = permutations( woord )
for item in set( seq ):
    print( "".join( item ) )
```

#### Antwoord 23.5

```python
from itertools import combinations

numlist = [ 3, 8, -1, 4, -5, 6 ]
oplossing = []

for i in range( 1, len( numlist )+1 ):
    seq = combinations( numlist, i )
    for item in seq:
        if sum( item ) == 0:
            oplossing = item
            break
    if len( oplossing ) > 0:
        break

if len( oplossing ) <= 0:
    print( "Er is geen subset die optelt tot nul" )
else:
    for i in range( len( oplossing ) ):
        if oplossing[i] < 0 or i == 0:
            print( oplossing[i], end="" )
        else:
            print( "+{}".format( oplossing[i] ), end="" )
    print( "=0" )
```

{:class="callout callout-info"}
> #### Opmerking
> Hoewel deze code alle subsets bouwt, wat een aantal is dat
> exponentieel toeneemt met de lengte van `numlist`, staat er nooit meer dan één
> subset in het geheugen omdat iteratoren worden gebruikt. Dus deze
> oplossing werkt uitstekend voor zelfs lange reeksen getallen (al wordt
> hij op een gegeven moment wel erg traag, maar dat kan niet verholpen
> worden omdat dit een NP-hard probleem is).

#### Antwoord 23.6

```python
from itertools import combinations

testdict = {"a":1, "b":2, "c":3, "d":4 }
resultaat = [ {} ]

keylist = list( testdict.keys() )
for lengte in range( 1, len( testdict)+1 ):
    for item in combinations( keylist, lengte ):
        subdict = {}
        for key in item:
            subdict[key] = testdict[key]
        resultaat.append( subdict )

print( resultaat )
```

#### Antwoord 23.7

Als je de rijen en de kolommen nummert van 0 tot 7, dan komt ieder rij
nummer en ieder kolom nummer precies één keer voor in de oplossing. Neem
een list met de acht kolom nummers, en beschouw de index in deze list
als de erbij horende rij nummers. Alle potentiële oplossingen worden
gerepresenteerd door permutaties van deze list. Je hoeft alleen maar te
zoeken naar een permutatie waarbij er geen twee koninginnen op dezelfde
diagonaal staan, dus waarbij het absolute verschil tussen hun rij
nummers gelijk is aan het absolute verschil tussen hun kolom nummers.

```python
from itertools import permutations

SIZE = 8 # Bord grootte

def toon_bord( kols ):
    for i in kols :
        for j in range( len( kols ) ):
            if i == j:
                print( 'K', end=" " )
            else:
                print( '-', end=" " )
        print()

def is_oplossing( kols ):
    for rij in range( len( kols ) ):
        kol = kols[rij]
        for i in range( rij+1, len( kols ) ):
            if i - rij == abs( kols[i] - kol ):
                return False
    return True

kols = list( range( SIZE ) )

for p in permutations( kols ):
    if is_oplossing( p ):
        toon_bord( p )
        break
else:
    print( "Geen oplossing gevonden" ) # Should not happen.
```

### Hoofdstuk 25

#### Antwoord 24.1

```python
import sys

totaal = 0
for i in sys.argv[1:]:
    try:
        totaal += float( sys.argv[i] )
    except TypeError:
        print( sys.argv[i], "is geen getal." )
        sys.exit(1)

print( "The arguments add up to", totaal )
```

### Hoofdstuk 26

#### Antwoord 25.1

```python
import re

zin = "De prijs voor een 2-kamer appartement op  Manhattan \
start bij 1 miljoen dollars, en kan oplopen tot het tienvoudige \
op 42nd Street."

pwoord = re.compile( r"[A-Za-z]+" )
woordlist = pwoord.findall( zin )
for woord in woordlist:
    print( woord )
```

#### Antwoord 25.2

```python
import re

zin = "De diender arresteerde de doerak op de Dam."

pde = re.compile( r"\bde\b", re.I )
delist = pde.findall( zin )
print( len( delist ) )
```

#### Antwoord 25.3

```python
import re

zin = "Michael Jordan, Bill Gates, and de Dalai Lama besloten \
om samen een vliegtochtje te ondernemen, toen ze een hippie \
zagen op de landingsbaan."

pnaam = re.compile( r"\b([A-Z][a-z]*\s+[A-Z][a-z]*)\b" )
naamlist = pnaam.findall( zin )
for naam in naamlist:
    print( naam )
```

#### Antwoord 25.4

```python
import re

zin = "William Randolph Hearst trachtte alle exemplaren van \
Orson Welles' meesterwerk 'Citizen Kane', te vernietigen, omdat \
hij het bezwaarlijk vond dat de protagonist een nauwelijks-\
verhulde karikatuur van hemzelf was. Ik vraag me af of William \
Henry Gates De Derde hetzelfde zou doen."

pnaam = re.compile( r"\b([A-Z][a-z]*(\s+[A-Z][a-z]*)+)\b" )
naamlist = pnaam.finditer( zin )
for naam in naamlist:
    print( naam.group(1) )
```

#### Antwoord 25.5

```python
import re

zin = "Klant: \"Ik wens een klacht te deponeren! \
Hallo mevrouw!\"\n\
Winkelier: \"Hoe bedoelt u, mevrouw?\"\n\
Klant: \"Het spijt me, ik ben verkouden.\"\n"

pgesproken = re.compile( r"\"[^\"]*\"" )
gesprokenlist = pgesproken.findall( zin )
for tekst in gesprokenlist:
    print( tekst )
```

#### Antwoord 25.6

```python
import re

tekst = "<html><head><title>Lijst van personen met ids</title>\
</head><body>\
<p><id>123123123</id><naam>Groucho Marx</naam>\
<p><id>123123124</id><naam>Harpo Marx</naam>\
<p><id>123123125</id><naam>Chico Marx</naam>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</naam></randomcrap>\
<nocrap><p><id>123123126</id><naam>Zeppo Marx</naam></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>geennaamtezien!\
</morerandomcrap>\
<p><id>123123127</id><naam>Gummo Marx</naam>\
<note>Zoek hem op via <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"

pidnaam = re.compile( r"<id>([^<]+)</id><naam>([^<]+)</naam>" )
mlist = pidnaam.finditer( tekst )
for m in mlist:
    print( m.group(1), m.group(2) )
```

### Hoofdstuk 27

#### Antwoord 26.1

```python
from csv import reader, writer

fp = open( "pc_inventory.csv", newline='' )
fpo = open( "pc_writetest.csv", "w", newline='' )
csvreader = reader( fp )
csvwriter = writer( fpo, delimiter=' ', quotechar="'" )
for line in csvreader:
    csvwriter.writerow( line )
fp.close()
fpo.close()

fp = open( "pc_writetest.csv" )
print( fp.read() )
fp.close()
```

Als je dit correct het gedaan, zie je dubbele aanhalingstekens rondom
"Blue Stilton," die daar staan omdat er een spatie in voorkomt.

#### Antwoord 26.2

```python
from csv import reader
from json import dump

data = []

fp = open( "pc_inventory.csv", newregel='' )
csvreader = reader( fp )
for regel in csvreader:
    data.append( regel )
fp.close()

fp = open( "pc_writetest.json", "w" )
dump( data, fp )
fp.close()

fp = open( "pc_writetest.json" )
print( fp.read() )
fp.close()
```

### Hoofdstuk 28

#### Antwoord 27.1

```python
from collections import Counter

z = "Je moeder was een hamster en je vader rook naar vlierbessen"
zin2 = ""
for c in z.lower():
    if c >= 'a' and c <= 'z':
        zin2 += c

clist = Counter( zin2 ).most_common( 5 )
for c in clist:
    print( "{}: {}".format( c[0], c[1] ) )
```

#### Antwoord 27.2

```python
from collections import Counter
from pcinput import getInteger
from statistics import mean, median
from sys import exit

numlist = []
while True:
    num = getInteger( "Geef een getal: " )
    if num == 0:
        break
    numlist.append( num )

if len( numlist ) <= 0:
    print( "Geen getallen ingegeven" )
    exit()

print( "Gemiddelde:", mean( numlist ) )
print( "Mediaan:", median( numlist ) )

clist = Counter( numlist ).most_common()
if clist[0][1] <= 1:
    print( "Er is geen modus" )
else:
    mlist = [str( x[0] ) for x in clist if x[1] == clist[0][1] ]
    s = ", ".join( mlist )
    print( "Modus:", s )
```

Voor de modus heb ik een redelijk slimme list comprehension geschreven,
maar je kunt dit uiteraard ook in meerdere regels code schrijven.
