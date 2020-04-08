Een alternatieve manier om loops te implementeren is via de `for` loop.
`for` loops zijn gemakkelijker en veiliger te gebruiken dan `while`
loops, maar kunnen niet voor alle iteratie problemen gebruikt worden.
`while` loops bieden een generieke oplossing voor loops. Met andere
woorden, alles wat een `for` loop kan doen, kan een `while` loop ook
doen, maar niet andersom.

De syntax voor de `for` loop is:

```python
for <variabele> in <collectie>:
    <acties>
```

A `for` loop krijgt een collectie van items, en verwerkt deze items één
voor één in de volgorde waarin ze worden aangeboden. Iedere cyclus door
de loop verwerkt één item door het in de variabele te stoppen die naast
de `for` staat. Die variabele kan dan gebruikt worden in het blok code
van de loop. De variabele hoeft niet te bestaan voordat de `for` loop
bezocht wordt. Als de variabele al bestaat, wordt hij overschreven. Als
hij nog niet bestaat, wordt hij aangemaakt. Het is overigens een echte
variabele, in de zin dat hij nog steeds bestaat als de loop afgelopen
is. Na afloop van de loop bevat hij het laatste item dat verwerkt is.

Op dit punt vraag je je wellicht af wat een "collectie" is. Er zijn
verschillende soorten collecties in Python, en ik zal er een paar
introduceren in dit hoofdstuk. In latere hoofdstukken volgen er meer.

### `for` loop met strings

De enige collectie die in de voorgaande hoofdstukken besproken is, is de
string. Een string is een collectie van tekens, bijvoorbeeld, de string
`"banaan"` is een collectie van de tekens `"b", "a", "n", "a", "a"`, en
`"n"`, in die specifieke volgorde. De volgende code verwerkt ieder van
de tekens van deze collectie:

```python
for letter in "banaan":
    print( letter )
print( "Klaar" )
```

Hoewel deze code vrij triviaal is, zal ik hem voor de duidelijkheid stap
voor stap bespreken (ik heb geen stroomdiagram gemaakt, want dat is
lastig voor `for` loops).

Als de `for` loop wordt aangetroffen, neemt Python de collectie (de
string `"banaan"` in dit geval) en maakt er een zogeheten "iterabele"
van. Wat dat precies is komt pas in hoofdstuk
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>
aan de orde, maar vooralsnog mag je aannemen dat het een lijst is van
alle tekens in de string, in de volgorde dat ze in de string staan.
Python neemt dan de eerste van deze tekens, en stopt hem in de variabele
`letter`. Daarna voert Python het blok code onder de `for` uit.

Het blok code bevat maar één regel, namelijk het printen van `letter`.
Het programma print dus de letter "b," en keert dan terug bij de `for`.
Python neemt dan het volgende teken, namelijk de eerste "a," en voert
wederom het blok code uit, maar nu met `"a"` als waarde in `letter`. Dit
proces wordt herhaald voor ieder van de tekens. Nadat alle tekens
verwerkt zijn, eindigt de `for` loop. Python voert dan nog de laatste
regel van het programma uit, het printen van het woord "Klaar."

Om volledig helder te zijn: In de `for` loop hoef je niet ergens
expliciet een variabele te verhogen of zo, of zelf iets te schrijven dat
het volgende teken van de string pakt. De `for` loop handelt dat
automatisch af: iedere keer dat de loop terugkeert bij de regel met de
`for`, wordt het volgende item uit de collectie gepakt.

### `for` loop met een variabele collectie

In de code hierboven wordt de string `"banaan"` gebruikt als collectie,
maar er had ook een variabele gebruikt kunnen worden die een string
bevat. Bijvoorbeeld, de volgende code is gelijk aan de vorige:

```python
fruit = "banaan"
for letter in fruit:
    print( letter )
print( "Klaar" )
```

Je kunt je afvragen of dat niet gevaarlijk is. Wat gebeurt er als de
programmeur iets in het blok code van de loop schrijft dat de inhoud van
de variabele `fruit` wijzigt? Je kunt het effect hiervan testen met de
volgende code:

```python
fruit = "banaan"
for letter in fruit:
    print( letter )
    if letter == "n":
        fruit = "mango"
print( "Klaar" )
```

Als je deze code uitvoert, merk je dat het wijzigen van de inhoud van de
variabele `fruit` in de loop geen effect heeft op het proces. De serie
tekens die de loop verwerkt wordt slechts eenmalig bepaald, namelijk de
eerste keer dat Python de loop betreedt. Het wijzigen van `fruit` in
`"mango"` gedurende het proces waarbij de loop de tekens van `"banaan"`
verwerkt, laat de loop niet ophouden met het verwerken `"banaan"`. Het
is een prachtige eigenschap van `for` loops dat ze gegarandeerd
eindigen. `for` loops kunnen niet eindeloos zijn![^6]

Wat bovenstaande code ook illustreert is dat het mogelijk is om een
conditie in het blok code van een loop te stoppen. Wellicht verbaast je
dat niet, en het hoeft je ook niet te verbazen, want de syntactische
definitie van loops legt geen beperkingen op aan wat de acties zijn die
een loop mag uitvoeren. Dus zulke acties mogen condities zijn. Het mogen
zelfs loops zijn (meer daarover volgt later in dit hoofdstuk).

### `for` loop met een getallenreeks

Pythin heeft een functie `range()` die het mogelijk maakt een serie
opeenvolgende getallen te genereren. `range()` wordt vaak gebruikt in
combinatie met een `for` loop, bijvoorbeeld om een loop te maken die een
specifiek aantal malen wordt uitgevoerd. De eenvoudigste manier om
`range()` aan te roepen is met één parameter, namelijk een integer. De
functie genereert dan een opeenvolgende lijst van integers, beginnend
bij nul, tot aan maar niet inclusief de parameter.

```python
for x in range( 10 ):
    print( x )
```

`range()` kan meer dan één parameter meekrijgen. Als je er twee
meegeeft, dan is de eerste het startgetal (de default is nul), en de
tweede het eindgetal. Het eerste getal zit in de gegenereerde serie, het
tweede niet. Als je drie getallen meegeeft, zijn de eerste twee als
direct hiervoor aangegeven, en is de derde een stapgrootte, dat wil
zeggen, de afstand tussen de gegenereerde getallen. Default stapgrootte
is 1. Als je wilt aftellen dan is dat mogelijk: je geeft dan een
negatieve stapgrootte. Je moet dan wel ervoor zorgen dat het startgetal
groter is dan het eindgetal.

```python
for x in range( 1, 11, 2 ):
    print( x )
```

Wijzig in bovenstaande code de drie parameters een paar keer, om het
effect van deze wijzigingen te bestuderen. Ga door totdat je de
`range()` functie begrijpt.

Gebruik een `for` loop en een `range()` functie om veelvouden van 3 af
te drukken, beginnend bij 21, aftellend tot 3, in slechts twee regels
code.

### `for` loop met een handmatige collectie

Als je een serie items hebt in een collectie die je "handmatig" hebt
samengesteld, kun je die middels een `for` loop verwerken als je de
items tussen haakjes zet. Een serie items tussen haakjes is een "tuple."
Tuples worden in hoofdstuk
<a href="#ch:tuples" data-reference-type="ref" data-reference="ch:tuples">12</a>
uitgebreid besproken.

```python
for x in ( 10, 100, 1000, 10000 ):
    print( x )
```

Of:

```python
for x in ( "appel", "peer", "druif", "banaan", "mango", "kers" ):
    print( x )
```

Een collectie die je zo samenstelt mag zelfs uit verschillende data
types bestaan.

### `for` loop oefeningen

Om grip te krijgen op het gebruik van `for` loops, zijn hier een paar
oefeningen:

Je hebt al code gecreëerd voor een `while` loop waarin om vijf getallen
wordt gevraagd en het totaal getoond wordt. Doe dat nu met een `for`
loop.

Je hebt ook code gecreëerd voor een `while` loop die aftelt tot nul, en
dan "Start!" print. Doe dat nu met een `for` loop.

Ik ga geen oefening geven waarin je met een `for` loop de gebruiker
vraagt om getallen totdat de gebruiker nul ingeeft. Waarom niet?
