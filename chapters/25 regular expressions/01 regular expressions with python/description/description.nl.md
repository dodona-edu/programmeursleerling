Reguliere expressies zijn tekst strings die een "patroon" beschrijven
dat je kunt vinden in tekstuele data. Bijvoorbeeld, de reguliere
expressie `a+` beschrijft een patroon dat bestaat uit een serie van één
of meer keer de letter "a." In de string "aardvarken" vind je dit
patroon twee keer, namelijk de "aa" aan het begin van het woord, en de
enkele "a" in de tweede helft van het woord.

Een reguliere expressie bestaat altijd uit een string, die ieder teken
mag bevatten. Sommige tekens zijn "meta-tekens" die een speciale
betekenis hebben in reguliere expressies. Je moet voorzichtig zijn met
ze te gebruiken (hoe je ze gebruikt volgt later). De meta-tekens zijn:


    . ^ $ * + ? { } [ ] \ | ( )

Ik ga later in dit hoofdstuk uitleggen hoe je reguliere expressies
samenstelt. Ik moet eerst bediscussiëren hoe je reguliere expressies
opneemt in Python code.

### De `re` module

Om reguliere expressies in Python te gebruiken, moet je de `re` module
importeren.

Een reguliere expressie kun je beschouwen als een stuk code. Die code
kun je "compileren" via de `re` module om een "patroon object" te
produceren. Dat patroon object kun je dan gebruiken om te zoeken naar
het patroon in data. Bijvoorbeeld, in de volgende code wordt de
reguliere expressie `a+` gecompileerd om een patroon object te
produceren dat wordt opgeslagen als `pAplus`. Dat patroon object wordt
vervolgens gebruikt om het patroon te zoeken in de string "aardvarken."
De patronen die gevonden worden, worden opgeslagen in een list, en die
list wordt dan geprint.

```python
import re

pAplus = re.compile( r"a+" )
lAplus = pAplus.findall( "aardvarken" )
print( lAplus )
```

Verander het woord "aardvarken" in de code hierboven in iets anders, en
bekijk hoe de uitvoer verandert.

Je vraagt je misschien af wat die letter "r" doet voor de string die de
reguliere expressie bevat. Waarom schreef ik `r"a+"` in plaats van
gewoon `"a+"`? Deze letter "r" vertelt Python dat deze string beschouwd
moet worden als "ruwe data," dat wil zeggen, dat Python niet moet
proberen delen van de string te converteren via de standaard Python
string interpretaties. Dat is met name belangrijk als de reguliere
expressie een `"\\b"` bevat, wat voor reguliere expressies betekent
"woord begrenzing" (dat leg ik later in dit hoofdstuk uit), maar voor
Python een speciaal teken is dat "backspace" betekent. Dus je doet er
goed aan die letter "r" altijd voor reguliere expressies op te nemen, om
problemen te voorkomen.

Hoewel het in de praktijk niet veel voorkomt, mag je een optionele
tweede parameter (een zogeheten "vlag") opnemen in de aanroep van
`compile()`, die aangeeft dat het patroon op een speciale manier
verwerkt moet worden. Het argument `re.I` geeft aan dat er geen
onderscheid gemaakt moet worden tussen hoofd- en kleine letters, terwijl
`re.S` aangeeft dat het patroon ook "newlines" moet verwerken, en `re.M`
aangeeft dat het patroon de meta-tekens `^` en `\$` moet toepassen op
iedere regel tekst, en niet alleen de tekst als geheel. Je mag deze
argumenten met elkaar combineren middels pipe-lines (`|`).

### Verkorte compilatie

Het is toegestaan om de compilatie-stap over te slaan, en het zoeken van
het patroon aan te roepen met een "class call" in de `re` module. In
plaats van methodes aan te roepen van het patroon object, kun je de
methodes direct aanroepen voor `re`, waarbij de reguliere expressie als
eerste parameter wordt opgegeven. De code hierboven wordt dan:

```python
import re

lAplus = re.findall( r"a+", "aardvarken" )
print( lAplus )
```

Als je deze code uitvoert, zie je dat de uitvoer precies gelijk is aan
die van de eerste code. De tweede manier compileert nog steeds de
reguliere expressie, maar slaat het patroon object niet op. Als het
patroon slechts een paar keer in de code gebruikt wordt, dan is deze
manier prima. Als het patroon echter vaak gebruikt wordt, is de eerste
methode te prefereren, omdat de compilatie van de reguliere expressie
(wat de meeste tijd in beslag neemt) slechts eenmalig gedaan wordt, in
plaats van iedere keer.

### Match objecten

De `findall()` methode die ik hierboven gebruikte retourneert alle
instanties van het patroon in de string waarin gezocht wordt. Vaak heb
je meer informatie nodig dan alleen de patronen; bijvoorbeeld, je wilt
misschien weten waar precies in de string het patroon staat. De `re`
module heeft methodes die resulteren in zogeheten "match objecten," wat
objecten zijn die behalve het tekstuele patroon meer informatie
bevatten, zoals de index waar het patroon gevonden is. Bijvoorbeeld, de
`search()` methode retourneert een match object voor de eerste instantie
waar het patroon in de string voorkomt.

```python
import re

m = re.search( r"a+", "Kijk uit voor het aardvarken!" )
print( "{} gevonden op index {}".format( m.group(), m.start() ) )
```

Zoals je kunt zien heeft het match object diverse nuttige methodes. Deze
zijn:

-   `group()` die het gevonden patroon retourneert

-   `start()` die de index retourneert waar het patroon start

-   `end()` die de index retourneert waar het patroon geëindigd is

De `group()` methode heeft een aantal handige toepassingen die je via
argumenten kunt benaderen, wat ik later zal bespreken.

De `match()` methode lijkt op de `search()` methode, maar controleert of
het patroon bestaat bij de start van de string (dus beginnend bij index
0). Beide methodes retourneren `None` als het patroon niet gevonden is,
dat door Python als `False` beschouwd wanneer het als conditie gebruikt
wordt.

```python
import re

m = re.match( r"a+", "Kijk uit voor het aardvarken!" )
if m:
    print( "{} start de string".format( m.group() ) )
else:
    print( "Het patroon staat niet aan de start van de string" )    
```

### Lists van matches

Ik liet zien dat de `findall()` methode een list bouwt van de
voorkomende patronen. `findall()` wordt gecomplementeerd door de
`finditer()` methode, die een list (of liever gezegd, een iterator)
bouwt van match objecten voor het gezochte patroon. De beste manier om
zo'n list te verwerken is via de `for m in ...` constructie.
Bijvoorbeeld:

```python
import re

mlist = re.finditer( r"a+", 
    "Kijk uit! Een gevaarlijk aardvarken is ontsnapt!" )
for m in mlist:
    print( "{} gevonden bij index {} tot index {}.".format( 
        m.group(), m.start(), m.end() ) )
```
