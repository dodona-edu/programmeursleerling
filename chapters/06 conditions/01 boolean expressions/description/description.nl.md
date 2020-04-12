Een conditioneel statement, vaak een "if"-statement genoemd, bestaat uit
een test en één of meerdere acties. De test is een zogeheten "boolean
expressie." De acties worden alleen uitgevoerd als de test evalueert als
zijnde "waar." Bijvoorbeeld, een app op een smartphone kan een
waarschuwing geven als de batterij minder dan 5% vol is. Dat betekent
dat de app test of een zekere variabele `batterij_energie` kleiner is
dan $$5$$, dus of de vergelijking `batterij_energie < 5` als zijnde "waar"
geëvalueerd wordt. Als de variabele momenteel de waarde $$17$$ bevat,
evalueert de test `batterij_energie < 5` als zijnde "onwaar."

### Booleans

In Python wordt "waar" weergegeven door de waarde `True`, en "onwaar"
door de waarde `False`.

`True` en `False` zijn zogeheten "boolean waardes," die door Python zijn
gedefinieerd. `True` en `False` zijn zelfs de *enige* booleans, en alles
wat niet `False`, is automatisch `True`.

Als je je afvraagt welke data type `True` en `False` hebben: ze zijn van
het type `bool`. In Python kan echter elke waarde worden geïnterpreteerd
als boolean, ongeacht het data type. Dus als je een test doet of iets
`True` of `False` is, en je test dat van een waarde die niet van het
data type `bool` is, dan wordt hetgeen je test toch als ofwel `True`
ofwel `False` beschouwd.

The volgende waardes worden beschouwd als zijnde `False`:

-   De speciale waarde `False`

-   De speciale waarde `None` (die ik heb besproken in hoofdstuk
    <a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>)

-   Iedere numerieke waarde die nul is, bijvoorbeeld 0 en 0.0

-   Iedere lege serie, bijvoorbeeld een lege string (`""`)

-   Iedere lege "afbeelding," bijvoorbeeld een lege "dictionary"
    (dictionaries zijn het onderwerp van hoofdstuk
    <a href="#ch:dictionaries" data-reference-type="ref" data-reference="ch:dictionaries">14</a>)

-   Iedere functie of methode die één van de bovenstaande waardes
    retourneert (inclusief functies die niks retourneren)

Iedere andere waarde wordt beschouwd als zijnde `True`.

Een expressie die evalueert als `True` of `False` heet een "boolean
expressie."

### Vergelijkingen

De meestgebruikte boolean expressies zijn vergelijkingen. Een
vergelijking bestaat uit twee waardes met een vergelijkingsoperator
ertussen. Vergelijkingsoperatoren zijn:

| operator | description |
|:--------:|-------------|
|        `<`  |    kleiner dan |
|        `<=` |  kleiner dan of gelijk aan |
|        `==`  | gelijk aan |
|        `>=` |  groter dan of gelijk aan |
|        `>`  |  groter dan |
|        `!=` |  niet gelijk aan |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Een veelgemaakte fout is om twee waardes te vergelijken met een enkele
$$=$$. De enkele $$=$$ is de assignment operator. Meestal (maar niet altijd)
produceert Python een syntax of runtime error als je de $$=$$ probeert te
gebruiken om twee waardes te vergelijken.

Je kunt vergelijksoperatoren gebruiken zowel tussen getallen als tussen
strings. Vergelijkingen tussen strings zijn alfabetische vergelijkingen,
waarbij je wel moet bedenken dat hoofdletters altijd beschouwd worden
als kleiner dan kleine letters (en cijfers kleiner dan alle letters). Ik
ga daar dieper op in in hoofdstuk
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>.

Hier volgen een paar voorbeelden van vergelijkingen:

```python
print( "1.", 2 < 5 )
print( "2.", 2 <= 5 )
print( "3.", 3 > 3 )
print( "4.", 3 >= 3 )
print( "5.", 3 == 3.0 )
print( "6.", 3 == "3" )
print( "7.", "syntax" == "syntax" )
print( "8.", "syntax" == "semantiek" )
print( "9.", "syntax" == " syntax" )
print( "10.", "Python" != "rotzooi" )
print( "11.", "Python" > "Perl" )
print( "12.", "banaan" < "mango" )
print( "13.", "banaan" < "Mango" )
```

Zorg dat je deze vergelijkingen uitvoert, en dat je snapt waarom ze de
uitkomst geven die ze geven!

Begrijp je waarom `3 < 13` `True` oplevert, maar `"3" < "13"` `False`
oplevert? Indien niet, denk er dan goed over na!

Je kunt de uitkomst van een boolean expressie aan een variabele
toekennen als je wilt:

```python
groter = 5 > 2
print( groter )
groter = 5 < 2
print( groter )
print( type( groter ) )
```

Schrijf code die test of $$1/2$$ groter dan, gelijk aan, of kleiner is dan
$$0.5$$. Doe dat ook voor $$1/3$$ en $$0.33$$. Doe het dan ook voor $$(1/3)*3$$
en $$1$$.

Vergelijkingen tussen data types die niet vergeleken kunnen worden,
leiden meestal tot runtime errors.

```python
# Deze code geeft een runtime error.
print( 3 < "3" )
```

### `in` operator

Python heeft een speciale operator die de "lidmaatschap test operator"
heet, en die vanwege die onverkwikkelijke mondvol meestal de "in
operator" wordt genoemd aangezien hij gecodeerd wordt als `in`. De `in`
operator test of een waarde voorkomt in een collectie, als de waarde
links van de `in` staat, en de collectie rechts van de `in`.

Er zijn verschillende soorten collecties in Python, maar de enige die ik
tot op dit moment bediscussiëerd heb is de string. Een string is een
collectie van tekens. Je kunt testen of een specifiek teken, of een
groepje tekens, onderdeel is van een string middels de `in` operator. De
tegenhanger van de `in` operator is de `not in` operator, die `True`
oplevert als `in` `False` oplevert, en vice versa. Bijvoorbeeld:

```python
print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" )
print( "y" not in "Python" )
```

Zorg er weer voor dat je deze evaluaties begrijpt!

Schrijf code die test van ieder van de klinkers (`"a"`, `"e"`, `"i"`,
`"o"`, `"u"`) of ze voorkomen in je naam. Je mag hoofdletters negeren.

### Logische operatoren

Boolean expressies kunnen gecombineerd worden middels logische
operatoren. Er zijn drie logische operatoren: `and`, `or`, en `not`.

`and` en `or` plaats je tussen twee boolean expressies.

Als `and` tussen twee boolean expressies staat, is het resultaat `True`
als beide expressies `True` zijn; anders is het resultaat `False`.

Als `or` tussen twee boolean expressies staat, is het resultaat `True`
als één of beide expressies `True` zijn; het resultaat is alleen `False`
als beide `False` zijn.

`not` kun je voor een boolean expressie plaatsen om hem om te keren van
`True` naar `False` en vice versa.

Bijvoorbeeld:

```python
t = True
f = False
print( t and t )
print( t and f )
print( f and t )
print( f and f )
print( t or t )
print( t or f )
print( f or t )
print( f or f )
print( not t )
print( not f )
```

Kijk uit met het gebruik van logische operatoren, want een combinatie
van `and`s en `or`s kan leiden tot onverwachte resultaten. Gebruik
haakjes om te zorgen dat ze in de gewenste volgorde geëvalueerd worden.
Bijvoorbeeld, in plaats van `a and b or c` te schrijven, moet je
`(a and b) or c` of `a and (b or c)` schrijven (afhankelijk van de
gewenste volgorde), zodat het duidelijk is welke evaluatie je wilt
uitvoeren. Zelfs als je weet in welke volgorde Python de evaluatie doet
zonder haakjes, hoeft dat niet te gelden voor iemand anders die je code
leest.

Geef voor de code hieronder waardes voor `a`, `b`, and `c`, die ertoe
leiden dat de twee expressies verschillende uitkomsten hebben.

```python
a = # True of False?
b = # True of False?
c = # True of False?

print( (a and b) or c )
print( a and (b or c) )
```

Als je logische expressie maakt met alleen `and`s, of alleen `or`s, hoef
je geen haakjes te gebruiken, want dan is er slechts één mogelijke
evaluatie van de expressie.

Boolean expressies worden van links naar rechts geëvalueerd, en Python
stopt de evaluatie op het moment dat de uitkomst van de evaluatie bekend
is. Neem bijvoorbeeld de volgende code:

```python
x = 1
y = 0
print( (x == 0) or (y == 0) or (x / y == 1) )
```

Als je deelt door nul, geeft Python een runtime error, dus de evaluatie
van `x / y == 1` geeft een error als `y` nul is. En als je de code
bestudeert, zie je dat `y` inderdaad nul is. Maar de code geeft geen
foutmelding. Python evalueert de boolean expressie van links naar
rechts, en ziet op een gegeven moment `… or (y == 0) or …`. `y == 0`
evalueert als `True`. Omdat een expressie die via `or`s gecombineerd is
`True` is als één van de componenten `True` is, kan Python na evaluatie
van `(y == 0)` concluderen dat deze hele expressie `True` is. Het is dus
niet nodig dat Python `x / y == 1` evalueert, en Python doet dat dan ook
niet. Het is wel van belang dat `y == 0` links van `x / y == 1` staat,
zodat Python `y == 0` eerst test.

Merk op dat hoewel je heel ingewikkelde boolean expressies kunt bouwen
via logische operatoren, ik je aanraad dat je je expressies zo eenvoudig
mogelijk houdt. Eenvoudige expressies houden code leesbaar.
