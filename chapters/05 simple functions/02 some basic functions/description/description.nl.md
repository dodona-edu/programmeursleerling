Ik introduceer nu een aantal basis functies die je in je programma's
kunt gebruiken.

### Type casting

Ik heb al gesproken over type casting functies in hoofdstuk
<a href="#ch:variables" data-reference-type="ref" data-reference="ch:variables">5</a>,
maar nu ik meer details van functies heb gegeven, kan ik de beschrijving
completeren.

-   `float()` heeft één parameter en retourneert een floating-point
    representatie van de waarde van de parameter. Als de waarde een
    integer is, krijg je dezelfde waarde terug als float. Als de
    parameter een float is, krijg je dezelfde waarde terug. Als de
    parameter een string bevat die je als integer of float zou kunnen
    interpreteren, dan krijg je die float terug als waarde. Anders krijg
    je een runtime error.

-   `int()` heeft één parameter en retourneert een integer representatie
    van de waarde van de parameter. Als de waarde een integer is, krijg
    je dezelfde waarde terug. Als de waarde een float is, krijg je een
    integer terug die de waarde van de float naar beneden heeft
    afgerond. Als de parameter een string bevat die je als integer zou
    kunnen interpreteren, dan krijg je die integer terug als waarde.
    Anders krijg je een runtime error.

-   `str()` heeft één parameter en retourneert een string representatie
    van de waarde van de parameter.

Wat denk je dat de volgende code doet? Als je het niet weet, test dan de
code.

```python
print( 10 * int( "100,000,000" ) )
```

De code hierboven geeft een runtime error. Los het probleem op door
precies twee tekens te verwijderen.

### Berekeningen

Een paar basis Python functies helpen met berekeningen.

-   `abs()` krijgt een numerieke parameter waarde. Als de waarde
    positief is, wordt hij weer geretourneerd. Als de waarde negatief
    is, wordt de waarde vermenigvuldigd met -1 geretourneerd.

-   `max()` krijgt twee of meer numerieke parameters en retourneert de
    grootste.

-   `min()` krijgt twee of meer numerieke parameters en retourneert de
    kleinste.

-   `pow()` krijgt twee numerieke parameters en retourneert de eerste
    verheven tot de macht weergeven door de tweede. Optioneel mag je een
    derde parameter meegeven, die een integer moet zijn. Als je dat
    doet, krijg je de waarde modulo de derde parameter terug.

-   `round()` krijgt een numerieke parameter die wiskundig wordt
    afgerond. Optioneel mag je als tweede parameter een integer meegeven
    die aangeeft hoeveel cijfers achter de komma behouden moeten worden.
    Als de tweede parameter niet wordt meegegeven, wordt afgerond op
    gehele getallen.

Bekijk de code hieronder en bedenk wat er op het scherm getoond wordt.
Voer daarna de code uit en controleer of je gelijk hebt.

```python
x = -2
y = 3
z = 1.27

print( abs( x ) )
print( max( x, y, z ) )
print( min( x, y, z ) )
print( pow( x, y ) )
print( round( z, 1 ) )
```

### `len()`

`len()` is a basis functie die één parameter krijgt, en die de lengte
van die parameter teruggeeft. Op dit moment is het enig zinvolle data
type dat je mee kunt geven aan `len()` een string, waarvan je dan de
lengte krijgt. In latere hoofdstukken volgen meer data types waarvan je
de lengte kunt bepalen.

Wat print de code hieronder? Controleer of je vermoeden klopt.

```python
print( len( 'man' ) )
print( len( 'mango' ) )
print( len( "" ) )  # "" is een lege string
```

En wat denk je van de code hieronder? Denk goed na voor je een antwoord
geeft.

```python
print( len( 'mango\'s' ) )
```

### `input()`

In veel programma's wil je dat de gebruiker van het programma data
verstrekt. Je kunt de gebruiker vragen een string in te typen met behulp
van de functie `input()`. De functie krijgt één parameter mee, namelijk
een string. Deze string is de zogeheten "prompt." Als `input()` wordt
aangeroepen, wordt de prompt op het scherm gezet en mag de gebruiker een
tekst ingeven. De gebruiker mag ingeven wat hij of zij wil, inclusief
niks. De gebruiker sluit het ingeven af met een druk op de `Enter`
toets. De retour waarde van de functie is hetgeen de gebruiker heeft
ingegeven, exclusief de `Enter`.

Het hangt van de omgeving waar je je programma in draait hoe de
gebruiker de ingave precies doet. Soms wordt er een rechthoek op het
scherm getoond met de prompt ervoor waarin de gebruiker mag typen. Als
je een Python programma draait op de command-line, moet de gebruiker ook
de ingave op de command-line doen. Sommige editors tonen een
popup-window waarin de gebruiker moet typen.

Hier is een voorbeeld:

```python
tekst = input( "Geef een tekst in: " )
print( "Je hebt het volgende ingetypt:", tekst )
```

Realiseer je dat `input()` altijd een string teruggeeft. Bekijk de
volgende code:

```python
nummer = input( "Geef een getal: " )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Het maakt niet uit wat je ingeeft, deze code geeft een runtime error.
Omdat `input()` een string teruggeeft, wordt op de tweede regel een
poging gedaan twee strings met elkaar te vermenigvuldigen, en dat kan
niet. Het maakt niet uit of je string een getal bevat: een string is een
string. Je kunt het probleem oplossen middels type casting,
bijvoorbeeld:

```python
nummer = input( "Geef een getal: " )
nummer = float( nummer )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Voor deze code geldt dat als de gebruiker een getal ingeeft, de code
doet wat hij moet doen. Maar als de gebruiker iets anders ingeeft, dat
niet in een getal omgezet kan worden, krijg je toch weer een runtime
error. Ook dat probleem kan opgelost worden, maar ik heb nog niet de
zaken uitgelegd die je nodig hebt om dit probleem aan te pakken, en het
zal nog tot hoofdstuk
<a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a>
duren voordat ik eraan toekom. Tot dat moment geef ik iets later in dit
hoofdstuk een methode die je kunt gebruiken om je programma om een getal
te laten vragen zonder dat het "crasht" als de gebruiker een wijsneus
probeert te zijn en iets anders ingeeft.

Schrijf code die de gebruiker twee getallen laat ingeven, en die dan
toont wat de uitkomst is als je ze optelt en als je ze vermenigvuldigt.
Je code mag een runtime error geven als de gebruiker iets ingeeft wat
geen getal is.

### `print()`

De functie `print()` krijgt nul of meer parameters mee, toont ze op het
scherm (als het er meerdere zijn, met spaties ertussen), en gaat daarna
naar de volgende regel. Dus als je twee `print` statements gebruikt,
komt de output van de tweede onder die van de eerste te staan.

Als `print()` wordt aangeroepen zonder parameters, gaat de functie
alleen naar de volgende regel. Zo kun je lege regels op het scherm
zetten.

Je mag als parameters meegeven wat je wilt, en `print()` zal zijn best
doen het op het scherm weer te geven. Vooralsnog zul je echter alleen
basis data types printen.

`print()` kan twee speciale parameters meekrijgen, die `sep` en `end`
heten.

`sep` geeft aan wat er getoond moet worden tussen iedere twee
parameters, en is als default een spatie. Je kunt die spatie wijzigen in
iets anders via `sep`, inclusief in een lege string.

`end` geeft aan wat `print()` moet tonen nadat alle parameters zijn
getoond, en is als default een "nieuwe regel." Door `end` te wijzigen
kun je ervoor zorgen dat `print()` iets anders doet dan naar een nieuwe
regel gaan als hij klaar is met het tonen van parameters.

On `sep` en `end` te gebruiken, moet je speciale parameters opnemen,
namelijk parameters `sep=<string>` en/of `end=<string>` (merk op: als in
een beschrijving van code je iets ziet dat tussen `<` en `>` staat,
betekent dat meestal dat je dat niet letterlijk moet typen, maar moet
vervangen door van wat de term tussen de `<` en `>` aangeeft, dus
`<string>` betekent dat je daar een string moet plaatsen). Bijvoorbeeld:

```python
print( "X", "X", "X", sep="x" )
print( "X", end="" )
print( "Y", end="" )
print( "Z" )
```

Als je deze code uitvoert, zie je twee regels. De eerste bevat "XxXxX,"
aangezien er is aangegeven dat er drie keer een hoofdletter "X"
afgedrukt moet worden met tussen iedere twee als separator een kleine
letter "x." De tweede regel bevat "XYZ", omdat weliswaar dit drie
verschillende aanroepen van `print()` betreft, maar na ieder van de
eerste twee er niet naar een volgende regel wordt gegaan.

### `format()`

`format()` is een nogal complexe functie die op een speciale manier
gebruikt moet worden. De functie staat je toe een geformatteerde string
te bouwen, dus een string waarin bepaalde waardes op een specifiek
geformatteerde manier zijn opgenomen. Om een voorbeeld te geven, stel je
voor dat ik de uitkomst van de berekening van een float wil tonen:

```python
print( 7/11 )
```

Nu stel ik dat je de uitkomst moet tonen met 3 decimalen. Dat zou je
kunnen doen met de `round()` functie, dus iets als:

```python
print( round( 7/11, 3 ) )
```

Dit werkt, maar misschien heb ik extra eisen. Misschien stel ik dat je
10 posities ruimte moet reserveren voor deze uitkomst, en dat je binnen
die 10 posities de uitkomst links moet aanlijnen. Dat lijkt lastig te
realiseren, maar middels de `format()` functie is het vrij eenvoudig om
waardes te formatteren op allerlei manieren. De volgende toepassing van
`format()` realiseert het afronden op drie decimalen:

```python
print( "{:.3f}".format( 7/11 ) )
```

`format()` "werkt" op een string. Tot op dit moment heb ik alleen
functies gebruikt die aangestuurd worden via parameters. Echter, er zijn
functies die alleen werken met een specifiek data type, en die op zo'n
manier gedefinieerd zijn dat een variabele (of waarde) van dat data type
vóór de functie naam moet staan, met een punt tussen de variabele (of
waarde) en de naam van de functie. De reden hiervoor is een techniek die
"object oriëntatie" heet, en die ik zal bediscussiëren in hoofdstukken
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
tot en met
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>.
Je hoeft nu alleen te weten dat zulke functie "methodes" genoemd worden,
en dat je, om ze aan te roepen, een variabele (of waarde) van het juiste
type voor de aanroep van de methode moet zetten, met een punt ertussen.
Die variabele (of waarde) zelf is ook beschikbaar voor de methode, net
als de parameters.

De `format()` methode (laten we de correcte benaming gebruiken, het is
geen functie maar een methode) wordt als volgt aangeroepen:
`<string>.format()`. Hij retourneert een nieuwe string, die een
geformatteerde versie is van de string waarvoor de methode is
aangeroepen. `format()` kan een willekeurig aantal parameters
meekrijgen, die in de geformatteerde string ingebracht kunnen worden op
specifieke plaatsen.

De plaatsen waar `format()` de parameter waardes in de string plaatst
worden in de string aangegeven middels accolades (`{` en `}`). Als je
alleen `{}` gebruikt om de parameters aan te duiden, worden ze van
links naar rechts afgehandeld. Bijvoorbeeld:

```python
    print( "De eerste drie getallen zijn {}, {} en {}.".format( 
        "een", "twee", "drie" ) )
```

Als je ze in een andere volgorde wilt afhandelen, kun je de volgorde
bepalen door een getal tussen de acolades te zetten. De eerste parameter
is nummer 0, de tweede nummer 1, de derde nummer 2, etcetera (als je het
vreemd vindt om nummering te beginnen bij nul, weet dan dat dat
gebruikelijk is in programmeertalen, en dat je het nog vaker zult
tegenkomen in dit boek). Bijvoorbeeld:

```python
print( "Achterwaarts zijn ze {2}, {1} en {0}.".format( 
    "een", "twee", "drie" ) )
```

`format()` kan variabelen van ieder type verwerken, zolang ze maar een
fatsoenlijke string representatie hebben. Bijvoorbeeld, `format()` kan
getallen verwerken, en zelfs verschillende soorten data types mixen:

```python
print( "De eerste drie getallen zijn {}, {} en {}.".format( 
    1, "twee", 3.0 ) )
```

Als je de parameters op een specifieke manier wil formatteren, zijn daar
mogelijkheden voor, als je een dubbele-punt (:) tussen de accolades zet,
na het volgorde-nummer als je dat gebruikt, met rechts van de
dubbele-punt formatteringsinstructies. Ik zal een aantal
formatteringsinstructies opnoemen.

Ik begin met instructies voor string parameters. Als je een bepaalde
hoeveelheid tekens wilt reserveren voor een string, dan kun je dat
aangeven met een integer rechts van de dubbele-punt. Dit wordt de
"precisie" genoemd. De volgende code gebruikt een precisie van 7.

```python
print( "De eerste drie getallen zijn {:7}, {:7} en {:7}.".format( 
    "een", "twee", "drie" ) )
```

Als de precisie te kort is voor de lengte van de string, neemt
`format()` gewoon meer ruimte voor de string. Je kunt de precisie dus
niet gebruiken om een string voortijdig af te breken.

```python
print( "De eerste drie getallen zijn {:3}, {:3} en {:3}.".format( 
    "een", "twee", "drie" ) )
```

Als je precisie gebruikt, kun je de parameter links aanlijnen,
centreren, of rechts aanlijnen in de ruimte die je hebt gereserveerd.
Dat doe je door een "alignment" teken te plaatsen tussen de dubbele punt
en de precisie. Deze "alignment" tekens zijn `<` voor links aanlijnen,
`^` voor centreren, en `>` voor rechts aanlijnen.

```python
print( "De eerste drie getallen zijn {:<7}, {:^7} en {:>7}.".
    format( "een", "twee", "drie" ) )
```

Ik ga nu over op formatteringsinstructies voor getallen. Als je een
getal wilt laten interpreteren als een integer, moet je de kleine letter
"d" plaatsen rechts van de dubbele punt ("d" staat hierbij voor
"decimaal"). Wil je dat het getal wordt geïnterpreteerd als een float,
dan moet je een "f" plaatsen rechts van de dubbele-punt. `format()`
maakt de juiste conversie voor je als dat kan. Je kunt echter niet van
een float een integer maken, want dat veroorzaakt een runtime error.

```python
print( "{} gedeeld door {} is {}".format( 1, 2, 1/2 ) )
print( "{:d} gedeeld door {:d} is {:f}".format( 1, 2, 1/2 ) )
print( "{:f} gedeeld door {:f} is {:f}".format( 1, 2, 1/2 ) )
```

Net als bij strings, kun je voor getallen precisie en aanlijning
gebruiken. Dit doe je op dezelfde manier. En net als bij strings geldt
dat als de precisie niet voldoende groot is, de functie gewoon de ruimte
neemt die nodig is. Let erop dat een eventueel min-teken en een
eventuele punt in een float ook plaats nodig hebben.

```python
print( "{:5d} gedeeld door {:5d} is {:5f}".format( 1, 2, 1/2 ) )
print( "{:<5f} gedeeld door {:^5f} is {:>5f}".format( 1,2,1/2 ))
```

Tenslotte, en misschien het meest nuttig, kun je aangeven met hoeveel
decimalen een float getoond moet worden, door een punt en een getal te
plaatsen links van de letter "f." De `format()` methode zal het getal
afronden tot het juiste aantal decimalen. Merk op dat je ook mag
aangeven dat je nul decimalen wilt zien door `.0` te gebruiken, wat
ervoor zal zorgen dat een float wordt getoond als een integer.

```python
print( "{:.2f} gedeeld door {:.2f} is {:.2f}".format( 1,2,1/2 ))
```

De combinatie van precisie, aanlijning, en decimalen staat je toe om
redelijk uitziende tabellen te tonen.

```python
s = "{:>5d} keer {:>5.2f} is {:>5.2f}"
print( s.format( 1, 3.75, 1 * 3.75 ) )
print( s.format( 2, 3.75, 2 * 3.75 ) )
print( s.format( 3, 3.75, 3 * 3.75 ) )
print( s.format( 4, 3.75, 4 * 3.75 ) )
print( s.format( 5, 3.75, 5 * 3.75 ) )
```
