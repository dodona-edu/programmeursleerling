Ter afronding van dit hoofdstuk, bediscussieer ik een aantal strategieën
voor het ontwerpen van loops, en het ontwerpen van algoritmes in het
algemeen.

### Wanneer gebruik je een loop

Als je vijf zes-zijdige dobbelstenen rolt, hoe groot is dan de
waarschijnlijkheid dat je vijf zessen rolt? het antwoord is $$1/(6^5)$$,
maar stel dat je dat niet weet, en je wilt een simulatie gebruiken om de
waarschijnlijkheid te schatten. Je kunt het rollen van een dobbelstenen
imiteren via `randint()`, dus daarmee kun je ook het rollen van vijf
dobbelstenen imiteren. Je kunt testen of ze alle zes zijn. Dat kun je
een heleboel keren doen, en aan het eind van je programma deel je het
aantal keren dat er vijf zessen vielen door het totaal aantal pogingen.
Als ik dit probleem voorleg aan studenten (in een iets ingewikkeldere
vorm zodat het antwoord niet gemakkelijk berekend kan worden), dan krijg
ik vaak code die er als volgt uitziet (je moet `TESTS` een grotere
waarde geven voor een betere schatting, maar ik wilde dat deze code niet
teveel tijd vergt om uit te voeren):

```python
from random import randint

TESTS = 10000
succes = 0
for i in range( TESTS ):
    d1 = randint( 1, 6 )
    d2 = randint( 1, 6 )
    d3 = randint( 1, 6 )
    d4 = randint( 1, 6 )
    d5 = randint( 1, 6 )
    if d1 == 6 and d2 == 6 and d3 == 6 and d4 == 6 and d5 == 6:
        succes += 1
print( "Waarschijnlijkheid van vijf zessen is", succes / TESTS )
```

Als ik dit soort code zie, vraag ik: "Wat had je gedaan als ik gevraagd
had 100 dobbelstenen te rollen? Had je 100 variabelen gemaakt en die
regel code die ze rolt 100 keer gekopieerd?" Als je een stukje code hebt
dat een paar keer herhaald wordt met slechts een kleine wijziging erin
(of wanneer je aan het kopiëren en plakken bent in je eigen code), dan
moet je beginnen te denken aan loops. Je kunt vijf dobbelstenen als
volgt rollen:

```python
from random import randint

for i in range( 5 ):
    d = randint( 1, 6 )
```

"Maar," hoor ik sommigen al protesteren: "ik moet de waarde van al die
vijf dobbelstenen hebben om te testen of het vijf zessen zijn! Iedere
keer dat deze code door de loop gaat, gooi je de vorige
dobbelsteenwaarde weg!" Dat is waar, maar de regel die test of ze
allemaal een zes zijn is ook erg lelijk. Kan dit geheel niet
gestroomlijnd worden? Kun je geen conclusie trekken als je één
dobbelsteen rolt?

Als je hier een beetje over nadenkt, kom je wellicht op het volgende
idee: zodra je een dobbelsteen rolt die géén zes is, heb je al gefaald
in je poging om vijf zessen te rollen, en kun je gelijk doorgaan met de
volgende poging. Er zijn diverse manieren om dit te implementeren, maar
hier is een hele korte die gebruik maakt van een `break` en een `else`:

```python
from random import randint

TESTS = 10000
succes = 0
for i in range( TESTS ):
    for j in range( 5 ):
        if randint( 1, 6 ) != 6:
            break
    else:
        succes += 1
print( "Waarschijnlijkheid van vijf zessen is", succes / TESTS )
```

Je denkt wellicht dat het moeilijk is om zoiets te verzinnen, maar het
is echt niet de enige manier. Je kunt, bijvoorbeeld, de waardes van de
dobbelstenen in de loop optellen en dan testen of het totaal 30 is na de
loop. Of je kunt tellen hoeveel dobbelstenen een zes zijn en dan testen
of dat vijf is na de loop. Of je kunt voor de loop een boolean variabele
op `True` zetten, en die in de loop op `False` zetten zodra een
dobbelsteen niet op zes valt; dan kun je die boolean testen na de loop.

Het punt is dat een willekeurig lange herhaling van stukken code vrijwel
altijd vervangen kan worden door een loop.

### Data items één voor één verwerken

Het is gebruikelijk dat loops een serie data items verwerken. Iedere
cyclus door de loop verwerkt dan één van die items. Vaak moet je iets
onthouden over de items die je verwerkt hebt, en daarvoor heb je extra
variabelen nodig. Je moet slim nadenken over welke variabelen je nodig
hebt.

Neem het volgende voorbeeld: ik geef je tien getallen en vraag je een
programma te schrijven dat bepaalt welke de grootste is, welke de
kleinste, en hoeveel er deelbaar zijn door 3. Je kunt dan zeggen: "Het
is gemakkelijk te bepalen wat de grootste en de kleinste zijn: daar
gebruik ik gewoon de `max()` en `min()` functies voor (besproken in
hoofdstuk
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>).
Deelbaar door 3 is misschien wat moeilijker, daar moet ik over denken."
Maar `max()` en `min()` maken het noodzakelijk dat alle tien de getallen
tegelijkertijd in het geheugen worden gehouden. Dat is nog te doen voor
tien getallen, maar wat als ik om honderd had gevraagd? Of een miljoen?

Omdat je een serie getallen moet verwerken, moet je denken over een
loop, en specifiek over een loop waarin iedere cyclus door de loop één
van die getallen beschikbaar is (maar waarbij ze allemaal voorbij zullen
komen voordat de loop eindigt). Je moet nu denken over variabelen
waarmee je iets kunt onthouden in de loop, die ervoor zorgen dat je aan
het einde van de loop kunt bepalen welke de grootste was, welke de
kleinste, en hoeveel deelbaar zijn door 3. Welke variabelen heb je
nodig?

Het antwoord, dat gemakkelijk te verzinnen is voor iemand die wat
ervaring heeft met programmeren, is dat je iedere cyclus door de loop
moet onthouden welk getal het grootste is *tot nu toe*, welk het
kleinste is *tot nu toe*, en hoeveel er deelbaar zijn door 3 *tot nu
toe*. Dat betekent dat iedere keer dat je door de loop gaat het nieuw
aangeboden getal vergelijkt met de variabelen die de grootste en de
kleinste bijhouden, en je de inhoud van de variabelen vervangt als dat
nodig is. Je test ook of het nieuw aangeboden getal deelbaar is door 3,
en zo ja, dan verhoog je de variabele die bijhoudt hoeveel er deelbaar
zijn door 3 met 1.

Je moet goede initiële waardes bepalen voor de drie variabelen. De
variabele die deelbaar-door-3 bijhoudt is eenvoudig; die begint op nul.
Het is wat lastiger voor de grootste en kleinste variabelen. Een goede
oplossing is ze te vullen met het eerste getal, want op dat moment is
dat eerste getal zowel de grootste als de kleinste.

Dit probleem staat hieronder als een genummerde opgave. Gebruik het
beschreven algoritme om de opgave op te lossen.

### Begin met de kleinste en bouw naar buiten op

Stel dat ik je de volgende opdracht geef: Van alle boeken op alle
planken in de bibliotheek moet je het aantal woorden tellen, en
tenslotte moet je het gemiddelde aantal woorden per boek rapporteren.
Als je dit aan een mens vraagt, zal hij of zij waarschijnlijk denken:
"Ik ga naar de bibliotheek, neem het eerste boek van de eerste plank,
tel de woorden en schrijf het totaal op, dan neem ik het tweede boek en
doe hetzelfde, etcetera. Als ik klaar ben met de eerste plank, doe ik
hetzelfde met de tweede, totdat alle boeken op alle planken gedaan heb.
Dan tel ik alle totalen op, en deel dat door het aantal boeken." Voor
mensen werkt dit, maar als ik dit aan een computer wil vertellen, is dat
best lastig.

Om dit probleem op te lossen, moet ik beginnen met de kleinste eenheid
van verwerking. In dit geval is de kleinste eenheid een "boek." Het is
niet "woord," want ik hoef niks te doen met woorden; ik moet totalen
woorden per boek hebben. In pseudo-code,[^8] wordt het tellen van
woorden per boek iets als:

```python
woordtotaal = 0
for woord in boek:
    woordtotaal += 1
```

Als ik zoiets codeer, kan ik het al testen. Als ik tevreden ben dat ik
woorden per boek kan tellen, kan ik naar een iets grotere eenheid gaan,
en dat is de "plank." Hoe verwerk ik alle boeken op een plank? In
pseudo-code is dat iets als:

```python
for boek on plank:
    verwerk_boek()
```

Wat doet `verwerk_boek()`? Het telt de woorden. Ik heb al pseudo-code
geschreven om woorden te tellen, en die kan ik hier invoegen. Dat wordt
dan:

```python
for boek in plank:
    woordtotaal = 0
    for woord in boek:
        woordtotaal += 1
```

Als ik dit test, loop ik tegen een probleem aan. Ik tel weliswaar
woorden per boek, maar ik doe niks met die totalen. Ik overschrijf die
gewoon. Om straks het gemiddelde te kunnen bepalen, moet ik het totaal
van het aantal woorden weten over alle boeken. Dat betekent dat ik
`woordtotaal` slechts één keer moet initialiseren, namelijk aan het
begin.

```python
woordtotaal = 0
for boek in plank:
    for woord in boek:
        woordtotaal += 1
```

Maar om het gemiddelde te kunnen uitrekenen, moet ik ook weten hoeveel
boeken ik verwerkt heb. Dat kan ik doen met een teller `boektotaal`, die
ook slechts eenmalig geïnitialiseerd moet worden. Aan het einde kan ik
dan het gemiddelde afdrukken.

```python
woordtotaal = 0
boektotaal = 0
for boek in plank:
    for woord in boek:
        woordtotaal += 1
    boektotaal += 1
print( woordtotaal / boektotaal )
```

Nu kan ik naar het hoogste niveau gaan: de bibliotheek als geheel. Ik
weet hoe ik één plank moet verwerken, en nu moet ik alle planken
verwerken. Natuurlijk moet de initialisatie van de totalen alleen aan
het begin gedaan worden, en het afdrukken van het gemiddelde alleen aan
het einde. Dat wil zeggen dat ik slechts één regel hoef toe te voegen om
de pseudo-code af te maken:

```python
woordtotaal = 0
boektotaal = 0
for plank in bibliotheek:
    for boek in plank:
        for woord in boek:
            woordtotaal += 1
        boektotaal += 1
print( woordtotaal / boektotaal )
```

Zoals je ziet heb ik een drievoudig-geneste loop ontworpen, werkend van
binnen naar buiten. Dit is een goede aanpak als je met geneste loops aan
de slag moet.

[^8]: pseudo-code is geen echte code, maar het leest als code, en zou
    als zodanig gemakkelijk te implementeren moeten zijn in
    verschillende programmeertalen.
