Een functie is een blok herbruikbare code dat een bepaalde actie uitvoert.
Om een functie aan het werk te zetten, roep je hem aan (Engels: "call"),
met de parameters als de functie nodig heeft. Je hoeft niet te weten hoe
de functie precies werkt. Je hoeft slechts drie dingen te weten:

-   De naam van de functie

-   De parameters die de functie nodig heeft (als die er zijn)

-   De waarde die de functie teruggeeft (als er zo'n waarde is)

Ik ga deze elementen één voor één bespreken.

### Functienamen

Iedere functie heeft een naam. Net als variabele namen, mogen functie
namen alleen bestaan uit letters, cijfers, en underscores, en mogen ze
niet starten met een cijfer. Vrijwel alle standaard Python functies
bestaan alleen uit kleine letters. Gewoonlijk is de naam van een functie
een korte beschrijving van wat de functie doet.

Als je in een tekst refereert aan een functie, is het de gewoonte dat je
achter de naam van de functie een openings- en sluithaakje zet, omdat
functies in code altijd die haakjes hebben (zelfs al staat er niks
tussen de haakjes).

### Parameters

Sommige functies worden aangeroepen met parameters ("argumenten"), die
meestal verplicht zijn. De parameters worden geplaatst tussen de haakjes
die achter de functienaam staan. Als er meerdere parameters zijn, moet
je er komma's tussen zetten.

De parameters zijn de waardes die de programmeur aan de functie geeft om
te verwerken. Bijvoorbeeld, de functie `int()` wordt aangeroepen met één
parameter, namelijk de waarde waarvan de functie probeert een integer
representatie te maken. De `print()` functie mag worden aangeroepen met
een willekeurig aantal parameters (zelfs nul), die de functie op het
scherm zal tonen, waarna de functie naar een nieuwe regel op het scherm
zal gaan.

Over het algemeen is het zo dat een functie de waardes van de parameters
niet kan wijzigen. Bekijk bijvoorbeeld de volgende code:

```python
x = 1.56
print( int( x ) )
print( x )
```

Als je deze code uitvoert, zie je dat `int()` niet de waarde van `x`
heeft aangepast; de functie heeft alleen aan `print()` doorgegeven wat
de integer representatie van de waarde van `x` is. De reden dat dit zo
is, is dat over het algemeen alleen de waarde van parameters wordt
doorgegeven (Engels: "passed by value"). Dit betekent dat de functie
geen toegang heeft tot de variabelen die als parameters gebruikt worden,
maar dat de functie kopieën krijgt van de waardes die in de parameters
staan. Ik zeg "over het algemeen" omdat dit niet geldt voor alle data
types, maar het geldt in ieder geval voor de data types die tot op dit
moment bediscussieerd zijn. Pas in hoofdstuk
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>
ga ik spreken over data types die wel door functies gewijzigd kunnen
worden, en op dat moment zal ik dat heel duidelijk maken.

Als een functie meerdere parameters krijgt, maakt de volgorde uit.
Bijvoorbeeld, de standaard functie `pow()` krijgt twee parameters, en
rekent de waarde uit van de eerste die wordt verheven tot de macht
weergegeven door de tweede.

```python
basis = 2
exponent = 3
print( pow( basis, exponent ) )
```

De namen die aan de variabelen zijn gegeven doen niet ter zake, de
eerste wordt verheven tot de macht die de tweede is. Dus de volgende
code geeft een ander antwoord dan de vorige, omdat de variabelen in een
andere (nogal verwarrende) volgorde aan de functie worden doorgegeven.

```python
basis = 2
exponent = 3
print( pow( exponent, basis ) ) # verwarrende variabele namen 
```

Wat gebeurt er als je een functie aanroept met parameter waardes waarmee
de functie niet kan werken? Bijvoorbeeld, wat gebeurt er als ik `int()`
aanroep met een string die geen integer bevat, of `pow()` met strings in
plaats van getallen? Dat leidt meestal tot "runtime errors" (fouten
tijdens de uitvoering van code). Bijvoorbeeld, beide regels in de
volgende code leiden tot runtime errors.

```python
x = pow( 3, "2" )
y = int( "twee-en-een-half" )
```

### Retour waarde

Een functie heeft vaak een retour waarde. Als een functie een waarde
retourneert, kun je die in je code gebruiken. Bijvoorbeeld, de `int()`
functie retourneert een integer representatie van de parameter die is
meegegeven. Je kunt deze retour waarde in een variabele stoppen middels
een assignment, of je kunt de waarde op een andere manier gebruiken,
bijvoorbeeld deze onmiddellijk printen. Je kunt er zelfs voor kiezen
niks met de waarde te doen, maar in dat geval had het waarschijnlijk
weinig zin om de functie aan te roepen.

```python
x = 2.1
y = '3'
z = int( x )
print( z )
print( int( y ) )
```

Zoals je hierboven kunt zien, kun je zelfs functie aanroepen als
parameter meegeven aan een functie, bijvoorbeeld, in de laatste regel
van de code hierboven krijgt de `print()` functie als waarde een aanroep
van de `int()` functie mee. De aanroep van `int()` vindt dan plaats
voordat de `print()` wordt afgehandeld, dus de return waarde van `int()`
is een parameter voor `print()`.

Niet alle functies retourneren een waarde. Bijvoorbeeld, `print()` geeft
geen waarde terug. Als je niet uitkijkt, kan dit tot vreemd gedrag van
je code leiden. Voer maar eens de volgende code uit:

```python
print( print( "Hello, world!" ) )
```

Je ziet dat deze code twee regels print. De eerste bevat de tekst
"Hello, world!" en de tweede het woord "None." Wat betekent dat woord
"None"? Om dat te begrijpen, moet je uitpluizen hoe Python deze regel
code verwerkt.

Wanneer Python deze regel code bekijkt, ziet het eerst
`print( <iets> )`. Omdat `<iets>` een argument is, moet dat eerst
geëvalueerd worden. `<iets>` is `print( <nog_iets> )`. Omdat
`<nog_iets>` een argument is, moet Python dat eerst evalueren.
`<nog_iets>` is de string `"Hello, world\`"!. Die hoeft niet verder
geëvalueerd te worden, dus `print()` wordt uitgevoerd met als argument
`"Hello, world\`"!, en Python "vangt" de retour waarde van deze
uitvoering omdat die nodig is als `<iets>`.

En daar is het probleem: `print()` heeft geen retourwaarde, dus er is
niks wat Python kan substitueren voor `<iets>`. Voor dit soort situaties
heeft Python een speciale waarde die `None` heet. Dus het eerste
`print()` commando krijgt als argument `None` mee, en dat leidt ertoe
dat Python "None" op het scherm afdrukt.

`None` is een speciale waarde die aangeeft "geen waarde." Als je `None`
probeert af te drukken, drukt Python het woord "None" af, maar dat is
niet een string met de waarde `"None"`. Het woord geeft slechts aan dat
er niks af te drukken was. `None` is niet hetzelfde als een lege string
(`""`). Een lege string heeft nog steeds een waarde, namelijk een string
met lengte nul. `None` is geen string, geen float, geen integer, niks.
Dus wees voorzichting met het aanroepen van een functie als parameter;
als de functie geen retour waarde heeft, kunnen er vreemde dingen
gebeuren.

### Een functie is een zwarte doos

In de wereld van programmeurs betekent een "zwarte doos" iets waar je
wat in kunt stoppen en wat uit kunt halen, maar waarvan je niet kunt
zien hoe het van binnen werkt. Je mag een functie beschouwen als een
zwarte doos: het is niet van belang te weten hoe de functie werkt of hoe
de code in de functie eruit ziet. Slechts de naam, de parameters, en de
retour waarde moet je kennen om de functie te kunnen gebruiken. Het zou
kunnen dat de functie intern variabelen aanmaakt en berekeningen doet,
maar die hebben geen effect op de rest van de code.

…Tenminste, als de functie netjes geïmplementeerd is. Een functie die
geen effect heeft op de rest van de code heet een "pure functie." Alle
functies die ik hier bespreek zijn "pure functies." Maar het feit dat er
een aparte naam is voor functies die de rest van de code niet aantasten,
geeft al aan dat er ook functies bestaan die niet "puur" zijn. Dit is
het duidelijkst bij functies waar de gebruiker parameters aan mee geeft,
waarbij de inhoud van de variabelen die als parameter worden meegegeven
gewijzigd wordt. Dat kan niet voor iedere soort variabele. En als het
gebeurt kan dat best acceptabel zijn, als het de bedoeling is en goed
gedocumenteerd is. Zulke functies heten "modifiers." Ik bespreek ze in
een later hoofdstuk.

Vooralsnog mag je aannemen dat iedere functie die je gebruikt, geen
effect heeft op de rest van de code. Het is veilig om functies aan te
roepen.
