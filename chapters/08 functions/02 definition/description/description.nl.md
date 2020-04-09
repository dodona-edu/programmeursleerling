Hoofdstuk
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>
beschrijft hoe iedere functie een naam heeft, nul of meer parameters, en
mogelijk een retourwaarde. Als je je eigen functies maakt, moet je al
deze elementen definiëren. Je gebruikt de volgende syntax:

```python
def <functie_naam>( <parameter_lijst> ):
    <acties>
```

Functienamen moeten voldoen aan dezelfde eisen als variabele namen, dat
wil zeggen, alleen letters, cijfers, en underscores, en ze mogen niet
beginnen met een cijfer. De parameter lijst bestaat uit nul of meer
variabele namen, met komma's ertussen. Het blok code onder de functie
definitie moet inspringen.

Let erop dat Python je functie definitie moet hebben "gezien" voordat je
de functie kunt aanroepen. Het is daarom de gewoonte dat functie
definities bovenin een programma staan, meteen onder de `import`
statements.

### Hoe Python omgaat met functies

Om functies te kunnen creëren, moet je begrijpen hoe Python met functies
omgaat. Bekijk het kleine Python programma hieronder. Dit programma
definieert één functie, die `totZiens()` heet. Deze functie heeft geen
parameters. Het blok code behorende bij de functie heeft alleen een
regel die de tekst "Tot ziens!" print.

De rest van het programma is geen deel van de functie. Het deel van de
code van een programma dat niet bij een functie hoort, noemt men meestal
het "hoofdprogramma" (Engels: "main program"). Het hoofdprogramma print
de regel "Hallo!," en roept daarna de functie `totZiens()` aan.

```python
def totZiens():
    print( "Tot ziens!" )

print( "Hallo!" )
totZiens()
```

Als je dit programma uitvoert, zie je dat het eerst de regel "Hallo!"
afdrukt, en daarna "Tot ziens!" Dit gebeurt zo ondanks het feit dat
Python de code van boven naar beneden uitvoert; Python komt
`print( "Tot ziens\`" )! tegen voordat `print( "Hallo\`" )! wordt
aangetroffen. De reden dat Python toch eerst de tekst "Hallo!" afdrukt
is dat Python de code van een functie alleen uitvoert als de functie
wordt aangeroepen. Een functie die Python tegenkomt voordat de functie
wordt aangeroepen wordt alleen geregistreerd – Python onthoudt dat die
functie bestaat, zodat hij kan worden uitgevoerd als het hoofdprogramma
(of een andere functie) de functie aanroept.

### Parameters en argumenten

Bekijk de code hieronder. De code definieert een functie `hallo()` met
één parameter, `naam` geheten. De functie gebruikt `naam` in het blok
code. Er is geen expliciete assignment die `naam` een waarde geeft.
`naam` bestaat als variabele naam omdat het een parameter is van de
functie.

Als een functie wordt aangeroepen, moet je een waarde geven aan iedere
(verplichte) parameter die voor de functie gedefinieerd is. Zo'n waarde
wordt een "argument" genoemd. Dus, om de functie `hallo()` aan te
roepen, moet een argument waarde voor de parameter `naam` gespecificeerd
worden. Je plaatst een argument tussen de haakjes van de functie
aanroep. Merk op dat het niet nodig is dat je in het hoofdprogramma weet
dat de parameter `naam` wordt genoemd in de functie. Hoe hij heet is
niet belangrijk. Het enige wat je moet weten is dat er een parameter is
die een waarde nodig heeft, en liefst ook de beperkingen die de functie
oplegt aan de waarde (bijvoorbeeld het type parameter dat de schrijver
van de functie wilt dat je meegeeft).

```python
def hallo( naam ):
    print( "Hallo, {}!".format( naam ) )

hallo( "Groucho" )
hallo( "Chico" )
hallo( "Harpo" )
hallo( "Zeppo" )
```

Parameters van een functie zijn niet meer en niet minder dan variabelen
die je kunt gebruiken in de functie, en die hun (initiële) waarde
krijgen van buiten de functie (namelijk via de functie aanroep). De
parameters zijn "lokaal" voor de functie, dat wil zeggen, ze kunnen niet
benaderd worden door code die niet in het blok code van de functie
staat, noch kunnen ze waardes van variabelen buiten de functie
beïnvloeden. Meer hierover volgt later in dit hoofdstuk.

Functies kunnen meerdere parameters hebben. Bijvoorbeeld, de volgende
functie krijgt twee parameters en vermenigvuldigt hun waardes, waarna
het resultaat wordt afgedrukt:

```python
def vermenigvuldig( x, y ):
    resultaat = x * y
    print( resultaat )

vermenigvuldig( 2020, 5278238 )
vermenigvuldig( 2, 3 )
```

### Parameter types

In veel programmeertalen
moet je bij de definitie van een functie aangeven wat de types van de
parameters zijn. Dit zorgt ervoor dat de compiler/interpreter kan
controleren of de functie met de juiste soort argumenten wordt
aangeroepen. Bij Python geef je geen data types aan. Dit betekent dat,
bijvoorbeeld, de `vermenigvuldig()` functie hierboven kan worden
aangeroepen met string argumenten. Als je dat doet, veroorzaakt dat een
runtime error (want je kunt geen strings met elkaar vermenigvuldigen).

Als je een "veilige" functie wilt schrijven, kun je het type argumenten
dat de functie meekrijgt testen met de `isinstance()` functie.
`isinstance()` krijgt een waarde of variabele mee als eerste argument,
en een data type als tweede argument. De functie geeft `True` als de
waarde of variabele van het genoemde type is, en anders `False`.
Bijvoorbeeld:

```python
a = "Hallo"
if isinstance( a, int ):
    print( "integer" )
elif isinstance( a, float ):
    print( "float" )
elif isinstance( a, str ):
    print( "string" )
else:
    print( "anders" )
```

Als je de parameters zo test, moet je natuurlijk wel besluiten wat je
doet als de functie met verkeerde argumenten is aangeroepen. De
standaard manier om dit af te handelen is door een "exception" te
genereren. Dat bespreek ik in hoofdstuk
<a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a>.
Vooralsnog mag je aannemen dat functies die je zelf schrijft worden
aangeroepen met argumenten van het correcte type. Zolang je alleen zelf
de functies gebruikt, kun je dat altijd garanderen.

### Default parameter waardes

Je kunt default waardes geven aan sommige parameters. Je doet dit door
bij het specificeren van de parameter een assignment operator (`=`) en
de gewenste waarde op te nemen, alsof het een reguliere assignment is.
Als je de functie aanroept, mag je een waarde voor alle parameters
opgeven, of slechts voor een aantal. De waardes worden aan de parameters
gegeven van links naar rechts. Als je minder waardes opgeeft dan er
parameters zijn, maar er default waardes gegeven zijn aan de parameters
waarvoor je niks opgeeft, krijg je geen runtime fouten. Als je een
functie definieert met default waardes voor een aantal parameters, maar
niet voor alle parameters, dan is het de gewoonte om de parameters
waarvoor je een default waarde opgeeft rechts te plaatsen van de
parameters waarvoor je geen default waarde hebt.

Als je de default waarde van een specifieke parameter wilt vervangen, en
je kent de naam van de parameter maar je weet niet waar hij staat in de
patameter-orde, of je wilt simpelweg de default waardes van de overige
parameters intact laten, dan kun je in de aanroep van de functie deze
*specifieke* parameter overschrijven door een assignment aan de
parameter op te nemen tussen de haakjes, dus
`<functie>( <parameternaam>=<waarde> )`.

De volgende code geeft voorbeelden van deze mogelijkheden:

```python
def vermenigvuldig_xyz( x, y=1, z=7 ):
    print( x * y * z )
    
vermenigvuldig_xyz( 2, 2, 2 ) # x=2, y=2, z=2
vermenigvuldig_xyz( 2, 5 )    # x=2, y=5, z=7
vermenigvuldig_xyz( 2, z=5 )  # x=2, y=1, z=5
```

### `return`

Parameters worden gebruikt om informatie van buiten de functie naar de
functie toe te communiceren. Vaak wil je ook informatie vanuit de
functie naar het programma buiten de functie toe communiceren. Daartoe
dient het commando `return`.

Als Python `return` tegenkomt in een functie, beëindigt dat de functie.
Python gaat dan verder met de code vlak na de plek waar de functie werd
aangeroepen. Je mag achter het woord `return` nul, één, of meerdere
waardes of variabelen opnemen. Deze waardes worden dan gecommuniceerd
naar het programma buiten de functie. Als je de waardes wilt gebruiken,
moet je zorgen dat ze in een variabele terecht komen. Dat krijg je voor
elkaar door de functie-aanroep te doen als een assignment naar een
variable.

Bijvoorbeeld, stel dat een functie wordt aangeroepen als
`<variabele> = <functie>()`. De functie maakt een berekening, die wordt
opgeslagen in een `<resultaat_variabele>`. Het commando
`return <resultaat_variabele>` beëindigt de functie, waarna de waarde
die in `<resultaat_variabele>` staat "uit de functie komt." Omdat
`<functie>()` was aangeroepen via een assignment, komt de waarde van
`<resultaat_variabele>` uiteindelijk terecht in `<variabele>`.

Ik snap dat dit wat ingewikkeld klinkt, maar het wordt waarschijnlijk
duidelijk als je het volgende voorbeeld bestudeert:

```python
from math import sqrt

def pythagoras( a, b ):
    return sqrt( a*a + b*b )

c = pythagoras( 3, 4 )
print( c )
```

De functie `pythagoras()` berekent de wortel van de som van de kwadraten
van de parameters. De uitkomst wordt via een `return` statement
geretourneerd. Het hoofdprogramma "vangt" de waarde door het toekennen
van de waarde aan de variabele `c`. Daarna wordt de inhoud van `c`
geprint.

Merk op dat het `return` statement in bovenstaande voorbeeld een
complete berekening meekrijgt. Die berekening wordt binnen de functie
uitgevoerd, en slechts de waarde die de uitkomst is van die berekening
wordt geretourneerd naar het hoofdprogramma.

Stel je nu voor dat je deze berekening alleen wilt uitvoeren met
positieve getallen (wat niet gek zou zijn, aangezien de functie
duidelijk bedoeld is om de lengte van de schuine zijde van een
rechthoekige driehoek te berekenen, en wie heeft er nu ooit gehoord van
een driehoek met zijden die nul of minder lang zijn). Bestudeer de
volgende code:

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return
    return sqrt( a*a + b*b )

print( pythagoras( 3, 4 ) )
print( pythagoras( -3, 4 ) )
```

Op het eerste gezicht is er niks mis met deze code: aangezien er niks te
berekenen is voor negatieve getallen, retourneert het geen waarde als er
een negatief argument wordt verstrekt. Echter, als je het programma
uitvoert zie je dat het de speciale waarde `None` afdrukt. Ik heb deze
speciale waarde besproken in hoofdstuk
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>.
Het hoofdprogramma verwacht dat de functie `pythagoras()` een getal
teruggeeft dat afgedrukt kan worden, dus `pythagoras()` voldoet niet aan
de verwachting aangezien het niets retourneert in bepaalde
omstandigheden. Je moet er altijd heel duidelijk over zijn welk data
type je functie retourneert, en ervoor zorgen dat een retourwaarde van
dat type ook altijd terugkomt, ongeacht de omstandigheden.

De volgende code is overigens equivalent met bovenstaande code (en bevat
dus dezelfde fout):

```python
from math import sqrt

def pythagoras( a, b ):
    if a > 0 and b > 0:
        return sqrt( a*a + b*b )

print( pythagoras( 3, 4 ) )
print( pythagoras( -3, 4 ) )
```

In deze code is niet expliciet zichtbaar dat er een `return` is zonder
waarde erachter, maar hij is er wel. Als Python de laatste regel van een
functie uitvoert, dan volgt daarna impliciet een `return`, en zal Python
dus uit de functie retourneren zonder waarde.

Wellicht vraag je je af wat je moet retourneren in omstandigheden
waarvoor je geen goede retourwaarde hebt. Dat hangt af van de
toepassing. Bijvoorbeeld, voor de functie `pythagoras()` zou je kunnen
besluiten dat je $$-1$$ retourneert als er iets niet in orde is met de
argumenten. Zolang je dat maar communiceert naar de gebruiker van de
functie, kan de gebruiker in het hoofdprogramma dit soort uitzonderlijke
omstandigheden naar wens afhandelen. Bijvoorbeeld:

```python
from math import sqrt
from pcinput import getInteger

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

num1 = getInteger( "Geef zijde 1: " )
num2 = getInteger( "Geef zijde 2: " )
num3 = pythagoras( num1, num2 )
if num3 < 0:
    print( "De getallen kunnen niet worden gebruikt." )
else:
    print( "De lengte van de diagonaal is", num3 )
```

Merk op dat iedere regel code die in een functie volgt na een `return`
op het zelfde niveau van inspringing altijd genegeerd zal worden.
Bijvoorbeeld, in de functie:

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
        print( "Deze regel wordt nooit uitgevoerd" )
    return sqrt( a*a + b*b )
```

geeft de regel onder `return -1` duidelijk aan hoe nutteloos hij is.

### Het verschil tussen `return` en `print`

In het verleden heb ik diverse malen geconstateerd dat veel studenten
moeite hebben met het verschil tusen een functie die een waarde
retourneert, en een functie die een waarde print. Vergelijk de volgende
twee stukken code:

```python
def print3():
   print( 3 )
print3()
```

en:

```python
def return3():
   return 3
print( return3() )
```

Zowel de functie `print3()` als de functie `return3()` worden
aangeroepen in hun respectievelijke hoofdprogramma's, en beide
resulteren in het printen van de waarde 3. Het verschil is dat bij
`print3()` dit printen gebeurt in de functie en de functie niks
retourneert, terwijl bij de functie `return3()` de waarde 3 wordt
geretourneerd, en geprint in het hoofdprogramma. Voor de gebruiker lijkt
er geen verschil te zijn: beide programma's printen 3. Voor een
programmeur zijn beide functies echter compleet verschillend.

De functie `print3()` kan voor slechts één doel gebruikt worden,
namelijk het tonen van het getal 3. De functie `return3()` kan echter
gebruikt worden waar je ook maar het getal 3 nodig hebt: om het te
tonen, om het te gebruiken in een berekening, of om het aan een
variabele toe te kennen. Bijvoorbeeld, de volgende code verheft 2 tot de
macht 3 en print de uitkomst:

```python
def return3():
   return 3
x = 2 ** return3()
print( x )
```

De code hieronder, echter, geeft een runtime error:

```python
def print3():
    print( 3 )
x = 2 ** print3() # Runtime error!
print( x )
```

De reden is dat hoewel `print3()` het getal 3 op het scherm toont (je
ziet het boven de runtime error als je de code uitvoert), het niet de
waarde 3 produceert op een manier dat een berekening er gebruik van kan
maken. De functie `print3()` geeft de speciale waarde `None`, en die kan
niet in een berekening gebruikt worden.

Dus als je een functie wilt maken die een waarde oplevert die elders in
je code gebruikt moet worden, dan moet die functie de waarde middels een
`return` retourneren. Als je een functie wilt maken die informatie
toont, dan kun je dat gewoon doen middels print statements in de
functie, en hoeft de functie niets te retourneren.

### De functie machine

Als je nog steeds moeite hebt met begrijpen hoe functies werken, denk
dan als volgt:

Een functie is net een grote machine, bijvoorbeeld, een machine die
pannenkoeken bakt. Er zijn input sleuven aan de bovenkant, met labels
"melk," "eieren," en "meel." Dat zijn de functie parameters. Je kunt
beïnvloeden wat voor pannenkoeken de machine bakt door de juiste
ingrediënten in de inputs te stoppen; bijvoorbeeld, als je volkoren
pannenkoeken wilt, doe je volkoren meel in de "meel" input. Natuurlijk
kunnen de zaken dramatisch fout lopen als je eieren in de "melk" input
doet – of als je probeert een kat in de "meel" input te stoppen.

Als de inputs gevuld zijn, begint de machine te ratelen. Je wacht
geduldig naast de output sleuf die (tot niemand's verrassing) het label
"return" draagt. Na enige tijd verschijnt er een pannenkoek in de
uitvoer. Die pannenkoek is de retourwaarde die de machine heeft
geproduceerd.

De machine heeft ook een display. Als je iets incorrects in de machine
stopt, komt daar wellicht een boodschap op in de trant van "Kat zit vast
in machine, herstarten alsjeblieft." Dit display is waar alles dat in de
machine geprint wordt verschijnt.

Je snapt wel dat het zinloos is als, nadat je de juiste ingrediënten
geladen hebt, de machine alleen maar op de display toont "Pannenkoek
gereed!" Je wilt een echte pannenkoek. Daarom moet de machine de
pannenkoek aanreiken via de "return," waarvandaan jij hem kunt aannemen
en "assignen" aan je lunch. Een tekst alleen is onvoldoende.

Een van de aardige dingen van de pannenkoek machine is dat zelfs als jij
niet weet hoe je een pannenkoek moet bakken, je toch pannenkoeken kunt
krijgen als je maar de juiste ingrediënten verstrekt. Dat is ook aardig
aan functies: ze kunnen complexe zaken voor je regelen, zonder dat je
hoeft te weten hoe ze dat doen.

![machine](media/Machine.png "machine"){:width="70%"}

### Meerdere retourwaardes

Je bent niet beperkt in je functies tot slechts één retourwaarde. Je
kunt meerdere waardes in één keer retourneren door er komma's tussen te
zetten. Als je deze waardes wilt gebruiken in je programma na aanroep
van de functies, moet je ze toekennen aan meerdere variabelen. Die zet
je allemaal aan de linkerkant van de assignment operator, ook met
komma's ertussen. Dit kan ik het beste illustreren aan de hand van een
voorbeeld:

```python
import datetime

def plusDagen( jaar, maand, dag, increment ):
    startdatum = datetime.datetime( jaar, maand, dag )
    einddatum = startdatum + datetime.timedelta( days=increment )
    return einddatum.year, einddatum.month, einddatum.day

y, m, d = plusDagen( 2015, 11, 13, 55 )
print( "{}/{}/{}".format( y, m, d ) )
```

De functie `plusDagen()` krijgt vier argumenten, namelijk integers die
een jaar, een maand, een dag, en een aantal dagen die je wilt optellen
bij de datum die wordt weergegeven door de eerste drie argumenten. Er
worden drie waardes geretourneerd, namelijk een nieuw jaar, een nieuwe
maand, en een nieuwe dag. De code stopt die in de variabelen `y`, `m`,
en `d`.

Als je de code hierboven bestudeert, vraag je je misschien af hoe
`plusDagen()` precies werkt. Zoals ik al zei, het is een voordeel van
functies dat zolang ze hun werk doen en je weet wat de argumenten zijn
en wat er geretourneerd wordt, dat je niet hoeft te weten hoe de functie
in elkaar zit. Je kunt de functie gebruiken zonder kennis van het
interne proces. Dus je mag gewoon negeren wat je in `plusDagen()` ziet
staan (overigens gebruikt de code van `plusDagen()` de `datetime`
module, die aan de orde komt in hoofdstuk
<a href="#ch:varioususefulmodules" data-reference-type="ref" data-reference="ch:varioususefulmodules">28</a>).

### Functies aanroepen vanuit functies

Functies mogen andere functies aanroepen, zolang die andere functies
maar bekend zijn bij de aanroepende functie. Bijvoorbeeld, hieronder zie
je hoe de functie `afstand()` de functie `pythagoras()` gebruikt om de
afstand te berekenen tussen twee punten in een 2-dimensionale ruimte.

```python
from math import sqrt

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

def afstand( x1, y1, x2, y2 ):
    return pythagoras( abs( x1 - x2 ), abs( y1 - y2 ) )

print( afstand( 1, 1, 4, 5 ) )
```

`afstand()` kent `pythagoras()`, omdat `pythagoras()` gedefinieerd is
vóór `afstand()` is aangeroepen.

Als je wilt, kun je functies *in* andere functies stoppen; met andere
woorden, je kunt functies "nesten." Bijvoorbeeld, je kunt de functie
`pythagoras()` in de functie `afstand()` stoppen. Dat betekent dat
`pythagoras()` kan worden aanroepen vanuit `afstand()`, maar niet op
andere plekken in de code.

```python
from math import sqrt

def afstand( x1, y1, x2, y2 ):

    def pythagoras_binnen( a, b ):
        if a <= 0 or b <= 0:
            return -1
        return sqrt( a*a + b*b )

    return pythagoras_binnen( abs( x1 - x2 ), abs( y1 - y2 ) )

print( afstand( 1, 1, 4, 5 ) )
# print( pythagoras_binnen( 3, 4 ) )
```

Het gebruik van geneste functies is wat uitzonderlijk, maar het is
mogelijk.

Merk op: Als je de hash mark verwijdert voor de laatste regel in de code
hierboven, wordt er een aanroep van `pythagoras_binnen()` toegevoegd
aan de code. Bij uitvoering van het programma geeft dat een runtime
error, omdat `pythagoras_binnen()` alleen zichtbaar is in de functie
`afstand()`.

Schrijf een functie `printx()` die alleen de letter "x" print. Schrijf
daarna een functie `meerderex()` die als argument een integer krijgt en
die zo vaak de letter "x" print als de integer aangeeft. Daartoe roept
de functie `meerderex()` zo vaak als nodig de functie `printx()` aan.

### Functienamen

Het is de gewoonte om namen van functies niet te laten beginnen met een
underscore (zulke functienamen zijn voorbehouden aan de ontwikkelaars
van Python zelf), en dat je probeert alleen kleine letters te gebruiken.
Als een functienaam uit meerdere woorden bestaat, kun je ofwel
underscores tussen die woorden zetten, ofwel ieder woord behalve het
eerste laten starten met een hoofdletter. Verschillende programmeurs
hebben hier verschillende meningen over, maar in de praktijk maakt het
niet zoveel uit omdat je een functie altijd kunt herkennen aan het feit
dat er haakjes achter de functienaam staan.

Bepaalde benamingen van functies zijn typerend voor bepaalde
functionaliteiten.

Een functie die test of een bepaald item een bepaalde eigenschap heeft,
en die dan `True` of `False` retourneert afhankelijk van het feit of de
eigenschap wel of niet aanwezig is, krijgt meestal een naam die begint
met het woord `is`, gevolgd door de naam van de eigenschap die start met
een hoofdletter. Bijvoorbeeld, een functie die test of een getal even
is, zou de naam `isEven()` krijgen.

Schrijf de functie `isEven()`.

Schrijf de functie `isOneven()`, die bepaalt of een getal oneven is,
door de functie `isEven()` aan te roepen en het resultaat te inverteren.

Merk op: Als je een functie als `isEven()` wilt gebruiken in een
conditionele expressie, bijvoorbeeld, als je een actie alleen wilt
uitvoeren als een getal even is, hoef je niet te schrijven
`if isEven( num ) == True:`. Je hoeft alleen maar te schrijven
`if isEven( num ):`, want de functie retourneert al `True` of `False`.
Een is-functie op zo'n manier gebruiken verhoogt de leesbaarheid van een
programma.

De naam van een functie die de waarde van een attribuut opvraagt en
retourneert, begint over het algemeen met het woord `get`, gevolgd door
de naam van de eigenschap, beginnend met een hoofdletter. Bijvoorbeeld,
een functie die van een float alleen het fractionele gedeelte (de
cijfers achter de komma) retourneert, zou heten `getFractie()`.[^9]

Schrijf de functie getFractie().

De tegenhanger van een "get" functie is een functie die een eigenschap
een bepaalde waarde geeft. De naam van zo'n functie begint meestal met
`set`, en is voor de rest gelijk aan een `get` functie. Ik kan op dit
punt geen voorbeeld van een `set` functie geven, aangezien ik nog niet
heb uitgelegd hoe een functie een waarde aan iets kan geven, aangezien
functies de waardes van de variabelen die als argumenten zijn meegegeven
niet kunnen wijzigen (tenminste, niet voor de data types die tot nu toe
zijn geïntroduceerd). Dit volgt in een later hoofdstuk.

Als je je aan dergelijke functiebenamingen houdt, wordt je code beter
leesbaar.

### Functie commentaar

In alle hoofdstukken tot nu toe heb ik weinig commentaar in code
geschreven. Boeken en cursussen die programmeren doceren moedigen
studenten vaak aan om commentaar aan code toe te voegen. Ikzelf ben van
mening dat code "zelf-documenterend" moet zijn, dat wil zeggen, dat je
gemakkelijk aan code kunt zien wat het doet door het te lezen. Je kunt
dat bereiken door goede namen te kiezen voor variabelen en functies,
door gebruik te maken van spaties en witregels, door nette inspringing
(wat gelukkig bij Python een noodzaak is), en door geen gebruik te maken
van "slimme" truukjes die je code een beetje sneller maken ten koste van
leesbaarheid, enkel en alleen om te laten zien hoe slim je bent.[^10]

Hoewel ik commentaar zie als iets extra's dat je alleen moet gebruiken
als er een noodzaak is om je code uit te leggen, is mijn opinie over
commentaar bij functies anders. Het idee achter een functie is dat de
gebruiker van de functie de code van de functie niet hoeft te kennen.
Daarom moet hetgeen de functie doet en hoe de functie werkt worden
uitgelegd middels commentaar, geschreven meteen boven de functienaam.

In commentaar bij een functie moet je drie zaken uitleggen:

-   Wat de functie doet

-   Welke argumenten de functie nodig heeft of accepteert, inclusief
    data types

-   Wat de functie retourneert, inclusief data types

Als een functie neveneffecten heeft, dus als een functie zaken buiten de
functie beïnvloedt, dan moet dat ook heel duidelijk in het
functiecommentaar staan. Ik heb dat niet in het lijstje hierboven
genoemd, omdat een functie *geen neveneffecten zou mogen hebben.*

Voor de antwoorden bij de opgaves in dit hoofdstuk heb ik commentaar aan
de functies toegevoegd op een manier die ik acceptabel acht. In volgende
hoofdstukken doe ik dat niet altijd, omdat ik de functies vaak in de
tekst bediscussieer, of omdat ik vind dat je de inhoud van een functie
moet bestuderen. Maar ik schrijf wel altijd commentaar bij functies die
ik voor andere doeleinden gebruik.

