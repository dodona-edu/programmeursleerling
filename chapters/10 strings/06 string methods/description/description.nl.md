Er is een aantal methodes beschikbaar die ontworpen zijn om strings te
bewerken. Al deze methodes worden toegepast op een string om een
operatie uit te voeren. Omdat strings onveranderbaar zijn, zullen deze
methodes nooit de string waarop ze werken wijzigen, maar ze retourneren
in plaats daarvan een gewijzigde versie van de string.

Net als de `format()` methode die in hoofdstuk
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>
besproken is, worden al de string methodes aangeroepen via de syntax
`<string>.<methode>()`, met andere woorden, je specificeert de string
waarop de methode moet werken, gevolgd door een punt, gevolgd door de
methode. Je zult dit vanaf nu vaker tegenkomen, en de reden dat methodes
op deze manier aangeroepen moeten worden volgt in latere hoofdstukken
(<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
en verder).

De meeste string methodes zijn geen deel van een module, en je kunt ze
aanroepen zonder iets te moeten importeren. Er is een `string` module
die bepaalde nuttige constanten en methodes bevat die je in je
programma's kunt gebruiken, maar de methodes die ik hier noem kun je
gebruiken zonder de `string` module te importeren.

### `strip()`

`strip()` verwijdert spaties aan het begin en einde van een string,
inclusief eventuele "newline" tekens en andere tekens die als spaties
gezien kunnen worden. Als je iets anders dan spaties wilt verwijderen,
kun je als parameter een string meegeven die bestaat uit alle te
verwijderen tekens.

```python
s = "    En nu iets heel anders \n    "
print( "["+s+"]" )
s = s.strip()
print( "["+s+"]" )
```

### `upper()` en `lower()`

`upper()` creëert een versie van een string met alle letters als
hoofdletters. `lower()` werkt op dezelfde manier, maar maakt van alle
letters kleine letters. Geen van beide methodes heeft parameters.

```python
s = "The Meaning of Life"
print( s )
print( s.upper() )
print( s.lower() )
```

### `find()`

`find()` kun je gebruiken om in een string te zoeken naar de start-index
van een bepaalde substring. Als parameter krijgt de methode de gezochte
substring. Optioneel kan een tweede, numerieke parameter meegegeven
worden die aangeeft bij welke index gestart moet worden met zoeken. Een
optionele derde, numerieke parameter is de index waarbij het zoeken moet
stoppen. Je krijgt de laagste index waarbij de substring gevonden wordt
terug, of -1 als de substring niet voorkomt.

```python
s = "Humpty Dumpty zat op de muur"
print( s.find( "zat" ) )
print( s.find( "t" ) )
print( s.find( "t", 12 ) )
print( s.find( "q" ) )
```

### `replace()`

`replace()` vervangt alle instanties van een substring in een string
door een andere substring. Als parameters krijgt het de substring die
gezocht wordt, en de substring die als vervanging dient. Optioneel kan
een derde, numerieke parameter meegegeven worden die aangeeft hoe vaak
een vervanging moet plaatsvinden.

Ik wil hier nogmaals benadrukken dat strings onveranderbaar zijn, dus de
`replace()` functie maakt niet echt vervangingen in de string; hij
retourneert een nieuwe string die een kopie is van de originele string,
waarbij de vervangingen zijn gemaakt.

```python
s = 'Humpty Dumpty zat op de muur'
print( s.replace( 'zat op', 'viel van' ) )
```

### `split()`

`split()` splitst een string op in woorden, gebaseerd op een gegeven
teken of substring die als separator beschouwd wordt. De separator is
een parameter, en als die niet is opgegeven, is de separator de spatie,
wat inhoudt dat je een string inderdaad opsplitst in de afzonderlijke
woorden (waarbij interpunctie die aan woorden vastzit beschouwd wordt
als een onderdeel van de desbetreffende woorden). Als de separator
meerdere keren naast elkaar staat, dan worden de extra separatoren
genegeerd (dat wil zeggen dat met spaties als separator, het niet
uitmaakt of er tussen twee woorden één spatie staat, of meerdere).

Het resultaat van deze opsplitsing is een "lijst" van woorden. Lijsten
komen aan bod in hoofdstuk
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>,
dus ik ga er nu weinig over zeggen. Ik zeg alleen dat als je de
afzonderlijke woorden in de lijst wilt benaderen, je de constructie
`for <woord> in <``lijst``>` kunt gebruiken.

```python
s = 'Humpty Dumpty      zat   op de muur   '
lijst = s.split()
for woord in lijst:
    print( woord )
```

Een nuttige toepassing van het opsplitsen van een string is dat je het
kunt gebruiken om sommige basale bestandsformaten te decoderen.
Bijvoorbeeld, een CSV (Comma-Separated Value) bestand is een eenvoudig
formaat, waarbij iedere regel van het bestand bestaat uit waardes die
van elkaar gescheiden zijn door komma's. De waardes kun je uit een regel
halen middels de `split()` methode.[^13]

```python
csv = "2016,september,28,Data Processing,Tilburg University"
waardes = csv.split( ',' )
for waarde in waardes:
    print( waarde )
```

### `join()`

`join()` is de tegenhanger van `split()`. `join()` plakt een lijst van
woorden aaneen tot een string, waarbij de woorden in de string van
elkaar gescheiden zijn middels een specifieke separator. Dit klinkt
wellicht alsof dit een methode van lijsten zou moeten zijn, maar om
historische redenen is het gedefinieerd als een string methode. Omdat
alle string methodes worden aangeroepen als `<string>.<methode>()`, moet
er een string staan voor de aanroep van `join()`. Die string is de
separator die je wilt gebruiken, terwijl de parameter die je meegeeft de
lijst is waarvan je de woorden aan elkaar wilt plakken. De retourwaarde
is, als altijd, de resulterende string.

```python
s = "Humpty;Dumpty;zat;op;de;muur"
lijst = s.split( ';' )
s = " ".join( lijst )
print( s )
```

### Oefening

In de string
`"Barbara had een bar, waar ze rabarbar verkocht, en die daarom de rabarbarbarbarabar werd genoemd."`
is het woord `"rabarber"` verkeerd gespeld. Gebruik `replace()` om alle
voorkomende gevallen van deze fout te verbeteren.

Neem de string `"Niemand verwacht de Spaanse Inquisitie\`\# In feite,!
`zij die de Spaanse Inquisitie wel verwachten..."` en toon hem tot aan,
maar niet inclusief, de hash mark (\#). Gebruik `find()` om de index van
de hash mark te bepalen.

Schrijf een programma dat een "schone" versie van alle woorden in de
string print. Alle tekens die geen letter zijn, worden niet beschouwd
als deel van een woord, maar als separator. Alle letters moeten in
kleine letters worden omgezet. Bijvoorbeeld, de string
`"Ik heb zo'n honger."` produceert vijf woorden, namelijk `"ik"`,
`"heb"`, `"zo"`, `"n"`, en `"honger"`. Je kunt de functie die je eerder
hebt geschreven voor het schoonmaken van strings hier gebruiken.

[^13]: In werkelijkheid is het vaak iets ingewikkelder omdat er komma's
    kunnen staan in de waardes die zijn opgeslagen in het CSV bestand,
    dus het is afhankelijk van de inhoud van het bestand of de genoemde
    aanpak werkt. Ik ga meer zeggen over CSV bestanden in hoofdstuk
    <a href="#ch:fileformats" data-reference-type="ref" data-reference="ch:fileformats">27</a>.

