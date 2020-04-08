Stel dat je de gebruik om paren getallen vraagt in een loop. Voor ieder
paar getallen dat de gebruiker ingeeft wil je laten zien wat hun
vermenigvuldiging is. Je wilt de gebruiker het programma laten stoppen
als hij een nul ingeeft, ongeacht voor welk getal. Vanwege een onbekende
reden mogen de twee getallen geen delers van elkaar zijn; als ze dat wel
zijn is dat een fout en wordt het programma onmiddellijk gestopt met een
foutboodschap. Tenslotte is het een eis dat de getallen in het bereik 0
tot en met 1000 liggen; als de gebruiker een getal ingeeft dat niet in
dat bereik zit wordt dat echter niet beschouwd als een fout; je wilt
gewoon dat de gebruiker dan een nieuw getal ingeeft. Hoe programmeer je
zoiets? Hier is een eerste poging:

```python
from pcinput import getInteger

x = 3
y = 7

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    x = getInteger( "Geef nummer 1: " )
    y = getInteger( "Geef nummer 2: " )
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Nummers moeten tussen 0 en 1000 zijn" )
        continue
    print( x, "keer", y, "is", x * y )
    
if x == 0 or y == 0:
    print( "Klaar!" )
else:
    print( "Fout: de nummers mogen geen delers zijn" )
```

Bestudeer deze code en maak een lijstje van alles wat je er slecht aan
vindt. Als je dat gedaan hebt, lees dan verder en vergelijk je
bevindingen met het lijstje hieronder. Als je zaken hebt aangetroffen
die slecht zijn en die niet op de lijst staan, kun je me emailen.

Er zijn veel zaken die ik slecht vind aan deze code. Hier is mijn lijst:

-   Om ervoor te zorgen dat de loop op zijn minst één keer wordt
    uitgevoerd, moeten `x` en `y` geïnitialiseerd worden. Waarom met 3
    en 7? Dat is willekeurig, maar ik moest twee getallen nemen die geen
    delers van elkaar zijn. Anders zou de loop niet zijn gestart. Over
    het algemeen is het niet netjes om variabelen startwaardes te geven
    die lijken een betekenis te hebben, terwijl ze er alleen maar zijn
    om de variabelen te laten bestaan terwijl de waardes betekenisloos
    zijn. Dat wil je het liefst vermijden.

-   Als je iets ingeeft dat de loop zou moeten beëindigen (bijvoorbeeld
    nul voor `x`), dan wordt alsnog de vermenigvuldiging uitgevoerd
    voordat de loop eindigt. Dat was niet de bedoeling.

-   Als je 0 ingeeft voor `x`, dan wordt alsnog om `y` gevraagd, hoewel
    het niet uitmaakt wat voor waarde voor `y` wordt ingegeven.

-   De boolean expressie naast de `while` is nogal complex. In deze code
    is hij nog wel leesbaar, maar meer eisen aan de getallen maken het
    behoorlijk onbegrijpelijk.

-   De foutboodschap voor de delers wordt niet gegeven bij de test waar
    besloten wordt het programma af te breken (dat wil zeggen, de
    boolean expressie bij de `while`).

De oplossing voor deze zaken die door sommige programmeurs geprefereerd
wordt, is om `x` en `y` te initialiseren met waardes die de gebruiker
ingeeft. Dit lost de willekeurige initialisatie op, en lost ook het
probleem op dat je de vermenigvuldiging uitvoert als dat niet meer
hoeft. Je moet dan wel het vragen om input verplaatsen naar het einde
van de loop. Als er dan een `continue` voorkomt in de loop, moet je vlak
voor die continue ook om de inputs vragen, anders krijg je een eindeloze
loop. De code wordt dan iets als:

```python
from pcinput import getInteger

x = getInteger( "Geef nummer 1: " )
y = getInteger( "Geef nummer 2: " )

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Nummers moeten tussen 0 en 1000 zijn" )
        x = getInteger( "Geef nummer 1: " )
        y = getInteger( "Geef nummer 2: " )
        continue
    print( x, "keer", y, "is", x * y )
    x = getInteger( "Geef nummer 1: " )
    y = getInteger( "Geef nummer 2: " )

if x == 0 or y == 0:
    print( "Klaar!" )
else:
    print( "Fout: de nummers mogen geen delers zijn" )
```

De code vermijdt twee van de drie genoemde problemen, maar voegt een
nieuwe toe, die het mijns inziens alleen maar erger maakt. De lijst van
problemen wordt:

-   Het vragen van input komt nu drie keer voor in de code, in plaats
    van slechts één keer.

-   Als je 0 ingeeft voor `x`, vraagt de code nog steeds om een waarde
    voor `y`.

-   De boolean expressie bij de `while` is nogal complex.

-   De foutmelding voor de delers staat niet bij de plek waar besloten
    wordt de loop te verlaten.

De "truc" die je kunt gebruiken om deze problemen te verhelpen is de
besturing van de loop puur te doen middels `continue`s en `break`s (een
misschien soms een `exit()` als er een fout optreedt, maar in het
volgende hoofdstuk wordt daar een "nettere" oplossing voor geboden). Dus
je voert de loop "altijd" uit, maar je besluit om de loop te verlaten of
opnieuw in te gaan als bepaalde omstandigheden optreden die je pas *in*
de loop controleert (en niet vooraf). Om een loop "altijd" uit te voeren
kun je `while True` gebruiken (dit betekent: de test die je uitvoert om
te besluiten of de loop uitgevoerd moet worden, geeft altijd `True`).

```python
from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Geef nummer 1: " )
    if x == 0:
        break
    y = getInteger( "Geef nummer 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "Nummers moeten tussen 0 en 1000 zijn" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Fout: de nummers mogen geen delers zijn" )
        exit()
    print( x, "keer", y, "is", x * y )

print( "Klaar!" )
```

Deze code lost vrijwel alle problemen op. Het vraagt slechts eenmalig om
`x` en `y`. Er is geen willekeurige initialisatie van `x` en `y`. De
loop stopt onmiddellijk als een nul wordt ingegeven. En de foutmelding
staat meteen daar waar de fout geconstateerd wordt. Er is geen complexe
boolean expressie nodig met een hoop `and`s en `or`s. De code is een
beetje langer dan de eerste versie, maar lengte maakt niet uit, en de
code is een stuk leesbaarder.

Het enige probleem dat nog over is, is dat als de gebruiker een waarde
ingeeft buiten het bereik 0 tot en met 1000 voor `x`, hij nog steeds een
waarde voor `y` moet ingeven alvorens het programma zegt dat de getallen
opnieuw ingegeven moeten worden. Dat kun je het beste oplossen met
functies, wat besproken wordt in het volgende hoofdstuk (je kunt het
eventueel nu al oplossen met een geneste loop, maar ik zou me er niet
druk om maken).

Een loop als deze, die `while True` gebruikt, wordt soms een
"loop-en-een-half" genoemd. Het is een heel gebruikelijke aanpak voor
het schrijven van een loop waarbij je niet precies weet wanneer de loop
moet eindigen.

De gebruiker geeft een positief geheel getal. Je gebruikt daarvoor de
`getInteger()` functie van `pcinput`. Deze functie staat het echter ook
toe om negatieve getallen in te geven. Als de gebruiker een negatief
getal ingeeft, wil je melden dat dat niet mag, en hem opnieuw een getal
laten ingeven. Dit blijf je doen totdat daadwerkelijk een positief getal
is ingegeven. Zodra een positief getal is ingegeven, druk je dat af en
stopt het programma. Een dergelijk probleem wordt typisch aangepakt met
een loop-en-een-half, omdat je geen idee hebt van hoe vaak een gebruiker
een negatief getal ingeeft totdat hij wijs wordt. Schrijf zo'n
loop-en-een-half. Je heb precies één `break` nodig, en hoogstens één
`continue`. Druk het positieve getal dat de gebruiker heeft ingegeven af
*na* de loop. De reden om het erna te doen is dat de loop alleen bedoeld
is om de input onder controle te krijgen, en niet voor het verwerken van
de correcte ingave.

Ik heb vaak geconstateerd dat studenten het gebruik van `while True`
maar verwarrend vinden. Ze zien het vaak in voorbeeldcode, maar ze
snappen niet echt het nut ervan. En vervolgens gaan ze `while True`
opnemen in code van henzelf als ze niet precies weten wat ze moeten
doen. Als je problemen hebt de loop-en-een-half te begrijpen, bestudeer
dan deze paragraaf opnieuw, totdat je het wel begrijpt.
